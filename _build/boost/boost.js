
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
