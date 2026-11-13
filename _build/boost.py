# -*- coding: utf-8 -*-
"""boost : couche commune à tous les sites satellites, appliquée à la fin de build.py.

Elle retravaille le site généré (dossier de sortie) sans toucher au moteur :
  - conversion : formulaire en 2 étapes, barre d'appel sur mobile, réassurance, appel à l'étude dans les articles,
    cas clients (uniquement s'ils sont renseignés dans boost_cfg.py) ;
  - référencement Google et IA : titre d'accueil, H1 porteur du mot-clé, fil d'Ariane et auteur en données
    structurées, encadré « En bref », page « Qui sommes-nous », llms.txt, robots.txt ouvert aux robots d'IA ;
  - visuel v2 (THEME = "v2") : typographie, cartes, en-tête clair ; les couleurs partent de celles du site.
Réglages par site : _build/boost_cfg.py. Ne rien écrire d'inventé dans CASES : uniquement des cas réels validés.
"""
import os, re, json, glob, hashlib, shutil, html as _html

HERE = os.path.dirname(os.path.abspath(__file__))
BX = os.path.join(HERE, "boost")
import boost_cfg as CFG

WWC = "https://www.wealthwiseconseil.fr"
AUTHOR = {"@type": "Person", "name": "Nicolas Ferran", "jobTitle": "Courtier en assurance, fondateur de WealthWise Conseil",
          "worksFor": {"@type": "Organization", "name": "WealthWise Conseil", "url": WWC + "/"}, "url": WWC + "/"}
AI_BOTS = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-SearchBot", "Claude-User", "PerplexityBot", "Perplexity-User",
           "Google-Extended", "Applebot-Extended", "MistralAI-User", "CCBot", "meta-externalagent", "Amazonbot", "DuckAssistBot"]


def _hex(c):
    c = c.strip().lstrip("#")
    if len(c) == 3: c = "".join(x * 2 for x in c)
    return tuple(int(c[i:i + 2], 16) for i in (0, 2, 4))


def _lum(rgb):
    f = lambda v: (v / 255 / 12.92) if v / 255 <= .03928 else ((v / 255 + .055) / 1.055) ** 2.4
    r, g, b = map(f, rgb)
    return .2126 * r + .7152 * g + .0722 * b


def _contrast_white(rgb):
    return 1.05 / (_lum(rgb) + .05)


def _mix(a, b, t):
    return tuple(round(a[i] * (1 - t) + b[i] * t) for i in range(3))


def _tohex(rgb):
    return "#%02X%02X%02X" % rgb


def _darken_to(rgb, target=4.6):
    n = 0
    while _contrast_white(rgb) < target and n < 40:
        rgb = _mix(rgb, (0, 0, 0), .06); n += 1
    return rgb


def tokens(css):
    """Couleurs v2 calculées à partir de la palette d'origine du site (les logos et images restent cohérents)."""
    root = re.search(r":root\{(.*?)\}", css, re.S).group(1)
    v = dict(re.findall(r"--([\w-]+):\s*(#[0-9A-Fa-f]{3,6})", root))
    g = lambda k, d: _hex(v.get(k, d))
    navy, teal, red, cream = g("navy", "#1D2250"), g("teal", "#11A39B"), g("red", "#D62E2F"), g("cream", "#FFF3DC")
    if _lum(navy) > .12: navy = _darken_to(navy, 11)
    t = {"navy": _tohex(navy), "ink": _tohex(_mix(navy, (0, 0, 0), .25)), "teal": _tohex(_darken_to(teal, 4.8)),
         "red": _tohex(_darken_to(red, 4.6)), "red-d": _tohex(_darken_to(_mix(red, (0, 0, 0), .15), 4.6)),
         "cream": _tohex(_mix(cream, (255, 255, 255), .78)), "cream-2": _tohex(_mix(cream, (255, 255, 255), .30)),
         "line": _tohex(_mix(_mix(cream, navy, .16), (255, 255, 255), .25)), "muted": _tohex(_mix(navy, (255, 255, 255), .30)),
         "white": "#FFFFFF", "ok": "#1F7A55"}
    if "mustard" in v: t["mustard"] = v["mustard"]
    t.update(getattr(CFG, "TOKENS", {}))
    return t


def _hash(s):
    return hashlib.md5(s.encode()).hexdigest()[:8]


def _txt(s):
    return re.sub(r"\s+", " ", _html.unescape(re.sub(r"<[^>]+>", " ", s))).strip()


# ------------------------------------------------------------------ formulaire en 2 étapes
def step_form(m):
    t = m.group(0)
    form_open = re.search(r"<form class=\"lead-form\"[^>]*>", t).group(0)
    inner = t[t.index(form_open) + len(form_open): t.index("</form>")]
    names_before = set(re.findall(r'name="([\w-]+)"', inner))
    honey = re.search(r'<input type="text" name="website"[^>]*>', inner)
    fieldsets = re.findall(r"<fieldset>.*?</fieldset>", inner, re.S)
    fields = re.findall(r'<div class="field">.*?</div>', inner, re.S)
    by = {}
    for f in fields:
        n = re.search(r'name="([\w-]+)"', f)
        by[n.group(1) if n else f] = f
    consent = re.search(r'<label class="consent".*?</label>', inner, re.S)
    fine = re.search(r'<p class="fine">.*?</p>', inner, re.S)
    submit = re.search(r'<button type="submit"[^>]*>.*?</button>', inner, re.S)
    if not (submit and "nom" in by and "email" in by):
        return t
    s1 = "".join(fieldsets) + by.pop("salaries", "")
    ident = [by.pop(k) for k in ("nom", "etablissement", "tel", "email") if k in by]
    rows = "".join(f'<div class="row2">{"".join(ident[i:i + 2])}</div>' for i in range(0, len(ident), 2))
    rest = list(by.values())
    more = ""
    if rest:
        rr = "".join(f'<div class="row2">{"".join(rest[i:i + 2])}</div>' if len(rest[i:i + 2]) == 2 else rest[i] for i in range(0, len(rest), 2))
        more = f'<details class="bx-more"><summary>Ajouter des précisions (facultatif) : contrat en place, échéance…</summary><div class="bx-more-in">{rr}</div></details>'
    new = f"""{form_open}
    {honey.group(0) if honey else ''}
    <div class="bx-steps" aria-hidden="true"><span>Étape 1 sur 2</span><div class="bx-bar"><i></i></div></div>
    <div class="bx-step" data-s="1">
      {s1}
      <button type="button" class="btn btn-red bx-next">Continuer</button>
      <ul class="bx-assure"><li>Gratuit</li><li>Sans engagement</li><li>Réponse sous 24 h ouvrées</li></ul>
    </div>
    <div class="bx-step" data-s="2">
      <p class="bx-step2-title">À qui envoyer l'étude ?</p>
      {rows}
      {more}
      {consent.group(0) if consent else ''}
      <div class="form-msg" role="alert" hidden></div>
      {submit.group(0)}
      <button type="button" class="bx-back">Revenir à l'étape 1</button>
      {fine.group(0) if fine else ''}
    </div>
  </form>"""
    missing = names_before - set(re.findall(r'name="([\w-]+)"', new))
    assert not missing, f"champs perdus dans le formulaire : {missing}"
    return t[:t.index(form_open)] + new + t[t.index("</form>") + 7:]


TICKET_RE = re.compile(r'<div class="ticket">.*?</form>', re.S)


# ------------------------------------------------------------------ blocs
def cases_block():
    cases = getattr(CFG, "CASES", [])
    if not cases:
        return ""
    cards = "".join(f'<article class="bx-case"><span class="who">{c["qui"]}</span><strong class="res">{c["resultat"]}</strong><p>{c["detail"]}</p></article>' for c in cases)
    return f"""<section class="band bg-cream2" id="cas-clients">
  <div class="wrap"><div class="sec-head"><span class="t-label">Cas clients</span><h2>Ce que nous avons obtenu pour des entreprises comme la vôtre</h2><p>Dossiers réels du cabinet, anonymisés à la demande des clients.</p></div>
  <div class="bx-cases">{cards}</div></div>
</section>
"""


def about_main(href):
    b, pub, conv = CFG.BRAND, CFG.PUBLIC, CFG.CONVENTION
    return f"""<main id="contenu">
<section class="page-hero bg-cream">
  <div class="wrap" style="grid-template-columns:minmax(0,1fr)">
    <div>
      <span class="crumb"><a href="{href('index')}">Accueil</a> · Qui sommes-nous</span>
      <h1 class="kw-h1">Qui est derrière {b} ?</h1>
      <p class="lead">{b} est la marque de WealthWise Conseil dédiée à la mutuelle et à la prévoyance {pub}. Derrière le site, un cabinet de courtage immatriculé et un conseiller que vous pouvez appeler.</p>
    </div>
  </div>
</section>
<section class="band bg-cream" style="padding-top:36px">
  <div class="wrap narrow prose bx-about">
    <h2>Le cabinet</h2>
    <p>WealthWise Conseil est un cabinet de courtage en assurance indépendant, fondé et dirigé par Nicolas Ferran. Le cabinet est spécialisé dans la protection sociale des entreprises : mutuelle d'entreprise, prévoyance des salariés et protection du dirigeant. {b} en est la marque spécialisée pour {conv}.</p>
    <ul class="bx-facts">
      <li><span>Immatriculation ORIAS</span><strong>n° 24000251, vérifiable sur <a href="https://www.orias.fr/" rel="noopener">orias.fr</a></strong></li>
      <li><span>Statut</span><strong>Courtier en assurance (catégorie « b »)</strong></li>
      <li><span>Société</span><strong>WealthWise Conseil, SASU, RCS Nanterre 980 572 671</strong></li>
      <li><span>Contrôle</span><strong>ACPR, 4 place de Budapest, 75436 Paris Cedex 09</strong></li>
      <li><span>Téléphone</span><strong><a href="tel:+33187667031">01 87 66 70 31</a></strong></li>
      <li><span>E-mail</span><strong><a href="mailto:contact@wealthwiseconseil.fr">contact@wealthwiseconseil.fr</a></strong></li>
    </ul>
    <h2>Comment nous travaillons</h2>
    <p>Un courtier ne vend pas le contrat d'un seul assureur : il compare. Pour chaque entreprise, nous partons de la convention collective applicable et de la réalité de l'équipe (effectif, cadres, temps partiels, contrats courts), puis nous mettons plusieurs assureurs en concurrence sur le même cahier des charges. Vous recevez un comparatif lisible, avec ce qui est obligatoire, ce qui est négociable et ce que nous recommandons.</p>
    <p>Une fois le contrat choisi, nous préparons les documents que l'employeur doit conserver (décision unilatérale, notices, dispenses d'affiliation) et nous restons l'interlocuteur de l'entreprise et des salariés pendant toute la vie du contrat.</p>
    <h2>Comment nous sommes rémunérés</h2>
    <p>L'étude et le comparatif sont gratuits et sans engagement. Si vous souscrivez un contrat par notre intermédiaire, le cabinet est rémunéré par une commission incluse dans la cotisation d'assurance et versée par l'assureur. Vous ne recevez aucune facture d'honoraires pour l'étude.</p>
    <h2>Qui écrit les guides du site ?</h2>
    <p>Les pages et les articles sont rédigés et relus par Nicolas Ferran, à partir des textes de la convention collective, des accords de branche et des barèmes officiels de l'année. Chaque article porte sa date de mise à jour. Une information vous semble dépassée ? Écrivez-nous, nous corrigeons.</p>
    <p><a class="btn btn-red" href="{href('devis')}">Demander une étude gratuite</a></p>
  </div>
</section>
</main>
"""



QUIZ = [
    ("Tous vos salariés ont-ils la mutuelle de l'entreprise, ou une dispense écrite et signée ?",
     "Affiliations et dispenses", "Chaque salarié doit être affilié ou avoir signé une dispense prévue par les textes. Une dispense orale ne vaut rien en cas de contrôle URSSAF.", 0),
    ("Avez-vous un écrit qui met en place le régime (décision de l'employeur ou accord), remis à chaque salarié ?",
     "L'acte de mise en place", "Sans cet écrit remis contre signature, les exonérations de charges sur la part employeur peuvent être remises en cause.", 0),
    ("Vos cadres ont-ils une prévoyance d'au moins 1,50 % de la tranche A, payée par l'employeur ?",
     "La prévoyance des cadres", "C'est une obligation nationale. Si elle manque, l'employeur peut devoir verser lui-même un capital de trois plafonds annuels de la Sécurité sociale en cas de décès.", 1),
    ("Votre contrat a-t-il été comparé à d'autres assureurs depuis moins de trois ans ?",
     "Le prix et les garanties", "Les tarifs et les obligations de branche évoluent chaque année. Un contrat jamais remis en concurrence est souvent plus cher ou en retard sur la convention.", 0),
]


def quiz_block():
    lis = "".join(f'<li data-t="{_html.escape(t)}" data-x="{_html.escape(x)}" data-na="{na}"><strong>{q}</strong><span>{x}</span></li>' for q, t, x, na in QUIZ)
    return f"""<section class="band bg-cream2 bx-quiz-band" id="diagnostic">
  <div class="wrap">
    <div class="sec-head"><span class="t-label">Diagnostic express</span><h2>Votre entreprise est-elle en règle ? 4 questions, 30 secondes</h2><p>Répondez sans rien saisir : vous voyez tout de suite les points à vérifier dans votre mutuelle et votre prévoyance.</p></div>
    <div class="bx-quiz" data-quiz><ol class="bx-quiz-list">{lis}</ol></div>
  </div>
</section>
"""


def _slug(t):
    import unicodedata
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")[:60] or "partie"


def html2md(h, base):
    """Texte propre d'une page (pour llms-full.txt)."""
    m = re.search(r"<main[^>]*>(.*?)</main>", h, re.S)
    b = m.group(1) if m else h
    b = re.sub(r"<(script|style|svg|form|nav|noscript|button|select|figure)\b.*?</\1>", "", b, flags=re.S)
    b = re.sub(r'<div class="(ticket|lead-done|bx-inline|bx-sticky|bx-quiz)".*?</div>\s*</div>', "", b, flags=re.S)
    def link(m):
        u, t = m.group(1), _txt(m.group(2))
        if not t: return ""
        if u.startswith("/"): u = base + u
        return f"[{t}]({u})" if u.startswith("http") else t
    b = re.sub(r'<a [^>]*href="([^"]*)"[^>]*>(.*?)</a>', link, b, flags=re.S)
    def row(m):
        cells = [_txt(c) for c in re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", m.group(1), re.S)]
        return "| " + " | ".join(cells) + " |\n"
    b = re.sub(r"<tr[^>]*>(.*?)</tr>", row, b, flags=re.S)
    for tag, pre in (("h1", "# "), ("h2", "## "), ("h3", "### "), ("summary", "### ")):
        b = re.sub(rf"<{tag}[^>]*>(.*?)</{tag}>", lambda m, pre=pre: f"\n\n{pre}{_txt(m.group(1))}\n\n", b, flags=re.S)
    b = re.sub(r"<li[^>]*>(.*?)</li>", lambda m: f"\n- {_txt(m.group(1))}", b, flags=re.S)
    b = re.sub(r"<(strong|b)>(.*?)</\1>", lambda m: f"**{_txt(m.group(2))}**", b, flags=re.S)
    b = re.sub(r"</(p|div|section|ul|ol|table|blockquote|details)>", "\n\n", b)
    b = re.sub(r"<br\s*/?>", "\n", b)
    b = _html.unescape(re.sub(r"<[^>]+>", "", b))
    b = "\n".join(l.strip() for l in b.split("\n"))
    return re.sub(r"\n{3,}", "\n\n", b).strip()


# ------------------------------------------------------------------ traitement d'une page
def process(path, slug, mode, versions):
    h = open(path, encoding="utf-8").read()
    depth = slug.count("/")
    pre = "../" * depth if mode == "preview" else "/"
    href = (lambda s: f"{pre}{s}.html") if mode == "preview" else (lambda s: "/" if s == "index" else f"/{s}")
    is_art = slug.startswith("blog/")
    title = _html.unescape(re.search(r"<title>(.*?)</title>", h, re.S).group(1))
    desc_m = re.search(r'<meta name="description" content="(.*?)">', h)
    desc = desc_m.group(1) if desc_m else ""

    # titre d'accueil : mot-clé d'abord
    if slug == "index" and getattr(CFG, "HOME_TITLE", ""):
        old = re.search(r"<title>(.*?)</title>", h, re.S).group(1)
        h = h.replace(old, _html.escape(CFG.HOME_TITLE, quote=True)); title = CFG.HOME_TITLE
        if getattr(CFG, "HOME_DESC", ""):
            h = h.replace(desc, _html.escape(CFG.HOME_DESC, quote=True)); desc = _html.escape(CFG.HOME_DESC, quote=True)

    if slug == "index" and getattr(CFG, "HOME_H1", ""):
        h = re.sub(r'(<span class="l1">)(.*?)(</span>)', lambda m: m.group(1) + CFG.HOME_H1 + m.group(3), h, count=1, flags=re.S)

    # feuilles de style, scripts, polices
    h = re.sub(r"(assets/style\.css)\?v=\w+", r"\1?v=" + versions["css"], h)
    h = re.sub(r"(assets/main\.js)\?v=\w+", r"\1?v=" + versions["js"], h)
    h = h.replace('<script src="https://cdn.jsdelivr.net/npm/@emailjs', '<script defer src="https://cdn.jsdelivr.net/npm/@emailjs')
    h = re.sub(r'<script src="([^"]*assets/main\.js[^"]*)">', r'<script defer src="\1">', h)
    h = h.replace("<script>CONFIG.preview = true;</script>", "<script>window.__bxPreview=true;</script>")
    if CFG.THEME == "v2":
        h = re.sub(r'<link rel="preconnect" href="https://fonts\.(googleapis|gstatic)\.com"[^>]*>\n?', "", h)
        h = re.sub(r'<link rel="stylesheet" href="https://fonts\.googleapis\.com[^>]*>\n?', "", h)
        a = ("../" * depth + "assets/") if mode == "preview" else "/assets/"
        pl = "".join(f'<link rel="preload" href="{a}fonts/{f}" as="font" type="font/woff2" crossorigin>\n' for f in
                     ("bricolage-grotesque-latin-wght-normal.woff2", "instrument-sans-latin-wght-normal.woff2"))
        h = h.replace('<link rel="stylesheet" href="', pl + '<link rel="stylesheet" href="', 1)
        h = re.sub(r'(<span class="l2[^"]*">)(.*?)(</span>)', lambda m: m.group(1) + re.sub(r"<br\s*/?>", " ", m.group(2)) + m.group(3), h, count=1, flags=re.S)
        def poster(m):
            ill = re.search(r'<svg class="ill".*?</svg>', m.group(2), re.S)
            go = re.search(r'<span class="go"[^>]*>(.*?)</span>', m.group(2), re.S)
            head = re.search(r'<div class="p-head">(.*?)</div>', m.group(2), re.S)
            if not (go and head): return m.group(0)
            parts = [_txt(x) for x in re.findall(r'<span class="(?:s|b|sc|c)\b[^"]*"[^>]*>(.*?)</span>', head.group(1), re.S)]
            label = re.sub(r"\s*→\s*$", "", _txt(go.group(1)))
            return (f'<a class="poster" href="{m.group(1)}">{ill.group(0) if ill else ""}<div class="p-head"><span class="b">{_html.escape(label, quote=False)}</span>'
                    f'<span class="sc">{_html.escape(" ".join(parts), quote=False)}</span></div><span class="go">Voir la page</span></a>')
        h = re.sub(r'<a class="poster[^"]*" href="([^"]*)">(.*?)</a>', poster, h, flags=re.S)
        h = re.sub(r'<meta name="theme-color" content="[^"]*">', f'<meta name="theme-color" content="{versions["navy"]}">', h)

    # H1 porteur du mot-clé sur les pages intérieures ; l'ancien titre devient le slogan
    if not is_art and slug not in ("index", "mentions-legales", "a-propos"):
        m = re.search(r'<h1([^>]*)>(.*?)</h1>\s*<p class="sub"([^>]*)>(.*?)</p>', h, re.S)
        if m and "art-h1" not in m.group(1):
            kw = _html.escape(re.sub(r"\s*·\s*[^·]+$", "", title), quote=False)
            slogan = (re.sub(r"<br\s*/?>", " ", m.group(2)).strip() + " " + m.group(4).strip()).strip()
            h = h.replace(m.group(0), f'<h1 class="kw-h1">{kw}</h1>\n      <p class="sub slogan"{m.group(3)}>{slogan}</p>', 1)

    # formulaires en 2 étapes ; le premier de la page porte l'ancre #etude
    h = TICKET_RE.sub(step_form, h)
    has_form = '<div class="ticket">' in h
    if has_form:
        h = h.replace('<div class="ticket">', '<div class="ticket" id="etude">', 1)
    target = "#etude" if has_form else href("devis")

    # accueil : ligne ORIAS sous les preuves, cas clients avant les assureurs
    if slug == "index":
        line = f'<p class="bx-orias">Cabinet WealthWise Conseil, courtier immatriculé à l\'ORIAS sous le n° 24000251. <a href="{href("a-propos")}">Qui sommes-nous ?</a></p>'
        if '<ul class="hero-proofs">' in h:
            i = h.index("</ul>", h.index('<ul class="hero-proofs">')) + 5
            h = h[:i] + "\n      " + line + h[i:]
        mi = h.index("<main")
        ends = [x.end() for x in re.finditer(r"</section>", h[mi:])]
        if len(ends) >= 2 and 'id="diagnostic"' not in h:
            k = mi + ends[1]
            h = h[:k] + "\n" + quiz_block() + h[k:]
        cb = cases_block()
        if cb:
            i = h.rfind('<section class="cta-band')
            if i > 0: h = h[:i] + cb + h[i:]

    # articles : auteur, encadré « En bref », appel à l'étude au milieu du texte
    if is_art:
        h = h.replace("· Par WealthWise Conseil</p>", f'· Par <a href="{href("a-propos")}" style="color:inherit">Nicolas Ferran</a>, courtier en assurance</p>')
        mk = '<div class="wrap narrow prose article">'
        if mk in h:
            dm = re.search(r'"dateModified":\s*"([\d-]+)"', h)
            maj = ""
            if dm:
                y, mo, d = dm.group(1).split("-")
                mois = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"][int(mo) - 1]
                maj = f"Mis à jour le {int(d)}{'er' if int(d) == 1 else ''} {mois} {y}. "
            brief = f'\n    <div class="bx-brief"><strong>En bref</strong><p>{desc}</p><small>{maj}Vérifié par Nicolas Ferran, courtier en assurance (ORIAS 24000251).</small></div>'
            i = h.index(mk) + len(mk)
            j = h.index('<div class="author-box">', i) if '<div class="author-box">' in h[i:] else len(h)
            body = h[i:j]
            heads = []
            def hid(m):
                t = _txt(m.group(2)); i_ = _slug(t)
                while i_ in [x[0] for x in heads]: i_ += "-2"
                heads.append((i_, t))
                return f'<h2 id="{i_}"{m.group(1)}>{m.group(2)}</h2>'
            body = re.sub(r"<h2(?![^>]*\bid=)([^>]*)>(.*?)</h2>", hid, body, flags=re.S)
            if len(heads) >= 3:
                brief += ('\n    <nav class="bx-toc" aria-label="Sommaire"><strong>Dans cet article</strong><ol>' +
                          "".join(f'<li><a href="#{i_}">{_html.escape(t, quote=False)}</a></li>' for i_, t in heads) + "</ol></nav>")
            pos = [x.start() for x in re.finditer(r"<h2", body)]
            if len(pos) >= 3:
                cta = (f'<div class="bx-inline"><p>Votre contrat couvre-t-il ce cas ?<small>Un conseiller le vérifie gratuitement et vous répond sous 24 h ouvrées.</small></p>'
                       f'<a class="btn" href="#etude">Faire vérifier mon contrat</a></div>\n    ')
                body = body[:pos[2]] + cta + body[pos[2]:]
            h = h[:i] + brief + body + h[j:]

    # données structurées
    def fix_ld(m):
        try:
            d = json.loads(m.group(1))
        except Exception:
            return m.group(0)
        nodes = d.get("@graph", [d])
        for n in nodes:
            if n.get("@type") == "BlogPosting":
                n["author"] = AUTHOR; n["inLanguage"] = "fr-FR"
                n["isPartOf"] = {"@type": "Blog", "url": CFG.DOMAIN + "/blog"}
            if n.get("@type") == "InsuranceAgency":
                n.setdefault("identifier", {"@type": "PropertyValue", "propertyID": "ORIAS", "value": "24000251"})
                n.setdefault("founder", AUTHOR); n.setdefault("areaServed", {"@type": "Country", "name": "France"})
                n.setdefault("knowsAbout", ["mutuelle d'entreprise", "prévoyance collective", "protection sociale du dirigeant", CFG.CONVENTION])
        return '<script type="application/ld+json">' + json.dumps(d, ensure_ascii=False) + "</script>"
    h = re.sub(r'<script type="application/ld\+json">(.*?)</script>', fix_ld, h, count=1, flags=re.S)
    extra = []
    if slug == "index":
        extra.append({"@context": "https://schema.org", "@type": "WebSite", "name": CFG.BRAND, "url": CFG.DOMAIN + "/", "inLanguage": "fr-FR",
                      "publisher": {"@type": "Organization", "name": "WealthWise Conseil", "url": WWC + "/"}})
    else:
        crumbs = [("Accueil", CFG.DOMAIN + "/")]
        if is_art: crumbs.append(("Blog", CFG.DOMAIN + "/blog"))
        crumbs.append((re.sub(r"\s*·\s*[^·]+$", "", title), CFG.DOMAIN + "/" + slug))
        extra.append({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(crumbs)]})
    h = h.replace("</head>", "".join('<script type="application/ld+json">' + json.dumps(e, ensure_ascii=False) + "</script>\n" for e in extra) + "</head>", 1)

    # pied de page : lien « Qui sommes-nous » ; barre d'appel sur mobile
    ml = re.search(r'<li><a href="([^"]*mentions-legales[^"]*)">', h)
    if ml and "Qui sommes-nous</a></li>" not in h:
        h = h.replace(ml.group(0), f'<li><a href="{href("a-propos")}">Qui sommes-nous</a></li>' + ml.group(0), 1)
    if is_art:
        h = h.replace("<header", '<div class="bx-progress" aria-hidden="true"><i></i></div>\n<header', 1)
    if slug != "mentions-legales":
        bar = (f'<div class="bx-sticky"><a class="call" href="tel:+33187667031" aria-label="Appeler le 01 87 66 70 31">Appeler</a>'
               f'<a class="go" href="{target}">Étude gratuite en 2 minutes</a></div>\n')
        h = h.replace("<footer", bar + "<footer", 1)
    open(path, "w", encoding="utf-8").write(h)
    return title, _html.unescape(desc)


def run(out, mode):
    # 1. feuille de style et script
    css_p, js_p = os.path.join(out, "assets", "style.css"), os.path.join(out, "assets", "main.js")
    css = open(css_p, encoding="utf-8").read()
    navy = "#1D2250"
    if CFG.THEME == "v2":
        tk = tokens(css); navy = tk["navy"]
        v2 = open(os.path.join(BX, "v2.css"), encoding="utf-8").read().replace("/*TOKENS*/", " ".join(f"--{k}:{v};" for k, v in tk.items()))
        css += v2
        os.makedirs(os.path.join(out, "assets", "fonts"), exist_ok=True)
        for f in glob.glob(os.path.join(BX, "fonts", "*.woff2")):
            shutil.copy(f, os.path.join(out, "assets", "fonts"))
    css += open(os.path.join(BX, "comp.css"), encoding="utf-8").read() + getattr(CFG, "EXTRA_CSS", "")
    open(css_p, "w", encoding="utf-8").write(css)
    js = open(js_p, encoding="utf-8").read() + open(os.path.join(BX, "boost.js"), encoding="utf-8").read()
    js = js.replace("preview: false,", "preview: !!window.__bxPreview,", 1) if "preview: false," in js else js
    open(js_p, "w", encoding="utf-8").write(js)
    versions = {"css": _hash(css), "js": _hash(js), "navy": navy}

    # 2. page « Qui sommes-nous », bâtie sur l'en-tête et le pied de l'accueil
    idx = open(os.path.join(out, "index.html"), encoding="utf-8").read()
    t0 = re.search(r"<title>(.*?)</title>", idx, re.S).group(1)
    d0 = re.search(r'<meta name="description" content="(.*?)">', idx).group(1)
    ab_t = f"Qui sommes-nous : le cabinet derrière {CFG.BRAND} · {CFG.BRAND}"
    ab_d = f"{CFG.BRAND} est une marque de WealthWise Conseil, courtier en assurance immatriculé à l'ORIAS (n° 24000251). Le cabinet, la méthode, la rémunération."
    hd, ft = idx[:idx.index("<main")], idx[idx.index("</main>") + 7:]
    hd = hd.replace(t0, _html.escape(ab_t, quote=True)).replace(d0, _html.escape(ab_d, quote=True))
    hd = hd.replace(f'<link rel="canonical" href="{CFG.DOMAIN}/">', f'<link rel="canonical" href="{CFG.DOMAIN}/a-propos">')
    hd = hd.replace(f'<meta property="og:url" content="{CFG.DOMAIN}/">', f'<meta property="og:url" content="{CFG.DOMAIN}/a-propos">')
    ld = {"@context": "https://schema.org", "@type": "AboutPage", "name": ab_t, "url": CFG.DOMAIN + "/a-propos", "inLanguage": "fr-FR",
          "about": {"@type": "InsuranceAgency", "name": CFG.BRAND, "url": CFG.DOMAIN + "/", "telephone": "+33187667031",
                    "identifier": {"@type": "PropertyValue", "propertyID": "ORIAS", "value": "24000251"}, "founder": AUTHOR,
                    "parentOrganization": {"@type": "Organization", "name": "WealthWise Conseil", "url": WWC + "/"}}}
    hd = re.sub(r'<script type="application/ld\+json">.*?</script>', lambda m: '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + "</script>", hd, count=1, flags=re.S)
    hd = hd.replace(' aria-current="page"', "")
    href0 = (lambda s: f"{s}.html") if mode == "preview" else (lambda s: "/" if s == "index" else f"/{s}")
    open(os.path.join(out, "a-propos.html"), "w", encoding="utf-8").write(hd + about_main(href0) + ft)

    # 3. toutes les pages
    pages = []
    for p in sorted(glob.glob(os.path.join(out, "**", "*.html"), recursive=True)):
        slug = os.path.relpath(p, out)[:-5].replace(os.sep, "/")
        pages.append((slug,) + process(p, slug, mode, versions))

    if mode != "deploy":
        return
    # 4. robots.txt ouvert aux robots d'IA, plan du site, llms.txt
    robots = "User-agent: *\nAllow: /\n\n# Robots des assistants d'IA : bienvenue, le contenu peut être lu et cité.\n"
    robots += "".join(f"User-agent: {b}\nAllow: /\n\n" for b in AI_BOTS) + f"Sitemap: {CFG.DOMAIN}/sitemap.xml\n"
    open(os.path.join(out, "robots.txt"), "w").write(robots)
    sm_p = os.path.join(out, "sitemap.xml")
    if os.path.exists(sm_p):
        sm = open(sm_p).read()
        if "/a-propos<" not in sm:
            lm = (re.findall(r"<lastmod>([\d-]+)</lastmod>", sm) or ["2026-11-13"])[0]
            sm = sm.replace("</urlset>", f"  <url><loc>{CFG.DOMAIN}/a-propos</loc><lastmod>{max(lm, '2026-11-13')}</lastmod></url>\n</urlset>")
            open(sm_p, "w").write(sm)
    url = lambda s: CFG.DOMAIN + ("/" if s == "index" else "/" + s)
    clean = lambda t: re.sub(r"\s*·\s*[^·]+$", "", t)
    fixed = [p for p in pages if not p[0].startswith("blog/") and p[0] not in ("mentions-legales", "index", "blog", "devis")]
    arts = [p for p in pages if p[0].startswith("blog/")]
    home = next(p for p in pages if p[0] == "index")
    faq = []
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', open(os.path.join(out, "index.html"), encoding="utf-8").read(), re.S)
    try:
        for n in json.loads(m.group(1)).get("@graph", []):
            if n.get("@type") == "FAQPage":
                faq = [(q["name"], _txt(q["acceptedAnswer"]["text"])) for q in n["mainEntity"]]
    except Exception:
        pass
    L = [f"# {CFG.BRAND}", "", f"> {home[2]}", "",
         f"{CFG.BRAND} est la marque de WealthWise Conseil consacrée à la mutuelle d'entreprise et à la prévoyance {CFG.PUBLIC} ({CFG.CONVENTION}). "
         "WealthWise Conseil est un cabinet de courtage en assurance indépendant, immatriculé à l'ORIAS sous le n° 24000251, fondé par Nicolas Ferran. "
         "Le cabinet compare plus de 15 assureurs ; l'étude est gratuite et sans engagement, la rémunération est une commission versée par l'assureur.", "",
         "Contact : 01 87 66 70 31, contact@wealthwiseconseil.fr. Demande d'étude : " + url("devis"), "",
         "Les contenus peuvent être cités avec un lien vers la page d'origine. Les chiffres sont ceux de l'année indiquée dans chaque page.", "",
         "## Pages principales", ""]
    L += [f"- [{clean(t)}]({url(s)}) : {d}" for s, t, d in fixed]
    if faq:
        L += ["", "## Questions fréquentes", ""]
        for q, a in faq:
            L += [f"### {q}", "", a, ""]
    if arts:
        L += ["", "## Guides et articles", ""] + [f"- [{clean(t)}]({url(s)}) : {d}" for s, t, d in arts]
    L += ["", "## Le cabinet", "", f"- [Qui sommes-nous]({url('a-propos')})", f"- [WealthWise Conseil]({WWC}/) : site du cabinet", ""]
    L += ["## Contenu complet", "", f"- [Tout le contenu du site en un seul fichier texte]({CFG.DOMAIN}/llms-full.txt)", ""]
    open(os.path.join(out, "llms.txt"), "w", encoding="utf-8").write("\n".join(L))
    full = [f"# {CFG.BRAND} : contenu complet", "", f"Source : {CFG.DOMAIN}/ (marque de WealthWise Conseil, courtier en assurance, ORIAS 24000251). Auteur : Nicolas Ferran.", ""]
    for sl, t, d in [home] + fixed + arts:
        md = html2md(open(os.path.join(out, sl + ".html"), encoding="utf-8").read(), CFG.DOMAIN)
        full += ["", "---", "", f"Page : {url(sl)}", "", md, ""]
    open(os.path.join(out, "llms-full.txt"), "w", encoding="utf-8").write("\n".join(full))
    print("boost OK :", len(pages), "pages, llms.txt, robots.txt")
