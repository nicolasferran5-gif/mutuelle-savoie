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
import boost_guides as GD
import boost_mascots as MS

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
    b = _hex(t[getattr(CFG, "LOGO_BG", "red")])          # couleur de marque : dégradé du héros, teintes, étiquettes
    t["brand"] = _tohex(b); t["brand-d"] = _tohex(_mix(b, _hex(t["navy"]), .62)); t["brand-l"] = _tohex(_mix(b, (255, 255, 255), .16))
    return t


def _hash(s):
    return hashlib.md5(s.encode()).hexdigest()[:8]


def _txt(s):
    return re.sub(r"\s+", " ", _html.unescape(re.sub(r"<[^>]+>", " ", s))).strip()


# ------------------------------------------------------------------ logos : pictogramme simple dans une tuile arrondie
ICONS = {
    "cloche": '<path d="M16 41a16 16 0 0 1 32 0"/><path d="M12 46h40"/><circle class="a" cx="32" cy="21" r="3.2"/>',
    "ciseaux": '<circle cx="22" cy="45" r="6"/><circle cx="42" cy="45" r="6"/><path d="M26 40 44 16M38 40 20 16"/><circle class="a" cx="32" cy="32" r="2.6"/>',
    "pain": '<path d="M14 44V38c0-10 8-17 18-17s18 7 18 17v6Z"/><path class="s" d="M25 29l3 7M32 27v8M39 29l-3 7"/>',
    "code": '<path d="M25 23 14 32l11 9M39 23l11 9-11 9"/><path class="s" d="M35 19 29 45"/>',
    "croix": '<path d="M27 15h10v12h12v10H37v12H27V37H15V27h12Z"/><circle class="a" cx="32" cy="32" r="3"/>',
    "dent": '<path d="M23 16c-5.500 0-9 4-9 9.500 0 5 2.500 8 3.500 13 .9 4.500 1.500 10 4.500 10 3.200 0 3-7.500 5-11 1-1.800 2.500-2.500 4.500-2.500s3.500.7 4.500 2.500c2 3.500 1.800 11 5 11 3 0 3.600-5.500 4.500-10 1-5 3.500-8 3.500-13 0-5.500-3.500-9.500-9-9.500-3.500 0-5.500 1.800-8.500 1.800S26.500 16 23 16Z"/><path class="s" d="M39 23c2 .6 3.200 2.200 3.400 4.400"/>',
    "golf": '<path d="M27 14v33"/><path class="f" d="M27 15l17 6.500L27 28Z"/><path d="M13 49c7-4.500 31-4.500 38 0"/>',
    "maison": '<path d="M13 32 32 16l19 16"/><path d="M19 28v20h26V28"/><circle class="a" cx="32" cy="36" r="3"/><path class="s" d="M32 39v5"/>',
    "beret": '<path d="M11 37c0-9 9-15 21-15s21 6 21 15c0 3.500-9.500 6-21 6s-21-2.500-21-6Z"/><path class="s" d="M32 22v-6"/>',
    "burger": '<path d="M15 30c0-9 7.500-14 17-14s17 5 17 14Z"/><path class="s" d="M13 37.500h38"/><path d="M16 44h32v1a5 5 0 0 1-5 5H21a5 5 0 0 1-5-5Z"/>',
}


def logo_svg(navy, accent, cls=' class="logo-mark"', extra="", dark="#1D2250", sec="#11A39B"):
    if CFG.LOGO in MS.M:   # logo dessiné : {D} foncé du site, {A} couleur de marque, {Y} accent
        g = MS.M[CFG.LOGO].format(D=dark, A=navy, Y=accent, S=sec, W="#FFFFFF", C="#F3ECDD")
        return f'<svg{cls} viewBox="0 0 64 64" aria-hidden="true"{extra}>{g}</svg>'
    ic = ICONS[CFG.LOGO]
    st = (f'<style>.bxl *{{fill:none;stroke:#fff;stroke-width:3.6;stroke-linecap:round;stroke-linejoin:round}}'
          f'.bxl .a{{fill:{accent};stroke:none}}.bxl .s{{stroke:{accent}}}.bxl .f{{fill:{accent};stroke:{accent}}}</style>')
    return (f'<svg{cls} viewBox="0 0 64 64" aria-hidden="true"{extra}>{st}<rect width="64" height="64" rx="18" fill="{navy}"/>'
            f'<g class="bxl">{ic}</g></svg>')


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


SITUATIONS = [
    ("Structure de cotisation", "Une équipe jeune, surtout des salariés sans enfant",
     "Le contrat prévoit une cotisation unique « famille » : tout le monde paie le même prix, que l'on couvre une personne ou cinq. Les salariés seuls paient pour les familles des autres, et l'employeur finance la moitié d'un tarif trop large.",
     ["Nous comparons trois structures : tarif unique, « isolé / famille » et « adulte / enfant ».", "La part employeur est calée sur la couverture obligatoire du salarié (au moins 50 %).", "Conjoint et enfants deviennent une option, payée par ceux qui en ont besoin."],
     "Chacun paie pour sa situation réelle, et le budget de l'employeur ne dépend plus de la composition des foyers."),
    ("Âge moyen de l'équipe", "Une équipe fidèle, dont l'âge moyen augmente",
     "À chaque échéance, la cotisation monte. L'assureur applique sa grille standard, sans regarder qui compose vraiment l'équipe ni ce qu'elle consomme.",
     ["Nous présentons aux assureurs la démographie réelle : âge moyen, répartition par âge, ancienneté, familles.", "Nous demandons les comptes de résultats du contrat pour voir les postes vraiment utilisés (optique, dentaire, hospitalisation).", "Nous mettons en concurrence les assureurs qui tarifent le mieux ce profil."],
     "Le tarif est négocié sur votre équipe, pas sur une moyenne nationale, et les garanties suivent les besoins réels."),
    ("Gestion multisite", "Trois établissements, trois contrats, trois échéances",
     "Chaque site a souscrit de son côté. Les garanties diffèrent, un salarié qui change de site change de mutuelle, et personne n'a de vue d'ensemble.",
     ["Un contrat unique, avec les mêmes garanties partout et un seul interlocuteur.", "Des affiliations centralisées, mais un suivi et une facturation par établissement.", "Un effectif regroupé face aux assureurs, donc plus de poids dans la négociation."],
     "Une seule gestion au lieu de trois, et des salariés traités de la même façon d'un site à l'autre. Selon que vos sites forment une ou plusieurs sociétés, nous vérifions aussi le seuil de 11 salariés, à partir duquel le forfait social de 8 % s'applique."),
    ("Entrées et sorties", "Beaucoup de contrats courts, de temps partiels et de départs",
     "Entre les embauches de la saison, les CDD et les départs, des salariés ne sont ni affiliés ni dispensés par écrit. C'est le premier point que regarde l'URSSAF.",
     ["Une routine d'embauche : affiliation ou dispense signée dès le premier jour.", "Le versement santé pour les contrats très courts qui y ont droit.", "La portabilité gérée à chaque départ : jusqu'à 12 mois de maintien gratuit pour l'ancien salarié."],
     "Plus d'oubli à l'entrée ni à la sortie, et un dossier prêt le jour d'un contrôle."),
    ("Prévoyance des cadres", "Un premier salarié passe cadre",
     "L'entreprise n'a jamais eu de cadre. Elle ignore qu'elle doit désormais financer seule une prévoyance d'au moins 1,50 % de la tranche A du salaire.",
     ["Nous mettons en place le contrat de prévoyance cadres, affecté en priorité au risque décès.", "Coût maximal pour un salaire au plafond : 60,08 € par mois et par cadre en 2026 (1,50 % de 4 005 €).", "Nous vérifions au passage la prévoyance des non-cadres prévue par votre convention."],
     "L'entreprise est à l'abri de la sanction prévue : sans ce contrat, elle peut devoir verser elle-même trois plafonds annuels de la Sécurité sociale, soit 144 180 € en 2026, à la famille du cadre décédé."),
    ("Prise en charge", "Des salariés mal remboursés en dentaire et en optique",
     "Le contrat est au minimum légal. Les restes à charge s'accumulent, les salariés se plaignent, et l'employeur ne veut pas doubler son budget.",
     ["Une base conforme, financée à 50 % au moins par l'employeur.", "Des niveaux supérieurs en option, que chaque salarié choisit et paie selon ses besoins.", "Un service d'explication des remboursements pour les salariés, par WhatsApp."],
     "De meilleures prises en charge pour ceux qui le souhaitent, sans alourdir la part de l'employeur."),
]


def situations_block():
    panels = ""
    for i, (tag, title, pb, acts, res) in enumerate(SITUATIONS):
        lis = "".join(f"<li>{a}</li>" for a in acts)
        panels += (f'<article class="bx-sit" data-tag="{tag}"><span class="bx-sit-tag">{tag}</span><h3>{title}</h3>'
                   f'<div class="bx-sit-cols"><div><strong>La situation</strong><p>{pb}</p></div>'
                   f'<div><strong>Ce que nous faisons</strong><ul>{lis}</ul></div>'
                   f'<div class="bx-sit-res"><strong>Ce que ça change</strong><p>{res}</p></div></div>'
                   f'<a class="btn btn-red bx-sit-go" href="#etude" data-sit="{tag} : {title}">C\'est ma situation, je veux un avis</a></article>')
    return f"""<section class="band bg-cream" id="situations">
  <div class="wrap">
    <div class="sec-head"><span class="t-label">Situations types</span><h2>Six situations fréquentes, et ce qu'un courtier y change</h2><p>Des exemples types, construits à partir des cas que nous rencontrons le plus souvent. Les montants cités sont les chiffres légaux de 2026.</p></div>
    <div class="bx-sits" data-sits>{panels}</div>
  </div>
</section>
"""


COMPARE = [
    ("Nombre d'offres étudiées", "Une seule : la sienne", "Celles de ses partenaires", "Plus de 15 assureurs, sans exclusivité"),
    ("Connaissance de votre convention collective", "Variable selon le conseiller", "Pas de vérification", "Garanties vérifiées ligne par ligne"),
    ("Documents de l'employeur (acte de mise en place, dispenses, notices)", "Modèles fournis, à vous de les adapter", "Non fournis", "Préparés et mis à jour pour vous"),
    ("Négociation du tarif selon votre équipe", "Grille standard", "Tarif affiché, non négociable", "Tarif négocié sur l'âge moyen et les besoins réels"),
    ("Interlocuteur après la signature", "Plateforme téléphonique", "Aucun", "Un conseiller attitré, pour vous et vos salariés"),
    ("Remise en concurrence régulière", "Non, par définition", "À refaire vous-même", "Oui, à chaque échéance utile"),
    ("Coût de l'étude", "Gratuit", "Gratuit", "Gratuit, sans engagement"),
]


def compare_block():
    rows = "".join(f'<tr><th scope="row">{a}</th><td>{b}</td><td>{c}</td><td class="us">{d}</td></tr>' for a, b, c, d in COMPARE)
    return f"""<section class="band bg-cream" id="comparatif">
  <div class="wrap">
    <div class="sec-head"><span class="t-label">Comparatif</span><h2>Assureur en direct, comparateur en ligne ou courtier spécialisé ?</h2><p>Trois façons de choisir sa mutuelle et sa prévoyance d'entreprise. Voici ce que chacune comprend vraiment.</p></div>
    <div class="table-wrap bx-cmp"><table><thead><tr><th scope="col"></th><th scope="col">Assureur en direct</th><th scope="col">Comparateur en ligne</th><th scope="col" class="us">{CFG.BRAND}, courtier spécialisé</th></tr></thead><tbody>{rows}</tbody></table></div>
  </div>
</section>
"""


LEXIQUE = [
    ("Mutuelle d'entreprise", "Aussi appelée complémentaire santé collective. Depuis le 1er janvier 2016, tout employeur du secteur privé doit en proposer une à ses salariés, dès le premier, et financer au moins 50 % de la cotisation de la couverture obligatoire."),
    ("Prévoyance collective", "Contrat qui protège le salarié et sa famille en cas d'arrêt de travail, d'invalidité ou de décès. Elle complète les versements de la Sécurité sociale et le maintien de salaire dû par l'employeur."),
    ("Panier de soins minimum", "Socle de garanties que toute mutuelle d'entreprise doit au moins contenir : ticket modérateur, forfait journalier hospitalier, minimums en dentaire et en optique. Votre convention collective peut imposer davantage."),
    ("Contrat responsable", "Contrat santé qui respecte des planchers et des plafonds de remboursement fixés par la loi. C'est la condition pour que la part payée par l'employeur soit exonérée de cotisations sociales, dans certaines limites."),
    ("100 % Santé", "Dispositif qui permet d'obtenir des lunettes, des prothèses dentaires et des aides auditives sans reste à charge, dans une sélection d'équipements, avec tout contrat responsable."),
    ("Ticket modérateur", "Part d'une dépense de santé qui reste à payer après le remboursement de la Sécurité sociale. C'est la première chose que rembourse une mutuelle."),
    ("Base de remboursement", "Tarif de référence de la Sécurité sociale pour chaque acte. Une garantie exprimée à « 200 % » rembourse jusqu'à deux fois ce tarif, part de la Sécurité sociale comprise."),
    ("Dépassement d'honoraires", "Part du prix d'une consultation ou d'un acte qui dépasse la base de remboursement. Elle n'est jamais remboursée par la Sécurité sociale ; la mutuelle peut la couvrir selon le niveau de garantie."),
    ("Reste à charge", "Ce que le salarié paie de sa poche une fois la Sécurité sociale et la mutuelle intervenues."),
    ("Tiers payant", "Système qui évite au salarié d'avancer les frais : le professionnel de santé est payé directement par la Sécurité sociale et la mutuelle."),
    ("Décision unilatérale de l'employeur", "Écrit par lequel l'employeur met en place la mutuelle ou la prévoyance : salariés concernés, garanties, répartition de la cotisation, dispenses. Il doit être remis à chaque salarié, avec une preuve de remise."),
    ("Dispense d'affiliation", "Possibilité, pour certains salariés, de refuser la mutuelle de l'entreprise : contrat court, salarié déjà couvert par ailleurs, temps très partiel. La demande doit être écrite, signée et conservée par l'employeur."),
    ("Versement santé", "Aide versée par l'employeur à certains salariés en contrat court ou à temps très partiel qui ne sont pas couverts par la mutuelle de l'entreprise, pour financer leur contrat individuel."),
    ("Portabilité", "Maintien gratuit de la mutuelle et de la prévoyance pour l'ancien salarié indemnisé par l'assurance chômage, pendant une durée égale à son dernier contrat, dans la limite de 12 mois."),
    ("Plafond de la Sécurité sociale", "Montant de référence revu chaque année : 4 005 € par mois et 48 060 € par an en 2026. Il sert à calculer de nombreuses cotisations et garanties."),
    ("Tranche A", "Partie du salaire comprise entre 0 et le plafond mensuel de la Sécurité sociale, soit jusqu'à 4 005 € par mois en 2026. Aussi appelée tranche 1."),
    ("Prévoyance des cadres (1,50 %)", "Obligation nationale : l'employeur doit financer seul, pour chaque cadre, une prévoyance d'au moins 1,50 % de la tranche A du salaire, affectée en priorité au risque décès. À défaut, il peut devoir verser lui-même trois plafonds annuels (144 180 € en 2026) en cas de décès."),
    ("Maintien de salaire", "Obligation de l'employeur de compléter les indemnités de la Sécurité sociale pendant un arrêt de travail, sous conditions d'ancienneté et pour une durée limitée, selon la loi et la convention collective."),
    ("Incapacité de travail", "Arrêt de travail temporaire. La prévoyance verse des indemnités journalières qui complètent celles de la Sécurité sociale, souvent après la période de maintien de salaire."),
    ("Invalidité", "Réduction durable de la capacité de travail, reconnue par la Sécurité sociale. La prévoyance verse alors une rente qui complète la pension d'invalidité."),
    ("Capital décès", "Somme versée aux bénéficiaires désignés par le salarié s'il décède. Elle s'exprime en pourcentage du salaire annuel."),
    ("Rente éducation", "Rente versée aux enfants d'un salarié décédé, jusqu'à la fin de leurs études, pour financer leur éducation."),
    ("Franchise", "Nombre de jours d'arrêt à partir duquel la prévoyance commence à verser ses indemnités. Elle doit être calée sur la fin du maintien de salaire, pour éviter un trou de revenu."),
    ("Forfait social", "Contribution de 8 % due par les entreprises de 11 salariés et plus sur la part employeur des cotisations de mutuelle et de prévoyance."),
    ("Assureur recommandé par la branche", "Organisme que les partenaires sociaux d'une branche conseillent pour appliquer la convention. L'employeur reste libre d'en choisir un autre, à condition d'offrir des garanties au moins équivalentes."),
    ("Structure de cotisation", "Façon de répartir le prix de la mutuelle : tarif unique, « isolé / famille » ou « adulte / enfant ». Elle change fortement ce que paient l'employeur et chaque salarié."),
    ("Comptes de résultats", "Document annuel qui compare les cotisations versées et les remboursements payés par l'assureur. Il sert de base pour négocier le tarif à l'échéance."),
    ("Catégories objectives", "Critères autorisés pour proposer des garanties différentes selon les salariés, par exemple cadres et non-cadres, sans perdre les exonérations sociales."),
    ("Courtier en assurance", "Professionnel indépendant, immatriculé à l'ORIAS, qui représente son client et non un assureur. Il compare plusieurs contrats, conseille et accompagne l'entreprise pendant la vie du contrat."),
    ("Travailleur non salarié (TNS)", "Dirigeant affilié à la Sécurité sociale des indépendants, par exemple un gérant majoritaire de SARL. Il n'est pas couvert par le contrat des salariés et doit souscrire sa propre mutuelle et sa propre prévoyance, déductibles sous conditions (contrats « Madelin »)."),
]


def lexique_main(href):
    import unicodedata
    items = sorted(LEXIQUE, key=lambda x: unicodedata.normalize("NFKD", x[0]).lower())
    dl = "".join(f'<div class="bx-term" id="{_slug(t)}"><dt>{t}</dt><dd>{d}</dd></div>' for t, d in items)
    return f"""<main id="contenu">
<section class="page-hero bg-cream">
  <div class="wrap" style="grid-template-columns:minmax(0,1fr)">
    <div>
      <span class="crumb"><a href="{href('index')}">Accueil</a> · Lexique</span>
      <h1 class="kw-h1">Lexique de la mutuelle et de la prévoyance d'entreprise</h1>
      <p class="lead">Les {len(items)} mots qu'un employeur rencontre dans son contrat, expliqués en langage clair, avec les chiffres de 2026.</p>
    </div>
  </div>
</section>
<section class="band bg-cream" style="padding-top:36px">
  <div class="wrap narrow">
    <label class="bx-lex-search"><span>Chercher un mot</span><input type="text" data-lex placeholder="Portabilité, dispense, tranche A…" autocomplete="off"></label>
    <dl class="bx-lex">{dl}</dl>
    <p class="bx-lex-empty" hidden>Aucun mot ne correspond. Posez-nous la question : nous répondons sous 24 h ouvrées.</p>
    <p style="margin-top:28px"><a class="btn btn-red" href="{href('devis')}">Poser ma question à un conseiller</a></p>
  </div>
</section>
</main>
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


MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]


def _date_fr(iso):
    y, mo, d = iso.split("-")
    return f"{int(d)}{'er' if int(d) == 1 else ''} {MOIS[int(mo) - 1]} {y}"


def build_guides(out, mode, idx, t0, d0, ft):
    """Guides de fond : pages bâties sur le gabarit d'un article du blog, plus une page sommaire /guides."""
    arts = sorted(glob.glob(os.path.join(out, "blog", "*.html")))
    if not arts:
        return []
    sh = open(arts[0], encoding="utf-8").read()
    old_slug = os.path.basename(arts[0])[:-5]
    old_full = re.search(r"<title>(.*?)</title>", sh, re.S).group(1)
    old_head = re.search(r'<h1 class="art-h1">(.*?)</h1>', sh, re.S).group(1)
    old_desc = re.search(r'<meta name="description" content="(.*?)">', sh).group(1)
    href = (lambda x: f"../{x}.html") if mode == "preview" else (lambda x: "/" if x == "index" else f"/{x}")
    obs = sorted(glob.glob(os.path.join(out, "obligations*.html")))
    ob = href(os.path.basename(obs[0])[:-5]) if obs else href("index")
    os.makedirs(os.path.join(out, "guides"), exist_ok=True)
    made = []
    pub = getattr(CFG, "GUIDE_PUB", "") or CFG.PUBLIC
    for g in GD.GUIDES:
        title = g["title"].format(pub=pub)
        body = g["body"].format(pub=pub, conv=CFG.CONVENTION, ob=ob)
        faq = "".join(f"<h3>{q}</h3><p>{a}</p>" for q, a in g["faq"])
        body += f"<h2>Questions fréquentes</h2>{faq}"
        mins = max(3, round(len(_txt(body).split()) / 210))
        h = sh.replace(f"assets/og/{old_slug}.png", "assets/og-default.png")
        h = h.replace(old_full, _html.escape(f"{title} · {CFG.BRAND}", quote=True)).replace(old_head, _html.escape(title, quote=False))
        h = h.replace(old_desc, _html.escape(g["desc"], quote=True))
        h = h.replace(f"/blog/{old_slug}", f"/guides/{g['slug']}")
        h = re.sub(r'<span class="crumb">.*?</span>', f'<span class="crumb"><a href="{href("index")}">Accueil</a> · <a href="{href("guides")}">Guides</a> · {g["cat"]}</span>', h, count=1, flags=re.S)
        h = re.sub(r'(<h1 class="art-h1">.*?</h1>\s*)<p class="lead"[^>]*>.*?</p>',
                   lambda m: m.group(1) + f'<p class="lead" style="margin-top:14px">Mis à jour le {_date_fr(GD.MAJ)} · {mins} min de lecture · Par WealthWise Conseil</p>', h, count=1, flags=re.S)
        mk = '<div class="wrap narrow prose article">'
        i = h.index(mk) + len(mk); j = h.index('<div class="author-box">', i)
        h = h[:i] + "\n" + body + "\n    " + h[j:]
        url = f"{CFG.DOMAIN}/guides/{g['slug']}"
        ld = {"@context": "https://schema.org", "@graph": [
            {"@type": "Article", "headline": title, "description": g["desc"], "datePublished": GD.MAJ, "dateModified": GD.MAJ, "inLanguage": "fr-FR",
             "mainEntityOfPage": url, "author": AUTHOR, "image": f"{CFG.DOMAIN}/assets/og-default.png",
             "publisher": {"@type": "Organization", "name": "WealthWise Conseil", "url": WWC + "/"}},
            {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in g["faq"]]}]}
        h = re.sub(r'<script type="application/ld\+json">.*?</script>', lambda m: '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + "</script>", h, count=1, flags=re.S)
        open(os.path.join(out, "guides", g["slug"] + ".html"), "w", encoding="utf-8").write(h)
        made.append((g, title))
    # page sommaire
    h0 = (lambda x: f"{x}.html") if mode == "preview" else (lambda x: "/" if x == "index" else f"/{x}")
    gt = f"Guides de l'employeur : mutuelle et prévoyance d'entreprise · {CFG.BRAND}"
    gd = "Mise en place, dispenses, changement de contrat, prévoyance obligatoire, coût réel : les guides complets pour les employeurs, à jour des chiffres 2026."
    hd = idx[:idx.index("<main")].replace(t0, _html.escape(gt, quote=True)).replace(d0, _html.escape(gd, quote=True))
    hd = hd.replace(f'<link rel="canonical" href="{CFG.DOMAIN}/">', f'<link rel="canonical" href="{CFG.DOMAIN}/guides">')
    hd = hd.replace(f'<meta property="og:url" content="{CFG.DOMAIN}/">', f'<meta property="og:url" content="{CFG.DOMAIN}/guides">').replace(' aria-current="page"', "")
    ld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": gt, "url": CFG.DOMAIN + "/guides", "inLanguage": "fr-FR",
          "hasPart": [{"@type": "Article", "headline": t, "url": f"{CFG.DOMAIN}/guides/{g['slug']}"} for g, t in made]}
    hd = re.sub(r'<script type="application/ld\+json">.*?</script>', lambda m: '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + "</script>", hd, count=1, flags=re.S)
    gpre = "guides/" + "{}" + (".html" if mode == "preview" else "")
    cards = "".join(f'<a class="rule bx-guide" href="{("/" if mode != "preview" else "") + gpre.format(g["slug"])}"><span class="tag">{g["cat"]}</span><h3>{t}</h3><p>{g["desc"]}</p></a>' for g, t in made)
    main = f"""<main id="contenu">
<section class="page-hero bg-cream">
  <div class="wrap" style="grid-template-columns:minmax(0,1fr)">
    <div>
      <span class="crumb"><a href="{h0('index')}">Accueil</a> · Guides</span>
      <h1 class="kw-h1">Guides de l'employeur : mutuelle et prévoyance d'entreprise</h1>
      <p class="lead">Les questions que se posent les employeurs {getattr(CFG, "GUIDE_PUB", "") or CFG.PUBLIC}, traitées à fond : étapes, documents, délais et chiffres 2026. Rédigés par un courtier, relus à chaque changement de barème.</p>
    </div>
  </div>
</section>
<section class="band bg-cream" style="padding-top:36px">
  <div class="wrap"><div class="rules bx-guides">{cards}</div>
  <p style="margin-top:30px"><a class="btn btn-red" href="{h0('devis')}">Poser ma question à un conseiller</a></p></div>
</section>
</main>
"""
    open(os.path.join(out, "guides.html"), "w", encoding="utf-8").write(hd + main + ft)
    return made


def guides_home_block(made, mode):
    if not made:
        return ""
    u = (lambda sl: f"guides/{sl}.html") if mode == "preview" else (lambda sl: f"/guides/{sl}")
    hub = "guides.html" if mode == "preview" else "/guides"
    cards = "".join(f'<a class="rule bx-guide" href="{u(g["slug"])}"><span class="tag">{g["cat"]}</span><h3>{t}</h3><p>{g["desc"]}</p></a>' for g, t in made[:4])
    return f"""<section class="band bg-cream2" id="guides">
  <div class="wrap">
    <div class="sec-head"><span class="t-label">Guides de l'employeur</span><h2>Les réponses complètes aux questions que vous vous posez</h2><p>Des guides de fond, à jour des chiffres 2026, pour décider en connaissance de cause.</p></div>
    <div class="rules bx-guides">{cards}</div>
    <p style="margin-top:26px"><a class="btn btn-navy" href="{hub}">Voir tous les guides</a></p>
  </div>
</section>
"""


# ------------------------------------------------------------------ traitement d'une page
def process(path, slug, mode, versions, made=()):
    h = open(path, encoding="utf-8").read()
    depth = slug.count("/")
    pre = "../" * depth if mode == "preview" else "/"
    href = (lambda s: f"{pre}{s}.html") if mode == "preview" else (lambda s: "/" if s == "index" else f"/{s}")
    is_art = slug.startswith("blog/") or slug.startswith("guides/")
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
                     ("source-serif-4-latin-wght-normal.woff2", "figtree-latin-wght-normal.woff2"))
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

    if getattr(CFG, "LOGO", ""):
        h = re.sub(r'<svg class="logo-mark"[^>]*>.*?</svg>', lambda m: logo_svg(versions["logo_bg"], versions["accent"], dark=versions["navy"], sec=versions["sec"]), h, flags=re.S)

    if CFG.THEME == "v2":
        h = re.sub(r'(<span class="brand-name">)(.*?)(</span>)', lambda m: m.group(1) + (CFG.BRAND if _txt(m.group(2)).isupper() else m.group(2)) + m.group(3), h, flags=re.S)

    # H1 porteur du mot-clé sur les pages intérieures ; l'ancien titre devient le slogan
    if not is_art and slug not in ("index", "mentions-legales", "a-propos", "lexique", "guides"):
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
        cb = guides_home_block(made, mode) + cases_block() + situations_block() + compare_block()
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
        if slug.startswith("guides/"): crumbs.append(("Guides", CFG.DOMAIN + "/guides"))
        elif is_art: crumbs.append(("Blog", CFG.DOMAIN + "/blog"))
        crumbs.append((re.sub(r"\s*·\s*[^·]+$", "", title), CFG.DOMAIN + "/" + slug))
        extra.append({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(crumbs)]})
    h = h.replace("</head>", "".join('<script type="application/ld+json">' + json.dumps(e, ensure_ascii=False) + "</script>\n" for e in extra) + "</head>", 1)

    # pied de page : lien « Qui sommes-nous » ; barre d'appel sur mobile
    ml = re.search(r'<li><a href="([^"]*mentions-legales[^"]*)">', h)
    if ml and "Qui sommes-nous</a></li>" not in h:
        h = h.replace(ml.group(0), f'<li><a href="{href("a-propos")}">Qui sommes-nous</a></li><li><a href="{href("guides")}">Guides</a></li><li><a href="{href("lexique")}">Lexique</a></li>' + ml.group(0), 1)
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
    accent = (tk.get("mustard") if CFG.THEME == "v2" else None) or "#F4C24B"
    if _lum(_hex(accent)) < .35: accent = "#F4C24B"
    logo_bg = tk.get(getattr(CFG, "LOGO_BG", "red"), navy) if CFG.THEME == "v2" else navy
    versions = {"css": _hash(css), "js": _hash(js), "navy": navy, "accent": accent, "logo_bg": logo_bg}
    versions["sec"] = (tk.get("red") if getattr(CFG, "LOGO_BG", "red") == "teal" else tk.get("teal")) if CFG.THEME == "v2" else "#11A39B"
    if getattr(CFG, "LOGO", ""):
        open(os.path.join(out, "assets", "favicon.svg"), "w").write(logo_svg(logo_bg, accent, "", ' xmlns="http://www.w3.org/2000/svg"', dark=navy, sec=versions["sec"]))
        for f in glob.glob(os.path.join(BX, "icons", "*")):
            shutil.copy(f, os.path.join(out, "favicon.ico") if f.endswith(".ico") else os.path.join(out, "assets", os.path.basename(f)))

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

    lx_t = f"Lexique mutuelle et prévoyance d'entreprise : {len(LEXIQUE)} définitions · {CFG.BRAND}"
    lx_d = "Portabilité, dispense, tranche A, contrat responsable, versement santé : les mots de la mutuelle et de la prévoyance d'entreprise expliqués simplement, chiffres 2026."
    hl = idx[:idx.index("<main")].replace(t0, _html.escape(lx_t, quote=True)).replace(d0, _html.escape(lx_d, quote=True))
    hl = hl.replace(f'<link rel="canonical" href="{CFG.DOMAIN}/">', f'<link rel="canonical" href="{CFG.DOMAIN}/lexique">')
    hl = hl.replace(f'<meta property="og:url" content="{CFG.DOMAIN}/">', f'<meta property="og:url" content="{CFG.DOMAIN}/lexique">').replace(' aria-current="page"', "")
    lld = {"@context": "https://schema.org", "@type": "DefinedTermSet", "name": "Lexique de la mutuelle et de la prévoyance d'entreprise", "url": CFG.DOMAIN + "/lexique", "inLanguage": "fr-FR",
           "hasDefinedTerm": [{"@type": "DefinedTerm", "name": t, "description": d, "url": CFG.DOMAIN + "/lexique#" + _slug(t)} for t, d in LEXIQUE]}
    hl = re.sub(r'<script type="application/ld\+json">.*?</script>', lambda m: '<script type="application/ld+json">' + json.dumps(lld, ensure_ascii=False) + "</script>", hl, count=1, flags=re.S)
    open(os.path.join(out, "lexique.html"), "w", encoding="utf-8").write(hl + lexique_main(href0) + ft)

    made = build_guides(out, mode, idx, t0, d0, ft)

    # 3. toutes les pages
    pages = []
    for p in sorted(glob.glob(os.path.join(out, "**", "*.html"), recursive=True)):
        slug = os.path.relpath(p, out)[:-5].replace(os.sep, "/")
        pages.append((slug,) + process(p, slug, mode, versions, made))

    if mode != "deploy":
        return
    # 4. robots.txt ouvert aux robots d'IA, plan du site, llms.txt
    robots = "User-agent: *\nAllow: /\n\n# Robots des assistants d'IA : bienvenue, le contenu peut être lu et cité.\n"
    robots += "".join(f"User-agent: {b}\nAllow: /\n\n" for b in AI_BOTS) + f"Sitemap: {CFG.DOMAIN}/sitemap.xml\n"
    open(os.path.join(out, "robots.txt"), "w").write(robots)
    sm_p = os.path.join(out, "sitemap.xml")
    if os.path.exists(sm_p):
        sm = open(sm_p).read()
        if "/guides<" not in sm:
            sm = sm.replace("</urlset>", f"  <url><loc>{CFG.DOMAIN}/guides</loc><lastmod>{GD.MAJ}</lastmod></url>\n" + "".join(
                f"  <url><loc>{CFG.DOMAIN}/guides/{g['slug']}</loc><lastmod>{GD.MAJ}</lastmod></url>\n" for g, _ in made) + "</urlset>")
            open(sm_p, "w").write(sm)
        if "/lexique<" not in sm:
            sm = sm.replace("</urlset>", f"  <url><loc>{CFG.DOMAIN}/lexique</loc><lastmod>2026-11-13</lastmod></url>\n</urlset>")
            open(sm_p, "w").write(sm)
        if "/a-propos<" not in sm:
            lm = (re.findall(r"<lastmod>([\d-]+)</lastmod>", sm) or ["2026-11-13"])[0]
            sm = sm.replace("</urlset>", f"  <url><loc>{CFG.DOMAIN}/a-propos</loc><lastmod>{max(lm, '2026-11-13')}</lastmod></url>\n</urlset>")
            open(sm_p, "w").write(sm)
    url = lambda s: CFG.DOMAIN + ("/" if s == "index" else "/" + s)
    clean = lambda t: re.sub(r"\s*·\s*[^·]+$", "", t)
    fixed = [p for p in pages if not p[0].startswith("blog/") and not p[0].startswith("guides/") and p[0] not in ("mentions-legales", "index", "blog", "devis")]
    arts = [p for p in pages if p[0].startswith("guides/")] + [p for p in pages if p[0].startswith("blog/")]
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
