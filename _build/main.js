/* Bonne Cordée — scripts du site : menu, formulaires de demande, simulateur, check-up conformité. */
var CONFIG = {
  site: 'mutuelle-savoie.fr',
  marque: 'Bonne Cordée',
  emailjsPublicKey: 'O5AIQpxXdcsONBjCo',
  emailjsService: 'service_b1o3yyd',
  emailjsTemplate: 'template_4z3s4jd',
  preview: false,
  telephone: '01 87 66 70 31'
};

(function () {
  /* Menu mobile */
  var btn = document.querySelector('.menu-btn'), nav = document.querySelector('.nav');
  if (btn && nav) btn.addEventListener('click', function () {
    var open = nav.classList.toggle('open');
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
  });

  /* Formulaires de demande */
  try { if (window.emailjs && !CONFIG.preview) emailjs.init({ publicKey: CONFIG.emailjsPublicKey }); } catch (e) {}
  document.querySelectorAll('form.lead-form').forEach(function (form) {
    var box = form.closest('.ticket');
    var msg = form.querySelector('.form-msg');
    var submit = form.querySelector('[type=submit]');
    var ref = 'BC-' + new Date().toISOString().slice(2, 10).replace(/-/g, '') + '-' + Math.random().toString(36).slice(2, 6).toUpperCase();
    var refEl = box && box.querySelector('.ticket-ref');
    if (refEl) refEl.textContent = 'Fiche n° ' + ref;

    function val(name) {
      var el = form.elements[name]; if (!el) return '';
      if (el.length && !el.tagName) { for (var i = 0; i < el.length; i++) if (el[i].checked) return el[i].value; return ''; }
      return (el.value || '').trim();
    }
    function err(t, field) { msg.textContent = t; msg.hidden = false; if (field && form.elements[field]) form.elements[field].focus(); }

    form.addEventListener('submit', function (e) {
      e.preventDefault(); msg.hidden = true;
      var nom = val('nom'), email = val('email'), tel = val('tel');
      var consentEl = form.elements.consent, consent = consentEl && consentEl.checked;
      if (!nom) return err('Indiquez votre prénom et votre nom.', 'nom');
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) return err('Vérifiez votre adresse e-mail : elle semble incomplète.', 'email');
      if (consent && tel.replace(/\D/g, '').length < 9) return err('Pour être rappelé(e), indiquez un numéro de téléphone valide.', 'tel');

      var when = new Date().toLocaleString('fr-FR', { timeZone: 'Europe/Paris' });
      var consentText = form.querySelector('.consent-text') ? form.querySelector('.consent-text').textContent : '';
      var lines = [
        'Site source : ' + CONFIG.site + ' (' + CONFIG.marque + ')',
        'Référence : ' + ref,
        'Formulaire : ' + (form.dataset.origin || 'accueil'),
        'Type d\'établissement : ' + (val('type') || 'Non précisé'),
        'Besoin : ' + (val('besoin') || 'Non précisé'),
        'Nombre de salariés : ' + (val('salaries') || 'Non précisé'),
        'Code postal : ' + (val('cp') || 'Non renseigné'),
        'Échéance du contrat actuel : ' + (val('echeance') || 'Non renseignée'),
        'Message : ' + (val('message') || '—'),
        'Consentement au rappel téléphonique : ' + (consent ? 'OUI, le ' + when + ' (Europe/Paris). Texte accepté : « ' + consentText + ' »' : 'NON : répondre uniquement par e-mail, ne pas appeler.'),
        'Page : ' + location.href
      ];
      var params = {
        from_name: '[' + CONFIG.marque + '] ' + nom,
        email: email,
        telephone: tel || 'Non renseigné',
        entreprise: (val('etablissement') || 'Non renseigné') + ' — ' + (val('type') || 'Entreprise de montagne') + ' — via ' + CONFIG.site,
        salaries: val('salaries') || 'Non précisé',
        message: lines.join('\n'),
        reply_to: email
      };
      submit.disabled = true; var orig = submit.textContent; submit.textContent = 'Envoi en cours…';
      function ok() {
        form.hidden = true;
        var done = box.querySelector('.lead-done'); done.hidden = false;
        if (!consent) done.querySelector('.done-text').textContent = 'Un conseiller vous répond par e-mail sous 24 h ouvrées avec les premières pistes.';
        done.querySelector('.ref').textContent = 'Référence de votre demande : ' + ref + (CONFIG.preview ? ' · Aperçu : aucune demande envoyée' : '');
        if (window.gtag) try { gtag('event', 'generate_lead', { site: CONFIG.site }); } catch (e) {}
      }
      if (CONFIG.preview || !window.emailjs) { setTimeout(ok, 450); return; }
      emailjs.send(CONFIG.emailjsService, CONFIG.emailjsTemplate, params).then(ok).catch(function () {
        submit.disabled = false; submit.textContent = orig;
        err('L\'envoi n\'a pas abouti. Réessayez dans un instant, ou appelez le ' + CONFIG.telephone + '.');
      });
    });
  });

  /* Simulateur de coût (montagne : mutuelle et prévoyance au tarif et au taux du contrat) */
  var sim = document.getElementById('simulateur');
  if (sim) {
    var PASS_M = 4005, CAD = 0.015, FS = 0.08;
    var eur = new Intl.NumberFormat('fr-FR', { style: 'currency', currency: 'EUR', maximumFractionDigits: 0 });
    var eur2 = new Intl.NumberFormat('fr-FR', { style: 'currency', currency: 'EUR', minimumFractionDigits: 2, maximumFractionDigits: 2 });
    function n(id) { var v = parseFloat(String(document.getElementById(id).value).replace(',', '.')); return isFinite(v) && v > 0 ? v : 0; }
    function calc() {
      var PREV = n('s-prev') / 100; var nc = Math.round(n('s-nc')), c = Math.round(n('s-c')), salNc = n('s-salnc'), salC = n('s-salc'), mut = n('s-mut');
      var part = Math.max(0.5, Math.min(n('s-part'), 100) / 100);
      var effectif = nc + c;
      var mutEmp = effectif * mut * part;
      var prevEmp = (nc * Math.min(salNc, PASS_M) + c * Math.min(salC, PASS_M)) * PREV * 0.5;
      var prevCEmp = c * Math.min(salC, PASS_M) * CAD;
      var base = mutEmp + prevEmp + prevCEmp;
      var fs = effectif >= 11 ? base * FS : 0;
      var mois = base + fs;
      document.getElementById('o-mois').textContent = eur.format(mois);
      document.getElementById('o-an').textContent = eur.format(mois * 12);
      document.getElementById('o-sal').textContent = eur2.format(mut * (1 - part) + Math.min(salNc, PASS_M) * PREV * 0.5);
      document.getElementById('o-detail').textContent = 'Dont mutuelle ' + eur.format(mutEmp) + ', prévoyance de branche ' + eur.format(prevEmp) +
        ', prévoyance cadres ' + eur.format(prevCEmp) + (fs ? ', forfait social ' + eur.format(fs) : ', pas de forfait social sous 11 salariés') + ' par mois.';
    }
    sim.addEventListener('input', calc); calc();
  }

  /* Check-up conformité */
  var chk = document.getElementById('checkup');
  if (chk) {
    function score() {
      var items = chk.querySelectorAll('.check-item'), answered = 0, issues = [];
      items.forEach(function (it) {
        var sel = it.querySelector('input:checked');
        if (sel) { answered++; if (sel.value === 'non') issues.push(it.dataset.fix); }
      });
      var out = document.getElementById('checkup-result');
      if (!answered) { out.hidden = true; return; }
      out.hidden = false;
      var title = out.querySelector('strong'), list = out.querySelector('ul'), p = out.querySelector('p');
      list.innerHTML = '';
      if (!issues.length) {
        title.textContent = answered === items.length ? 'Tout est en ordre. Bravo.' : 'Rien à signaler pour l\'instant.';
        p.textContent = answered === items.length ? 'Pensez à remettre votre contrat en concurrence tous les deux ou trois ans : à garanties égales, les écarts de prix sont fréquents.' : 'Répondez aux questions restantes pour un bilan complet.';
      } else {
        title.textContent = issues.length + (issues.length > 1 ? ' points à corriger' : ' point à corriger');
        p.textContent = 'Ce sont les écarts que l\'URSSAF ou un sinistre font apparaître. Nous pouvons les régler avec vous, gratuitement et sans engagement.';
        issues.forEach(function (t) { var li = document.createElement('li'); li.textContent = t; list.appendChild(li); });
      }
    }
    chk.addEventListener('change', score);
  }
})();
