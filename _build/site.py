# Identité et textes communs du site Bonne Cordée (mutuelle-savoie.fr).
# Exécuté par build.py : les fonctions L(), A(), check() et photo() du moteur sont disponibles.
DOMAIN = "https://www.mutuelle-savoie.fr"
BRAND = "Bonne Cordée"
SITE_SLUG = "bonne-cordee"
SITE_BRAND_HTML = "Bonne Cordée"
SITE_BRAND_SHORT = "Bonne Cordée"
SITE_BRAND_SUB = "Le courtier des entreprises de montagne"
SITE_DOMAIN_TXT = "mutuelle-savoie.fr"
LASTMOD = "2026-11-11"
INSURERS = [("malakoff-humanis", "Malakoff Humanis"), ("ag2r-la-mondiale", "AG2R La Mondiale"), ("apicil", "Apicil"), ("harmonie-mutuelle", "Harmonie Mutuelle"),
            ("swiss-life", "Swiss Life"), ("april", "APRIL"), ("generali", "Generali"), ("klesia", "Klesia"),
            ("alptis", "Alptis"), ("axa", "AXA"), ("mma", "MMA"), ("matmut", "Matmut")]
NAV = [("saisonniers", "Saisonniers"), ("hotels-restaurants", "Hôtels & restaurants"), ("remontees-mecaniques", "Remontées"),
       ("moniteurs-independants", "Indépendants"), ("obligations-montagne", "Obligations"), ("outils", "Outils"), ("blog", "Blog")]

INK, ACCENT, PINE, PAPER, SKY, PEACH = "#1B2A41", "#C8102E", "#2F5D50", "#F7F9FB", "#DCE8F2", "#F2D27A"
SITE_THEME = "#F7F9FB"
SITE_FONTS_LINK = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap">'

SITE_ICONS = f"""<symbol id="i-peak" viewBox="0 0 64 64"><path d="M4 56L24 18l10 16 8-10 18 32Z" fill="{SKY}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/><path d="M17 31l7-13 7 11-4 4-3-3-3 3Z" fill="{PAPER}" stroke="{INK}" stroke-width="2.4" stroke-linejoin="round"/><path d="M52 6v8M48 10h8" stroke="{ACCENT}" stroke-width="2.6" stroke-linecap="round"/></symbol>
<symbol id="i-chalet" viewBox="0 0 64 64"><path d="M6 32L32 10l26 22" fill="none" stroke="{INK}" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/><path d="M12 28v28h40V28" fill="{PEACH}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/><path d="M8 30L32 12l24 18" fill="none" stroke="{PAPER}" stroke-width="2"/><rect x="27" y="40" width="10" height="16" fill="{ACCENT}" stroke="{INK}" stroke-width="2.6"/><rect x="17" y="34" width="7" height="7" fill="{SKY}" stroke="{INK}" stroke-width="2.4"/><rect x="40" y="34" width="7" height="7" fill="{SKY}" stroke="{INK}" stroke-width="2.4"/></symbol>
<symbol id="i-lift" viewBox="0 0 64 64"><path d="M4 12l56 12" stroke="{INK}" stroke-width="3" stroke-linecap="round"/><path d="M32 18v14" stroke="{INK}" stroke-width="3" stroke-linecap="round"/><path d="M18 32h28v10c0 6-4 10-10 10h-8c-6 0-10-4-10-10Z" fill="{ACCENT}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/><path d="M22 40h20" stroke="{PAPER}" stroke-width="3" stroke-linecap="round"/><path d="M54 40v8M50 44h8" stroke="{PEACH}" stroke-width="2.6" stroke-linecap="round"/></symbol>
<symbol id="i-rope" viewBox="0 0 64 64"><g stroke="{INK}" stroke-width="2.6" stroke-linecap="round"><path d="M14 10l36 44M50 10L14 54" stroke="{INK}" stroke-width="2"/></g><g transform="rotate(-38 32 32)"><rect x="28" y="4" width="8" height="56" rx="4" fill="{ACCENT}" stroke="{INK}" stroke-width="2.6"/><path d="M28 10c0-6 8-6 8 0" fill="{ACCENT}"/></g><g transform="rotate(38 32 32)"><rect x="28" y="4" width="8" height="56" rx="4" fill="{PAPER}" stroke="{INK}" stroke-width="2.6"/></g><circle cx="32" cy="32" r="5" fill="{PEACH}" stroke="{INK}" stroke-width="2.4"/></symbol>"""

SITE_CTA_TITLE = "Votre entreprise de montagne est-elle vraiment bien couverte ?"
SITE_FOOT_ABOUT = "mutuelle et prévoyance collectives pour les entreprises de montagne de Savoie et Haute-Savoie : hôtels, restaurants, remontées mécaniques, commerces de station, saisonniers"
SITE_FOOT_METIER = [("saisonniers", "Saisonniers"), ("hotels-restaurants", "Hôtels et restaurants de station"), ("remontees-mecaniques", "Remontées mécaniques"),
                    ("moniteurs-independants", "Moniteurs et indépendants"), ("dirigeants", "Dirigeants")]
SITE_FOOT_GUIDES = [("obligations-montagne", "Obligations des entreprises de montagne")]
SITE_WWC_CCN = ("ccn-hcr-protection-sociale-saisonniers-extras", "Le guide des saisonniers sur wealthwiseconseil.fr")
SITE_INDEP = "sans lien avec les organisations professionnelles de la montagne, les branches concernées ni les organismes qu'elles recommandent."
SITE_INDEP_MENTIONS = "Il n'est ni un organisme de branche, ni une organisation professionnelle, et n'a aucun lien avec les organisations patronales ou syndicales, les stations ou les exploitants cités."
SITE_TYPES = ["Hôtel ou résidence", "Restaurant, bar", "Remontées mécaniques", "Location, magasin de sport", "École, moniteur", "Autre commerce de station"]
SITE_BESOINS = ["Mutuelle + prévoyance", "Mutuelle seule", "Prévoyance seule", "Audit de mon contrat", "Ma protection de dirigeant"]
SITE_EFFECTIFS = ["1 à 2", "3 à 5", "6 à 10", "11 à 20", "21 à 50", "Plus de 50", "Aucun pour l'instant (création)"]
SITE_LEGEND = "Votre entreprise"
SITE_ETAB = "Entreprise"
SITE_PH = ["73120", "Claire Perrier", "Hôtel Le Belvédère", "contact@hotel-belvedere.fr"]
SITE_DONE_TXT = "Gardez sous la main votre contrat actuel, la liste de vos salariés (permanents et saisonniers) et un bulletin de paie si vous en avez."
SITE_INSURERS_TXT = "en vérifiant le respect des garanties de votre branche."
SITE_WWC_MARQUE = "montagne"
SITE_ALT_NAME = "Bonne Cordée, le courtier des entreprises de montagne"
SITE_ORG_DESC = "Courtier en mutuelle et prévoyance collectives pour les entreprises de montagne de Savoie et Haute-Savoie : hôtels et restaurants de station (IDCC 1979), remontées mécaniques et domaines skiables (IDCC 454), commerces de station, saisonniers, moniteurs indépendants."
SITE_BLOG = ("Le blog de la cordée",
             "Des guides courts et concrets pour les entreprises de montagne, rédigés par l'équipe de WealthWise Conseil.",
             "i-peak",
             "Blog mutuelle et prévoyance des entreprises de montagne",
             "Guides pratiques pour hôtels, restaurants, remontées mécaniques et commerces de station : saisonniers, versement santé, portabilité, prévoyance, protection des dirigeants.")
SITE_TEMOIGNAGES = []

PHOTO_STRIP = [("1550503736-c1a2c9033c03", "Chalets en bois dans une station de montagne", "À l'hôtel", "Réceptionnistes, cuisiniers, femmes de chambre : saisonniers et permanents, chacun ses règles."),
               ("1775642126954-a918219028ed", "Télésiège montant une pente enneigée", "Sur le domaine", "Perchmans, pisteurs, conducteurs : une prévoyance de branche recommandée depuis 2026."),
               ("1735441984733-3dd209fd2fc0", "Rue enneigée d'une station de ski", "En station", "Magasins, écoles, commerces : une saison courte, des obligations qui ne le sont pas.")]
PHOTO_STRIP_TITLE = "De la vallée au sommet, chaque saisonnier compte"
PHOTO_STRIP_TEXT = "Un saisonnier qui se blesse en février, un cadre sans prévoyance, un CDD sans mutuelle : en montagne, la saison est courte mais les risques sont réels. Nous vérifions que toute l'équipe est couverte."


def site_posters():
    return f"""<div class="posters">
  <a class="poster bg-mustard" href="{L('saisonniers')}">
    <div class="p-head"><svg class="ill" aria-hidden="true"><use href="#i-rope"/></svg><span class="s">Une saison courte.</span><span class="b">Une couverture<br>solide.</span><span class="sc">Saisonniers</span><span class="c">et CDD.</span></div>
    <span class="go">Saisonniers →</span></a>
  <a class="poster bg-red" href="{L('hotels-restaurants')}">
    <div class="p-head"><svg class="ill" aria-hidden="true"><use href="#i-chalet"/></svg><span class="s" style="color:var(--mustard)">Hôtels,</span><span class="b relief-cream">restaurants,<br>bars d'altitude :</span><span class="sc" style="color:var(--mustard)">toute</span><span class="c relief-cream">l'équipe.</span></div>
    <span class="go" style="color:var(--cream)">Hôtels & restaurants →</span></a>
  <a class="poster bg-navy on-navy" href="{L('remontees-mecaniques')}">
    <div class="p-head"><svg class="ill" aria-hidden="true"><use href="#i-lift"/></svg><span class="s" style="color:var(--mustard)">Remontées mécaniques&nbsp;?</span><span class="b relief-cream">Une branche,<br>ses règles.</span><span class="sc" style="color:var(--mustard)">Prévoyance</span><span class="c relief-cream">2026.</span></div>
    <span class="go" style="color:var(--cream)">Remontées →</span></a>
  <a class="poster bg-teal" href="{L('moniteurs-independants')}">
    <div class="p-head"><svg class="ill" aria-hidden="true"><use href="#i-peak"/></svg><span class="s" style="color:var(--mustard)">Moniteur, guide&nbsp;?</span><span class="b relief-cream">Votre revenu<br>aussi.</span><span class="sc" style="color:var(--mustard)">Indépendants</span><span class="c relief-cream">sur mesure.</span></div>
    <span class="go" style="color:var(--cream)">Indépendants →</span></a>
</div>"""
