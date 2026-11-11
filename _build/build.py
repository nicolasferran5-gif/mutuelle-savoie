#!/usr/bin/env python3
"""Moteur commun des sites satellites de WealthWise Conseil.
   Le contenu propre au site est dans site.py (identité, textes communs) et pages.py (pages).
   python3 build.py deploy OUT  -> dossier prêt pour Vercel (liens propres)
   python3 build.py preview OUT -> aperçu (liens .html, formulaires en mode démo)"""
import os, sys, shutil, json, re
from logo import mark_svg, pastille_svg, favicon_svg, mark_inner
from articles import ARTICLES, AUTHOR, WWC

MODE = sys.argv[1] if len(sys.argv) > 1 else "deploy"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[2] if len(sys.argv) > 2 else "/tmp/site-satellite"  # dossier de sortie (jamais le dépôt lui-même)
REPO_LOGOS = os.path.join(HERE, "assureurs")

def asset_v(name):
    import hashlib
    return hashlib.md5(open(os.path.join(HERE, name), "rb").read()).hexdigest()[:8]


PREFIX = ""  # "../" pour les pages du dossier blog/ en mode aperçu


def L(slug):
    """Lien interne selon le mode."""
    if slug in ("", "index"):
        return "/" if MODE == "deploy" else PREFIX + "index.html"
    return f"/{slug}" if MODE == "deploy" else f"{PREFIX}{slug}.html"


def A(path):
    return f"/{path}" if MODE == "deploy" else PREFIX + path


exec(open(os.path.join(HERE, "site.py"), encoding="utf-8").read())  # identité et textes du site


SPRITE = f"""<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false"><defs>
<symbol id="i-star" viewBox="0 0 20 20"><path d="M10 0l2.6 7.4H20l-6 4.6 2.3 7.6L10 15l-6.3 4.6L6 12 0 7.4h7.4Z"/></symbol>
<symbol id="i-check" viewBox="0 0 24 24"><path d="M20 6 9 17l-5-5" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></symbol>
{SITE_ICONS}
<symbol id="i-people" viewBox="0 0 24 24"><g fill="none" stroke="{INK}" stroke-width="2" stroke-linecap="round"><circle cx="9" cy="7" r="4"/><path d="M1 21v-2a4 4 0 0 1 4-4h8a4 4 0 0 1 4 4v2M16 3.1a4 4 0 0 1 0 7.8M23 21v-2a4 4 0 0 0-3-3.9"/></g></symbol>
<symbol id="i-scale" viewBox="0 0 24 24"><g fill="none" stroke="{INK}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v18M5 21h14M5 7h14M5 7l-3 7a3 3 0 0 0 6 0ZM19 7l-3 7a3 3 0 0 0 6 0Z"/></g></symbol>
<symbol id="i-shield" viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" fill="none" stroke="{INK}" stroke-width="2" stroke-linejoin="round"/><path d="m8.5 12 2.5 2.5 4.5-5" fill="none" stroke="{ACCENT}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></symbol>
<symbol id="i-phone" viewBox="0 0 24 24"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z" fill="none" stroke="currentColor" stroke-width="2"/></symbol>
</defs></svg>"""


def check(color=INK):
    return f'<svg width="18" height="18" style="color:{color}" aria-hidden="true"><use href="#i-check"/></svg>'


IMG = os.path.join(HERE, "img")  # icônes et images de partage, produites par _build/images.py


def og_image(slug):
    """Image de partage : celle de l'article si elle existe, sinon l'image générale du site."""
    if slug.startswith("blog/") and os.path.exists(os.path.join(IMG, "og", slug[5:] + ".png")):
        return f"{DOMAIN}/assets/og/{slug[5:]}.png"
    return f"{DOMAIN}/assets/og-default.png"


def head(title, desc, slug, extra_ld=None):
    canonical = DOMAIN + ("/" if slug == "index" else f"/{slug}")
    img = og_image(slug)
    art = next((a for a in ARTICLES if "blog/" + a["slug"] == slug), None)
    og_type = (f'<meta property="og:type" content="article">\n<meta property="article:published_time" content="{art["date"]}">'
               if art else '<meta property="og:type" content="website">')
    ld = ""
    if extra_ld:
        ld = '<script type="application/ld+json">' + json.dumps(extra_ld, ensure_ascii=False) + "</script>"
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
{og_type}
<meta property="og:locale" content="fr_FR">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{title}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{img}">
<meta name="theme-color" content="{SITE_THEME}">
<link rel="icon" href="{A('favicon.ico')}" sizes="48x48">
<link rel="icon" type="image/svg+xml" href="{A('assets/favicon.svg')}">
<link rel="icon" type="image/png" sizes="96x96" href="{A('assets/favicon-96x96.png')}">
<link rel="apple-touch-icon" href="{A('assets/apple-touch-icon.png')}">
<link rel="manifest" href="{A('site.webmanifest')}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
{SITE_FONTS_LINK}
<link rel="stylesheet" href="{A('assets/style.css')}?v={asset_v('style.css')}">
{ld}
</head>
<body>
<a class="skip" href="#contenu">Aller au contenu</a>
{SPRITE}
"""


def header(active):
    cur = ' aria-current="page"'
    links = "".join(f'<a href="{L(s)}"{cur if s == active else ""}>{t}</a>' for s, t in NAV)
    return f"""<header class="site-head">
  <div class="wrap">
    <a class="brand" href="{L('index')}" aria-label="{SITE_BRAND_HTML}, accueil">{mark_svg(False)}<span class="brand-txt"><span class="brand-name">{SITE_BRAND_SHORT}</span><span class="brand-sub">{SITE_BRAND_SUB}</span></span></a>
    <nav class="nav" aria-label="Navigation principale">{links}</nav>
    <button class="menu-btn" type="button" aria-expanded="false" aria-label="Ouvrir le menu">Menu</button>
    <div class="head-cta"><a class="head-tel" href="tel:+33187667031">01 87 66 70 31</a><a class="btn btn-red btn-sm" href="{L('devis')}">Étude gratuite</a></div>
  </div>
</header>
<main id="contenu">
"""


def footer():
    return f"""</main>
<section class="cta-band bg-red">
  <div class="wrap">
    <div><h2 class="relief-cream">{SITE_CTA_TITLE}</h2><p>Envoyez-nous votre contrat : on vérifie gratuitement, et on vous dit ce qui manque.</p></div>
    <a class="btn btn-navy" href="{L('devis')}">Demander mon étude</a>
  </div>
</section>
<footer class="site-foot">
  <div class="wrap">
    <div class="foot-top">
      <div class="foot-brand">
        <a class="brand" href="{L('index')}">{mark_svg(True)}<span class="brand-txt"><span class="brand-name">{SITE_BRAND_SHORT}</span><span class="brand-sub">{SITE_BRAND_SUB}</span></span></a>
        <p>L'humain au cœur de la relation : {SITE_FOOT_ABOUT}, avec un vrai conseiller à l'écoute. Une marque de WealthWise Conseil.</p>
        <p>01 87 66 70 31 · contact@wealthwiseconseil.fr<br>WhatsApp salariés : 06 89 16 64 54 (réponse en 15 min, lun.–ven. 9 h–19 h)</p>
      </div>
      <div><h3>Votre métier</h3><ul>{"".join(f'<li><a href="{L(s)}">{x}</a></li>' for s, x in SITE_FOOT_METIER)}</ul></div>
      <div><h3>Guides</h3><ul>{"".join(f'<li><a href="{L(s)}">{x}</a></li>' for s, x in SITE_FOOT_GUIDES)}<li><a href="{L('outils')}#simulateur">Simulateur de coût</a></li><li><a href="{L('outils')}#checkup">Check-up conformité</a></li><li><a href="{L('blog')}">Le blog</a></li></ul></div>
      <div><h3>Contact</h3><ul><li><a href="{L('devis')}">Demande d'étude</a></li><li><a href="{L('mentions-legales')}">Mentions légales</a></li><li><a href="https://www.wealthwiseconseil.fr/">WealthWise Conseil, le cabinet</a></li><li><a href="https://www.wealthwiseconseil.fr/{SITE_WWC_CCN[0]}">{SITE_WWC_CCN[1]}</a></li></ul></div>
    </div>
    <div class="foot-legal">
      <p>{SITE_BRAND_HTML} est une marque commerciale de WealthWise Conseil, SASU, cabinet de courtage en assurance (catégorie « b »), immatriculé à l'ORIAS sous le n° 24000251, RCS Nanterre 980 572 671, 67 rue de Passy, 75116 Paris. Activité sous le contrôle de l'ACPR, 4 place de Budapest, 75436 Paris Cedex 09. Réclamations : reclamation@wealthwiseconseil.fr. Médiateur : CMAP, 39 avenue Franklin D. Roosevelt, 75008 Paris.</p>
      <p>Site indépendant, {SITE_INDEP} · Photos : Unsplash · <a href="{L('mentions-legales')}">Mentions légales et données personnelles</a> · © 2026 WealthWise Conseil</p>
    </div>
  </div>
</footer>
{'' if MODE == 'preview' else '<script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@4.4.1/dist/email.min.js"></script>'}
<script src="{A('assets/main.js')}?v={asset_v('main.js')}"></script>
{'<script>CONFIG.preview = true;</script>' if MODE == 'preview' else ''}
</body>
</html>
"""


def lead_form(origin, title="Demande d'étude", type_default=None):
    type_default = type_default or SITE_TYPES[0]
    types = SITE_TYPES
    chips = "".join(f'<label class="chip"><input type="radio" name="type" value="{t}"{" checked" if t == type_default else ""}><span>{t}</span></label>' for t in types)
    besoins = SITE_BESOINS
    bchips = "".join(f'<label class="chip"><input type="radio" name="besoin" value="{b}"{" checked" if i == 0 else ""}><span>{b}</span></label>' for i, b in enumerate(besoins))
    sal = "".join(f'<option{" selected" if s == SITE_EFFECTIFS[1] else ""}>{s}</option>' for s in SITE_EFFECTIFS)
    o = origin
    return f"""<div class="ticket">
  <div class="ticket-head"><strong>{title}</strong><span class="ticket-ref">Fiche n° —</span></div>
  <form class="lead-form" data-origin="{o}" novalidate>
    <fieldset><legend>{SITE_LEGEND}</legend><div class="chips">{chips}</div></fieldset>
    <fieldset><legend>Votre besoin</legend><div class="chips">{bchips}</div></fieldset>
    <div class="row2">
      <div class="field"><label class="lbl" for="{o}-sal">Nombre de salariés</label><select id="{o}-sal" name="salaries">{sal}</select></div>
      <div class="field"><label class="lbl" for="{o}-cp">Code postal</label><input id="{o}-cp" name="cp" type="text" inputmode="numeric" maxlength="5" autocomplete="postal-code" placeholder="{SITE_PH[0]}"></div>
    </div>
    <div class="row2">
      <div class="field"><label class="lbl" for="{o}-nom">Prénom et nom</label><input id="{o}-nom" name="nom" type="text" autocomplete="name" placeholder="{SITE_PH[1]}"></div>
      <div class="field"><label class="lbl" for="{o}-etab">{SITE_ETAB}</label><input id="{o}-etab" name="etablissement" type="text" autocomplete="organization" placeholder="{SITE_PH[2]}"></div>
    </div>
    <div class="row2">
      <div class="field"><label class="lbl" for="{o}-tel">Téléphone</label><input id="{o}-tel" name="tel" type="tel" autocomplete="tel" placeholder="06 12 34 56 78"></div>
      <div class="field"><label class="lbl" for="{o}-email">E-mail</label><input id="{o}-email" name="email" type="email" autocomplete="email" placeholder="{SITE_PH[3]}"></div>
    </div>
    <label class="consent" for="{o}-consent"><input id="{o}-consent" name="consent" type="checkbox"><span class="consent-text">J'accepte d'être rappelé(e) par téléphone par WealthWise Conseil (marque {SITE_BRAND_HTML}) au sujet de ma demande. Je peux retirer ce consentement à tout moment.</span></label>
    <div class="form-msg" role="alert" hidden></div>
    <button type="submit" class="btn btn-red">Recevoir mon étude gratuite</button>
    <p class="fine">Sans case cochée, nous vous répondons uniquement par e-mail. Vos données servent seulement à traiter votre demande (responsable : WealthWise Conseil). Détails dans les <a href="{L('mentions-legales')}">mentions légales</a>.</p>
  </form>
  <div class="lead-done" hidden>
    <span class="t-label" style="color:var(--teal)">Demande enregistrée</span>
    <h3>Merci, c'est noté.</h3>
    <p class="done-text">Un conseiller vous rappelle sous 24 h ouvrées avec les premières pistes. {SITE_DONE_TXT}</p>
    <p class="ref"></p>
  </div>
</div>"""


def insurers_block():
    tiles = "".join(f'<div><img src="{A("assets/assureurs/" + f + ".png")}" alt="{n}" loading="lazy" width="140" height="42"></div>' for f, n in INSURERS)
    return f"""<section class="band bg-cream2">
  <div class="wrap">
    <div class="sec-head"><span class="t-label">On compare pour vous</span><h2>Plus de 15 assureurs mis en concurrence</h2><p>Mutuelles, institutions de prévoyance, assureurs : nous travaillons avec plusieurs organismes, sans obligation d'exclusivité, {SITE_INSURERS_TXT}</p></div>
    <div class="insurers">{tiles}</div>
  </div>
</section>"""


def posters_block():
    return site_posters()


def wwc_links(links, title="Pour aller plus loin"):
    lis = "".join(f'<li><a href="{WWC}/{p}">{t}</a></li>' for p, t in links)
    return f"""<section class="band bg-cream2" style="padding-block:48px">
  <div class="wrap narrow">
    <div class="wwc-box">
      <span class="t-label">{title}</span>
      <h2>Les guides de WealthWise Conseil</h2>
      <p>{SITE_BRAND_HTML} est la marque {SITE_WWC_MARQUE} du cabinet de courtage WealthWise Conseil. Retrouvez ses guides détaillés :</p>
      <ul>{lis}</ul>
    </div>
  </div>
</section>"""


def faq_block(items, title="Questions fréquentes"):
    det = "".join(f"<details{' open' if i == 0 else ''}><summary>{q}</summary><p>{a}</p></details>" for i, (q, a) in enumerate(items))
    return f"""<section class="band bg-cream">
  <div class="wrap">
    <div class="sec-head"><span class="t-label">{title}</span><h2>Ce que nous demandent les dirigeants</h2></div>
    <div class="faq">{det}</div>
  </div>
</section>"""


def faq_ld(items):
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a)}} for q, a in items]}


ORG_LD = {"@type": "InsuranceAgency", "name": BRAND, "alternateName": SITE_ALT_NAME,
          "url": DOMAIN + "/", "logo": DOMAIN + "/assets/icon-512.png", "image": DOMAIN + "/assets/og-default.png", "telephone": "+33187667031", "email": "contact@wealthwiseconseil.fr", "areaServed": "FR",
          "parentOrganization": {"@type": "Organization", "name": "WealthWise Conseil", "url": "https://www.wealthwiseconseil.fr/"},
          "address": {"@type": "PostalAddress", "streetAddress": "67 rue de Passy", "postalCode": "75116", "addressLocality": "Paris", "addressCountry": "FR"},
          "description": SITE_ORG_DESC}


def page_hero(bg, crumb, h1, sub, lead, ill, h1cls="relief-red", subcolor="var(--red)", on_navy=False):
    return f"""<section class="page-hero {bg}{' on-navy' if on_navy else ''}">
  <div class="wrap">
    <div>
      <span class="crumb"><a href="{L('index')}">Accueil</a> · {crumb}</span>
      <h1 class="{h1cls}">{h1}</h1>
      <p class="sub" style="color:{subcolor}">{sub}</p>
      <p class="lead">{lead}</p>
      <p class="hero-cta" style="margin-top:22px;display:flex;flex-wrap:wrap;gap:12px 18px;align-items:center"><a class="btn {'btn-navy' if bg in ('bg-red', 'bg-mustard') else 'btn-red'}" href="{L('devis')}">Demander mon étude gratuite</a><a href="tel:+33187667031" style="font-weight:700;color:inherit;text-decoration:underline">ou appelez le 01 87 66 70 31</a></p>
    </div>
    {ill}
  </div>
</section>"""


def ill(icon):
    return f'<svg class="ill-big" viewBox="0 0 64 64" aria-hidden="true"><use href="#{icon}"/></svg>'



# ---------------------------------------------------------------- PHOTOS ET TÉMOIGNAGES
# Photos libres de droits (licence Unsplash), servies par le CDN d'Unsplash.
def photo(pid, alt, w=900, h=700, cls="", lazy=True):
    base = f"https://images.unsplash.com/photo-{pid}?auto=format&fit=crop&q=70"
    return (f'<img class="{cls}" src="{base}&w={w}&h={h}" srcset="{base}&w={w}&h={h} 1x, {base}&w={w * 2}&h={h * 2} 2x" '
            f'alt="{alt}" width="{w}" height="{h}"{' loading="lazy"' if lazy else ''} decoding="async">')


def photo_ill(pid, alt):
    return photo(pid, alt, 600, 720, "ill-photo", lazy=False)




def proof_band():
    items = [("ORIAS 24000251", "Courtier en assurance immatriculé, sous le contrôle de l'ACPR"),
             ("15+ assureurs", "Mis en concurrence pour chaque étude, sans exclusivité"),
             ("15 min", "Réponse garantie sur le WhatsApp de vos salariés, en semaine"),
             ("0 €", "Étude et comparatif gratuits, sans engagement")]
    cells = "".join(f'<div><strong>{a}</strong><span>{b}</span></div>' for a, b in items)
    return f'<div class="proof-band">{cells}</div>'


def photo_strip():
    cards = "".join(f'<figure class="photo-card">{photo(p, a, 640, 480, lazy=False)}<figcaption><h3>{c}</h3><p>{t}</p></figcaption></figure>'
                    for p, a, c, t in PHOTO_STRIP)
    return f"""<section class="band bg-cream photo-band">
  <div class="wrap">
    <div class="sec-head"><span class="t-label">Votre métier</span><h2>{PHOTO_STRIP_TITLE}</h2><p>{PHOTO_STRIP_TEXT}</p></div>
    <div class="photo-cards">{cards}</div>
    {proof_band()}
  </div>
</section>"""


# Témoignages : uniquement des retours réels de clients, publiés avec leur accord
# À remplir uniquement avec des retours vérifiables (message d'origine et accord du client conservés).
# Format : ("Texte du témoignage", "Client ou Cliente", "Type d'établissement")
TEMOIGNAGES = SITE_TEMOIGNAGES


def testimonials_block():
    if not TEMOIGNAGES:
        return ""
    cards = "".join(f'<figure class="temoignage"><blockquote>« {t} »</blockquote><figcaption><strong>{n}</strong><span>{r}</span></figcaption></figure>'
                    for t, n, r in TEMOIGNAGES)
    return f"""<section class="band bg-cream2" id="temoignages">
  <div class="wrap">
    <div class="sec-head"><span class="t-label">Ils nous font confiance</span><h2>Ce qu'en disent nos clients</h2></div>
    <div class="temoignages">{cards}</div>
    <p class="fine" style="margin-top:14px">Témoignages recueillis auprès de clients du cabinet WealthWise Conseil et publiés avec leur accord.</p>
  </div>
</section>"""



PAGES = {}
exec(open(os.path.join(HERE, "pages.py"), encoding="utf-8").read())  # pages du site


# ---------------------------------------------------------------- MENTIONS
PAGES["mentions-legales"] = (
    "Mentions légales · " + SITE_BRAND_HTML,
    "Mentions légales du site " + SITE_BRAND_HTML + ", marque de WealthWise Conseil, courtier en assurance (ORIAS 24000251).",
    None,
    "mentions-legales",
    f"""<section class="band bg-cream">
  <div class="wrap narrow prose">
    <h1 class="t-slab relief-red" style="font-size:clamp(2rem,4vw,2.8rem)">Mentions légales</h1>
    <h2>Éditeur</h2>
    <p>Le site {SITE_DOMAIN_TXT} est édité par <strong>WealthWise Conseil</strong>, SASU, dont « {SITE_BRAND_HTML} » est une marque commerciale. Siège : 67 rue de Passy, 75116 Paris. RCS Nanterre 980 572 671 · SIRET 980 572 671 00017 · APE 6622Z. Téléphone : 01 87 66 70 31 · contact@wealthwiseconseil.fr. Directeur de la publication : Nicolas Ferran, Président.</p>
    <h2>Statut de courtier</h2>
    <p>WealthWise Conseil est immatriculé à l'ORIAS sous le n° 24000251 (www.orias.fr) en qualité de courtier en assurance, catégorie « b » : le cabinet n'est soumis à aucune obligation contractuelle de travailler exclusivement avec une ou plusieurs entreprises d'assurance. La liste des assureurs partenaires est communiquée sur simple demande. Le cabinet ne détient aucune participation de 10 % ou plus dans une entreprise d'assurance, et aucune entreprise d'assurance n'en détient dans le cabinet.</p>
    <p>Rémunération : commission incluse dans la cotisation d'assurance, versée par l'assureur.</p>
    <p>Autorité de contrôle : ACPR, 4 place de Budapest, CS 92459, 75436 Paris Cedex 09.</p>
    <p>Responsabilité civile professionnelle et garantie financière (articles L.512-6 et L.512-7 du Code des assurances) : MMA IARD Assurances Mutuelles / MMA IARD, 14 boulevard Marie et Alexandre Oyon, 72030 Le Mans Cedex 9, police n° 112 786 342.</p>
    <h2>Indépendance</h2>
    <p>{SITE_BRAND_HTML} est un service privé de courtage. {SITE_INDEP_MENTIONS} Les logos d'assureurs présentés appartiennent à leurs propriétaires et illustrent les organismes que le cabinet peut consulter.</p>
    <h2>Réclamations et médiation</h2>
    <p>Réclamations : reclamation@wealthwiseconseil.fr ou par courrier au siège. Accusé de réception sous 10 jours ouvrables, réponse sous 2 mois au plus. En l'absence de réponse satisfaisante : Centre de Médiation et d'Arbitrage de Paris (CMAP), service Médiation de la consommation, 39 avenue Franklin D. Roosevelt, 75008 Paris.</p>
    <h2>Données personnelles</h2>
    <p>Responsable du traitement : WealthWise Conseil. Les informations du formulaire servent uniquement à traiter votre demande d'étude, à vous recontacter et, le cas échéant, à préparer votre contrat (base légale : mesures précontractuelles prises à votre demande). Elles sont transmises par le service EmailJS.</p>
    <p>Rappel téléphonique : vous n'êtes appelé(e) que si vous avez coché la case de consentement prévue à cet effet. Ce consentement est horodaté et conservé comme preuve ; vous pouvez le retirer à tout moment.</p>
    <p>Destinataires : les équipes de WealthWise Conseil et, à votre demande, les assureurs consultés. Aucune cession ni vente. Conservation : 3 ans après le dernier contact pour un prospect ; durée de la relation puis 5 ans pour un client.</p>
    <p>Droits d'accès, de rectification, d'effacement, d'opposition, de limitation et de portabilité : rgpd@wealthwiseconseil.fr. Réclamation possible auprès de la CNIL (www.cnil.fr).</p>
    <h2>Hébergement</h2>
    <p>Vercel Inc., 440 N Barranca Avenue #4133, Covina, CA 91723, États-Unis.</p>
    <h2>Propriété intellectuelle</h2>
    <p>Textes, illustrations, logo et marque « {SITE_BRAND_HTML} » : propriété de WealthWise Conseil. Reproduction interdite sans autorisation préalable.</p>
    <p style="color:var(--muted)">Mise à jour : octobre 2026.</p>
  </div>
</section>
""")


# ---------------------------------------------------------------- BLOG
MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]


def fr_date(iso):
    y, m, d = iso.split("-")
    return f"{int(d)} {MOIS[int(m) - 1]} {y}"


LINK_ANCHORS = {"simulateur": "simulateur de coût", "checkup": "check-up conformité"}


def art_body(a):
    """{{L:slug}} dans un attribut href="…" devient l'adresse ; seul dans le texte, il devient un lien complet avec un libellé lisible."""
    body = a["body"]
    labels = {s: t[:1].lower() + t[1:] for s, t in NAV}
    labels.update({"devis": "demande d'étude gratuite", "index": "page d'accueil"})

    def rep(m):
        slug, anc = m.group(1), (m.group(2) or m.group(3) or "")
        url = L(slug) + anc
        if body[max(0, m.start() - 6):m.start()].endswith('href="'):
            return url + (m.group(3) or "") if m.group(2) else url
        label = LINK_ANCHORS.get(anc[1:]) or labels.get(slug) or slug.split("/")[-1].replace("-", " ")
        return f'<a href="{url}">{label}</a>'
    return re.sub(r"\{\{L:([a-z0-9\-/]+)(#[a-z0-9\-]+)?\}\}(#[a-z0-9\-]+)?", rep, body)


def blog_card(a):
    return f"""<a class="blog-card" href="{L('blog/' + a['slug'])}">
  <span class="blog-thumb {a['color']}{' on-navy' if a['color'] == 'bg-navy' else ''}"><svg aria-hidden="true"><use href="#{a['icon']}"/></svg><span class="t-label">{a['cat']}</span></span>
  <span class="blog-meta">{fr_date(a['date'])} · {a['minutes']} min de lecture</span>
  <span class="blog-title">{a['title']}</span>
  <span class="blog-desc">{a['desc']}</span>
</a>"""


def blog_index():
    cards = "".join(blog_card(a) for a in ARTICLES)
    return page_hero("bg-mustard", "Blog", SITE_BLOG[0], "Mutuelle, prévoyance, et tout ce qui va avec.", SITE_BLOG[1], ill(SITE_BLOG[2])) + f"""
<section class="band bg-cream">
  <div class="wrap"><div class="blog-grid">{cards}</div></div>
</section>"""


def article_page(a):
    others = [o for o in ARTICLES if o["slug"] != a["slug"]][:3]
    rel = "".join(blog_card(o) for o in others)
    return f"""<article>
<section class="page-hero {a['color']}{' on-navy' if a['color'] == 'bg-navy' else ''}">
  <div class="wrap" style="grid-template-columns:minmax(0,1fr)">
    <div>
      <span class="crumb"><a href="{L('index')}">Accueil</a> · <a href="{L('blog')}">Blog</a> · {a['cat']}</span>
      <h1 class="art-h1">{a['title']}</h1>
      <p class="lead" style="margin-top:14px">{fr_date(a['date'])} · {a['minutes']} min de lecture · Par WealthWise Conseil</p>
    </div>
  </div>
</section>
<section class="band bg-cream" style="padding-top:40px">
  <div class="wrap narrow prose article">
    {art_body(a)}
    <div class="author-box"><strong>À propos</strong><p>{AUTHOR}</p></div>
  </div>
</section>
</article>
<section class="band bg-mustard">
  <div class="wrap split">
    <div class="sec-head" style="margin:0"><span class="t-label">Étude gratuite</span><h2>Votre contrat est-il à jour ?</h2><p style="color:var(--ink)">Un conseiller vérifie gratuitement votre mutuelle et votre prévoyance, et vous rappelle sous 24 h ouvrées.</p></div>
    {lead_form('blog-' + a['slug'][:20], "Demande d'étude")}
  </div>
</section>
<section class="band bg-cream2">
  <div class="wrap"><div class="sec-head"><span class="t-label">À lire aussi</span><h2>Sur le même sujet</h2></div><div class="blog-grid">{rel}</div></div>
</section>"""


PAGES["blog"] = (SITE_BLOG[3] + " · " + SITE_BRAND_HTML,
                 SITE_BLOG[4],
                 {"@context": "https://schema.org", "@graph": [ORG_LD, {"@type": "Blog", "name": "Le blog " + BRAND, "url": DOMAIN + "/blog", "publisher": {"@type": "Organization", "name": "WealthWise Conseil", "url": WWC + "/"}}]},
                 "blog", blog_index)
for _a in ARTICLES:
    PAGES["blog/" + _a["slug"]] = (
        _a["title"] + " · " + SITE_BRAND_HTML, _a["desc"],
        {"@context": "https://schema.org", "@type": "BlogPosting", "headline": _a["title"], "description": _a["desc"], "image": og_image("blog/" + _a["slug"]),
         "datePublished": _a["date"], "dateModified": _a["date"], "mainEntityOfPage": DOMAIN + "/blog/" + _a["slug"],
         "author": {"@type": "Organization", "name": "WealthWise Conseil", "url": WWC + "/"},
         "publisher": {"@type": "Organization", "name": BRAND, "url": DOMAIN + "/", "parentOrganization": {"@type": "Organization", "name": "WealthWise Conseil", "url": WWC + "/"}}},
        "blog", (lambda a=_a: article_page(a)))


def build():
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(os.path.join(OUT, "assets", "assureurs"))
    shutil.copy(os.path.join(HERE, "style.css"), os.path.join(OUT, "assets", "style.css"))
    shutil.copy(os.path.join(HERE, "main.js"), os.path.join(OUT, "assets", "main.js"))
    for f, _ in INSURERS:
        shutil.copy(os.path.join(REPO_LOGOS, f + ".png"), os.path.join(OUT, "assets", "assureurs", f + ".png"))
    open(os.path.join(OUT, "assets", "favicon.svg"), "w").write(favicon_svg())
    # icônes et images de partage (voir _build/images.py)
    if os.path.isdir(IMG):
        shutil.copy(os.path.join(IMG, "favicon.ico"), os.path.join(OUT, "favicon.ico"))
        for f in ("favicon-96x96.png", "apple-touch-icon.png", "icon-192.png", "icon-512.png", "og-default.png"):
            shutil.copy(os.path.join(IMG, f), os.path.join(OUT, "assets", f))
        shutil.copytree(os.path.join(IMG, "og"), os.path.join(OUT, "assets", "og"))
    open(os.path.join(OUT, "site.webmanifest"), "w").write(json.dumps({
        "name": BRAND, "short_name": BRAND, "start_url": "/", "display": "standalone",
        "background_color": SITE_THEME, "theme_color": SITE_THEME,
        "icons": [{"src": "/assets/icon-192.png", "sizes": "192x192", "type": "image/png"},
                  {"src": "/assets/icon-512.png", "sizes": "512x512", "type": "image/png"}]}, ensure_ascii=False, indent=2))
    open(os.path.join(OUT, "assets", f"logo-{SITE_SLUG}-clair.svg"), "w").write(mark_svg(False, "logo", True))
    open(os.path.join(OUT, "assets", f"logo-{SITE_SLUG}-fonce.svg"), "w").write(mark_svg(True, "logo", True))
    open(os.path.join(OUT, "assets", f"pastille-{SITE_SLUG}.svg"), "w").write(pastille_svg(True))
    global PREFIX
    for slug, (title, desc, ld, active, body) in PAGES.items():
        PREFIX = "../" if (MODE == "preview" and "/" in slug) else ""
        if callable(body):
            body = body()
        html = head(title, desc, slug, ld) + header(active) + body + footer()
        os.makedirs(os.path.dirname(os.path.join(OUT, f"{slug}.html")), exist_ok=True)
        if slug == "mentions-legales":
            html = html.replace('<meta name="description"', '<meta name="robots" content="noindex, follow">\n<meta name="description"', 1)
        open(os.path.join(OUT, f"{slug}.html"), "w").write(html)
    if MODE == "deploy":
        open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
        urls = "".join(f"  <url><loc>{DOMAIN}{'/' if s == 'index' else '/' + s}</loc><lastmod>{LASTMOD}</lastmod></url>\n" for s in PAGES if s != "mentions-legales")
        open(os.path.join(OUT, "sitemap.xml"), "w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
        open(os.path.join(OUT, "vercel.json"), "w").write(json.dumps({
            "cleanUrls": True, "trailingSlash": False,
            "redirects": [{"source": "/:path*.html", "destination": "/:path*", "permanent": True}],
            "headers": [{"source": "/(.*)", "headers": [{"key": "X-Content-Type-Options", "value": "nosniff"}, {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"}]},
                        {"source": "/assets/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=604800"}]}]}, indent=2))
    print("OK", MODE, OUT, len(PAGES), "pages")


build()
