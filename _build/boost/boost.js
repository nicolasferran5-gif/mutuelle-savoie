
/* ---- boost : formulaire en 2 étapes, barre d'appel sur mobile ---- */
(function () {
  document.querySelectorAll('form.lead-form').forEach(function (form) {
    var s1 = form.querySelector('.bx-step[data-s="1"]'), s2 = form.querySelector('.bx-step[data-s="2"]');
    if (!s1 || !s2) return;
    form.classList.add('js-steps'); form.dataset.step = '1';
    var lab = form.querySelector('.bx-steps span');
    function go(n) {
      form.dataset.step = String(n);
      if (lab) lab.textContent = 'Étape ' + n + ' sur 2';
      if (n === 2) { var f = s2.querySelector('input:not([type=hidden])'); if (f) try { f.focus({ preventScroll: true }); } catch (e) {} }
      if (window.gtag && n === 2) try { gtag('event', 'form_step_2', { site: CONFIG.site }); } catch (e) {}
    }
    var next = form.querySelector('.bx-next'), back = form.querySelector('.bx-back');
    if (next) next.addEventListener('click', function () { go(2); });
    if (back) back.addEventListener('click', function () { go(1); });
    form.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' && form.dataset.step === '1' && e.target.tagName !== 'TEXTAREA') { e.preventDefault(); go(2); }
    });
  });
  var bar = document.querySelector('.bx-sticky');
  if (bar) {
    var forms = document.querySelectorAll('.ticket');
    var onScroll = function () {
      var show = window.scrollY > 500;
      forms.forEach(function (t) { var r = t.getBoundingClientRect(); if (r.top < window.innerHeight - 80 && r.bottom > 80) show = false; });
      bar.classList.toggle('on', show);
    };
    window.addEventListener('scroll', onScroll, { passive: true }); onScroll();
  }
})();

/* ---- boost : diagnostic express, progression de lecture ---- */
(function () {
  var box = document.querySelector('[data-quiz]');
  if (box) {
    var items = [].map.call(box.querySelectorAll('.bx-quiz-list li'), function (li) {
      return { q: li.querySelector('strong').textContent, t: li.dataset.t, x: li.dataset.x, na: li.dataset.na === '1' };
    });
    var ans = [], i = 0, view = document.createElement('div'); box.appendChild(view); box.classList.add('on');
    function el(tag, cls, txt) { var e = document.createElement(tag); if (cls) e.className = cls; if (txt != null) e.textContent = txt; return e; }
    function ask() {
      view.innerHTML = '';
      var top = el('div', 'bx-q-top'); top.appendChild(el('span', '', 'Question ' + (i + 1) + ' sur ' + items.length));
      var dots = el('div', 'bx-q-dots'); items.forEach(function (_, k) { var d = el('i', k <= i ? 'd' : ''); dots.appendChild(d); }); top.appendChild(dots);
      view.appendChild(top); view.appendChild(el('p', 'bx-q-text', items[i].q));
      var row = el('div', 'bx-q-ans');
      [['Oui', 'oui'], ['Non', 'non'], ['Je ne sais pas', 'nsp']].concat(items[i].na ? [['Pas de cadre', 'na']] : []).forEach(function (o) {
        var b = el('button', '', o[0]); b.type = 'button';
        b.addEventListener('click', function () { ans[i] = o[1]; i++; if (i < items.length) ask(); else result(); });
        row.appendChild(b);
      });
      view.appendChild(row);
    }
    function result() {
      var ok = ans.filter(function (a) { return a === 'oui' || a === 'na'; }).length, n = items.length, bad = n - ok;
      view.innerHTML = '';
      var res = el('div', 'bx-q-res'), C = 2 * Math.PI * 52;
      res.innerHTML = '<svg class="bx-ring" viewBox="0 0 132 132" role="img" aria-label="' + ok + ' point(s) sur ' + n + ' en règle"><circle class="bg" cx="66" cy="66" r="52"/><circle class="fg" cx="66" cy="66" r="52" stroke-dasharray="' + C + '" stroke-dashoffset="' + C + '"/><text x="66" y="76" text-anchor="middle">' + ok + '/' + n + '</text></svg>';
      var txt = el('div');
      txt.appendChild(el('h3', '', bad === 0 ? 'Tout semble en ordre.' : bad + ' point' + (bad > 1 ? 's' : '') + ' à vérifier'));
      txt.appendChild(el('p', '', bad === 0 ? 'Reste à savoir si vous payez le bon prix : un comparatif gratuit le dit en quelques jours.' : 'Rien de grave si on s\'en occupe maintenant. Un conseiller reprend ces points avec vous, gratuitement.'));
      res.appendChild(txt);
      var ul = el('ul', 'bx-q-issues');
      items.forEach(function (it, k) {
        var good = ans[k] === 'oui' || ans[k] === 'na', li = el('li', good ? 'ok' : '');
        li.appendChild(el('strong', '', (good ? 'En règle : ' : 'À vérifier : ') + it.t)); if (!good) li.appendChild(el('span', '', it.x)); ul.appendChild(li);
      });
      res.appendChild(ul);
      var cta = el('div', 'bx-q-cta'), go = el('a', 'btn btn-red', 'Faire vérifier ces points gratuitement'); go.href = '#etude';
      go.addEventListener('click', function () {
        var form = document.querySelector('#etude form.lead-form'); if (!form) return;
        var m = form.elements.message; if (!m) { m = document.createElement('input'); m.type = 'hidden'; m.name = 'message'; form.appendChild(m); }
        m.value = 'Diagnostic express : ' + items.map(function (it, k) { return it.t + ' = ' + ans[k]; }).join(' ; ');
        [].forEach.call(form.querySelectorAll('input[name=besoin]'), function (r) { if (/audit/i.test(r.value)) r.checked = true; });
      });
      var again = el('button', 'link', 'Recommencer'); again.type = 'button'; again.addEventListener('click', function () { ans = []; i = 0; ask(); });
      cta.appendChild(go); cta.appendChild(again); res.appendChild(cta); view.appendChild(res);
      setTimeout(function () { res.querySelector('.fg').setAttribute('stroke-dashoffset', C * (1 - ok / n)); }, 60);
      if (window.gtag) try { gtag('event', 'diagnostic_termine', { site: CONFIG.site, score: ok }); } catch (e) {}
    }
    ask();
  }
  var pr = document.querySelector('.bx-progress i'), art = document.querySelector('article');
  if (pr && art) {
    var upd = function () { var r = art.getBoundingClientRect(), tot = r.height - window.innerHeight; pr.style.width = Math.max(0, Math.min(100, tot > 0 ? (-r.top / tot) * 100 : 0)) + '%'; };
    window.addEventListener('scroll', upd, { passive: true }); upd();
  }
})();

/* ---- boost : situations types en onglets ---- */
(function () {
  var box = document.querySelector('[data-sits]'); if (!box) return;
  var arts = [].slice.call(box.querySelectorAll('.bx-sit')), tabs = document.createElement('div');
  tabs.className = 'bx-sit-tabs'; tabs.setAttribute('role', 'tablist'); tabs.setAttribute('aria-label', 'Situations types');
  function show(k) { arts.forEach(function (a, i) { a.classList.toggle('cur', i === k); tabs.children[i].setAttribute('aria-selected', i === k ? 'true' : 'false'); }); }
  arts.forEach(function (a, i) {
    var b = document.createElement('button'); b.type = 'button'; b.setAttribute('role', 'tab'); b.textContent = a.dataset.tag;
    b.addEventListener('click', function () { show(i); }); tabs.appendChild(b);
  });
  box.insertBefore(tabs, box.firstChild); box.classList.add('on'); show(0);
  box.addEventListener('click', function (e) {
    var go = e.target.closest('.bx-sit-go'); if (!go) return;
    var form = document.querySelector('#etude form.lead-form'); if (!form) return;
    var m = form.elements.message; if (!m) { m = document.createElement('input'); m.type = 'hidden'; m.name = 'message'; form.appendChild(m); }
    m.value = 'Situation type choisie : ' + go.dataset.sit;
  });
})();

/* ---- boost : recherche dans le lexique ---- */
(function () {
  var inp = document.querySelector('[data-lex]'); if (!inp) return;
  var terms = [].slice.call(document.querySelectorAll('.bx-term')), empty = document.querySelector('.bx-lex-empty');
  function norm(t) { return t.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, ''); }
  inp.addEventListener('input', function () {
    var q = norm(inp.value.trim()), n = 0;
    terms.forEach(function (t) { var ok = !q || norm(t.textContent).indexOf(q) >= 0; t.hidden = !ok; if (ok) n++; });
    if (empty) empty.hidden = n > 0;
  });
})();

/* ---- boost : simulateur d'arrêt de travail (règles légales de maintien de salaire) ---- */
(function () {
  var box = document.querySelector('[data-arret]'); if (!box) return;
  var q = function (s) { return box.querySelector(s); };
  var day = q('[data-day]'), anc = q('[data-anc]');
  function calc() {
    var d = +day.value, a = +anc.value;
    var dur = a < 1 ? 0 : Math.min(90, 30 + 10 * Math.floor((a - 1) / 5));
    var secu = d >= 4 ? 50 : 0, total = secu, phase = '';
    if (a >= 1 && d >= 8 && d <= 7 + dur) { total = 90; phase = 'p1'; }
    else if (a >= 1 && d > 7 + dur && d <= 7 + 2 * dur) { total = 66.7; phase = 'p2'; }
    else if (d < 4) phase = 'carence';
    else if (a >= 1 && d < 8) phase = 'attente';
    else phase = 'fin';
    var emp = Math.max(0, total - secu), trou = 100 - total;
    q('[data-jour]').textContent = d;
    q('[data-b-secu]').style.width = secu + '%'; q('[data-b-emp]').style.width = emp + '%'; q('[data-b-trou]').style.width = trou + '%';
    var f = function (v) { return (Math.round(v * 10) / 10).toString().replace('.', ',') + ' %'; };
    q('[data-v-secu]').textContent = f(secu); q('[data-v-emp]').textContent = f(emp); q('[data-v-trou]').textContent = f(trou);
    var m = { carence: 'Jours 1 à 3 : délai de carence de la Sécurité sociale, le salarié ne perçoit rien sans prévoyance ni accord plus favorable.',
      attente: 'Jours 4 à 7 : seule la Sécurité sociale verse ses indemnités. Le complément de l\'employeur commence au 8e jour.',
      p1: 'L\'employeur complète jusqu\'à 90 % du salaire brut pendant ' + dur + ' jours. Une prévoyance peut lui rembourser ce coût.',
      p2: 'L\'employeur ne complète plus qu\'aux deux tiers du salaire brut, pendant ' + dur + ' jours.',
      fin: a < 1 ? 'Moins d\'un an d\'ancienneté : la loi n\'impose aucun complément à l\'employeur. Sans prévoyance, le salarié vit avec la moitié de son salaire.'
                 : 'Le maintien de salaire est terminé : sans prévoyance, le salarié ne perçoit plus que les indemnités de la Sécurité sociale.' };
    q('[data-msg]').textContent = m[phase];
  }
  day.addEventListener('input', calc); anc.addEventListener('change', calc); calc();
})();
