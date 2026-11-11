# Pages du site Bonne Cordée (exécuté par build.py, qui fournit les fonctions du moteur).
# Sources : service-public (complémentaire santé, versement santé 2026) ; convention HCR (IDCC 1979) ;
# convention des remontées mécaniques et domaines skiables (IDCC 454) : APICIL prévoyance + OCIRP recommandés
# depuis le 1er janvier 2026, grilles APICIL cadres au 1er juillet 2025, avenant n° 87 du 27 octobre 2025 (saisonniers).

TEL = '<a href="tel:+33187667031" style="font-weight:700;color:inherit">01 87 66 70 31</a>'
SP = "https://entreprendre.service-public.gouv.fr/vosdroits/F33754"
APICIL_RM = "https://pro.apicil.com/accord-branche/ccn-remontees-mecaniques-domaines-skiables/"
APICIL_RM_G = "https://pro.apicil.com/wp-content/uploads/sites/3/2025/05/CCN-rmds-prevoyance-garanties-c-2025.pdf"
APICIL_RM_C = "https://pro.apicil.com/wp-content/uploads/sites/3/2025/05/CCN-rmds-prevoyance-cotisations-c-2025.pdf"
AV87 = "https://presse.tripalio.fr/wp-content/uploads/2025/12/IDCC-454-Avenant-contrats-saisonniers.pdf"


def page_meta(headline):
    return {"@type": "Article", "headline": headline, "datePublished": "2026-11-11", "dateModified": "2026-11-11",
            "author": {"@type": "Organization", "name": "WealthWise Conseil"}, "publisher": {"@type": "Organization", "name": SITE_BRAND_HTML}}


def cta_inline(txt, btn="Faire comparer mon contrat"):
    return f"""<div class="callout" style="border-left-color:var(--red);display:flex;flex-wrap:wrap;gap:14px;align-items:center;justify-content:space-between"><span><strong>{txt}</strong></span><a class="btn btn-red btn-sm" href="{L('devis')}">{btn}</a></div>"""


def value_block(prix_txt):
    return f"""<section class="band bg-navy on-navy" id="avec-nous">
  <div class="wrap">
    <div class="sec-head" style="max-width:52em"><span class="t-label">Avec Bonne Cordée</span><h2 class="relief-red">Ce que vous gagnez à nous confier votre dossier</h2><p>{prix_txt}</p></div>
    <div class="rules" style="color:var(--ink)">
      <div class="rule"><span class="tag">votre budget</span><span class="num">15+</span><h3>Assureurs mis en concurrence</h3><p>Assureurs recommandés compris. Pour chaque offre : le montant par salarié, la part employeur, le coût annuel, et l'écart avec votre contrat actuel, en euros.</p></div>
      <div class="rule"><span class="tag">votre sécurité</span><h3>Zéro risque employeur</h3><p>Si votre contrat est en dessous des garanties de votre convention, c'est vous qui payez la différence en cas de décès, d'invalidité ou d'arrêt long. Nous vérifions chaque ligne avant de signer.</p></div>
      <div class="rule"><span class="tag">votre temps</span><h3>Zéro paperasse</h3><p>Entrées et sorties de saison, dispenses, versement santé, portabilité entre deux saisons : nous gérons tout.</p></div>
      <div class="rule"><span class="tag">vos équipes</span><span class="num">15 min</span><h3>Une réponse sur WhatsApp</h3><p>Une ligne dédiée à vos salariés, réponse garantie en 15 minutes en semaine, et un conseiller qui suit les arrêts de travail avec l'assureur.</p></div>
    </div>
    <p style="margin-top:22px;color:var(--cream)"><strong>Combien ça coûte ?</strong> L'étude est gratuite et sans engagement. Si vous souscrivez par notre intermédiaire, notre rémunération est une commission incluse dans la cotisation, versée par l'assureur.</p>
    <p style="margin-top:14px"><a class="btn btn-red" href="{L('devis')}">Demander mon étude gratuite</a> <span style="margin-left:14px;color:var(--cream)">ou appelez le {TEL}</span></p>
  </div>
</section>"""


def steps_block():
    return """<section class="band bg-cream2">
  <div class="wrap">
    <div class="sec-head"><span class="t-label">Comment ça se passe</span><h2>Trois étapes, et vous n'avez plus à y penser</h2></div>
    <ol class="steps">
      <li><h3>Vous nous envoyez l'essentiel</h3><p>Le formulaire en 2 minutes, puis votre contrat actuel (tableau de garanties et tarif) et la liste des salariés. Pas de contrat ? On part de zéro.</p></li>
      <li><h3>On vous présente un comparatif chiffré</h3><p>Ce qui est conforme et ce qui ne l'est pas dans votre contrat actuel, puis les meilleures offres du marché, avec le coût employeur et salarié de chacune et notre recommandation.</p></li>
      <li><h3>Vous choisissez, on s'occupe du reste</h3><p>Mise en place, affiliations, dispenses, résiliation de l'ancien contrat, puis gestion au quotidien : vous gardez un seul interlocuteur.</p></li>
    </ol>
  </div>
</section>"""


def montagne_table():
    return f"""<section class="band bg-cream2">
  <div class="wrap">
    <div class="sec-head"><span class="t-label">Selon votre activité</span><h2>Quelle convention, quelles règles ?</h2><p>En station, chaque métier a sa convention collective, et ses propres règles de mutuelle et de prévoyance. Le numéro de convention (IDCC) figure sur vos bulletins de paie.</p></div>
    <div class="table-wrap"><table>
      <thead><tr><th>Activité</th><th>Convention</th><th>Prévoyance</th><th>Mutuelle</th></tr></thead>
      <tbody>
        <tr><td><strong>Hôtels, restaurants, bars, discothèques</strong></td><td>Hôtels, cafés, restaurants (IDCC 1979)</td><td>Non-cadres : 0,86 % de la tranche A, à parts égales</td><td>Obligatoire, au moins 50 % employeur</td></tr>
        <tr><td><strong>Remontées mécaniques, domaines skiables</strong></td><td>IDCC 454</td><td>Régime de branche ; APICIL et l'OCIRP recommandés depuis 2026</td><td>Obligatoire, au moins 50 % employeur</td></tr>
        <tr><td><strong>Magasins de sport, location de skis, autres commerces</strong></td><td>Selon l'activité principale</td><td>Selon la convention</td><td>Obligatoire, au moins 50 % employeur</td></tr>
        <tr><td><strong>Moniteurs, guides, indépendants</strong></td><td>Aucune (travailleurs indépendants)</td><td>Contrat individuel</td><td>Contrat individuel</td></tr>
        <tr><td><strong>Tous les cadres</strong></td><td>Accord national de 2017</td><td>1,50 % de la tranche A à la charge de l'employeur</td><td>—</td></tr>
      </tbody></table></div>
    <p class="fine" style="margin-top:10px">Plafond mensuel de la Sécurité sociale : 4 005 € en 2026. Les textes des conventions et les notices des assureurs font foi.</p>
  </div>
</section>"""



ALP_SCENE = """<svg class="alp-scene" viewBox="0 0 1440 560" preserveAspectRatio="xMidYMax slice" aria-hidden="true">
  <circle cx="1130" cy="190" r="92" fill="#F4B942"/>
  <path d="M0 380L150 250l90 70 140-160 120 110 110-90 160 150 130-120 170 140 140-110 230 170V560H0Z" fill="#7FA7D6"/>
  <path d="M0 430L210 220l120 110 180-200 170 170 120-90 190 180 160-140 290 230V560H0Z" fill="#DCE8F2"/>
  <path d="M330 330l180-200 52 58-30 10-22-14-30 40-34-6Z M680 300l120-90 64 61-34-4-30 22-38-15Z M1030 310l160-140 74 64-40 4-26 24-36-20-40 16Z" fill="#FFFFFF"/>
  <path d="M0 470c160-40 300-30 470 6s330 40 520 0 300-50 450-10V560H0Z" fill="#F5F8FB"/>
  <g fill="#1F4A3D">
    <path d="M70 486l22-58 22 58Z M108 492l18-46 18 46Z M1290 474l24-64 24 64Z M1334 482l18-46 18 46Z M1372 478l22-56 22 56Z"/>
  </g>
  <path d="M-20 120L1460 330" stroke="#12305A" stroke-width="3"/>
  <g fill="#C8102E" stroke="#12305A" stroke-width="3">
    <path d="M420 182v34M398 216h44v14a12 12 0 0 1-12 12h-20a12 12 0 0 1-12-12Z"/>
    <path d="M900 250v34M878 284h44v14a12 12 0 0 1-12 12h-20a12 12 0 0 1-12-12Z"/>
  </g>
</svg>"""

SKIS = """<svg class="alp-skis" viewBox="0 0 160 160" aria-hidden="true">
  <g stroke="#F5F8FB" stroke-width="5" stroke-linecap="round"><path d="M34 22l92 118"/><path d="M126 22L34 140"/></g>
  <circle cx="34" cy="132" r="9" fill="none" stroke="#F5F8FB" stroke-width="4"/><circle cx="126" cy="132" r="9" fill="none" stroke="#F5F8FB" stroke-width="4"/>
  <g transform="rotate(-30 80 80)"><path d="M70 6c0-6 20-6 20 0v146c0 4-20 4-20 0Z" fill="#C8102E" stroke="#12305A" stroke-width="4"/><path d="M70 6c2-10 18-10 20 0" fill="#C8102E" stroke="#12305A" stroke-width="4"/></g>
  <g transform="rotate(30 80 80)"><path d="M70 6c0-6 20-6 20 0v146c0 4-20 4-20 0Z" fill="#F5F8FB" stroke="#12305A" stroke-width="4"/></g>
  <rect x="64" y="64" width="32" height="32" rx="6" fill="#C8102E" stroke="#12305A" stroke-width="4"/>
  <path d="M80 70v20M70 80h20" stroke="#F5F8FB" stroke-width="5" stroke-linecap="round"/>
</svg>"""

RIDGE = '<svg class="alp-ridge" viewBox="0 0 1440 60" preserveAspectRatio="none" aria-hidden="true"><path d="M0 60L120 22l70 26 110-40 90 30 130-36 100 34 120-28 110 24 140-34 110 30 120-22 120 32V60Z" fill="currentColor"/></svg>'


# ---------------------------------------------------------------- ACCUEIL
HOME_FAQ = [
    ("Un saisonnier doit-il avoir la mutuelle de l'entreprise ?", "Oui, en principe dès l'embauche, avec au moins 50 % de la cotisation payés par l'employeur. Un saisonnier en contrat de moins de 3 mois peut demander une dispense s'il a déjà une mutuelle individuelle responsable : l'employeur lui verse alors un « versement santé »."),
    ("Combien coûte le versement santé en 2026 ?", "Il correspond à ce que l'employeur aurait payé pour la mutuelle, multiplié par 125 % pour un CDD. Si ce montant n'est pas connu, la référence 2026 est de 22,27 € par mois pour un temps plein, soit 27,84 € pour un CDD, au prorata des heures."),
    ("Mon saisonnier garde-t-il sa mutuelle entre deux saisons ?", "Oui, s'il est indemnisé par l'assurance chômage : la portabilité le couvre gratuitement pendant la durée de son contrat, dans la limite de 12 mois, jusqu'à ce qu'il retrouve un emploi."),
    ("Vous êtes en Savoie ?", "WealthWise Conseil accompagne les entreprises de montagne de Savoie et Haute-Savoie à distance : téléphone, visio, WhatsApp, avec un conseiller dédié qui connaît les conventions des stations."),
    ("Combien coûte votre accompagnement ?", "L'étude et le comparatif sont gratuits et sans engagement. Si vous souscrivez par notre intermédiaire, notre rémunération est une commission incluse dans la cotisation, versée par l'assureur."),
    ("Mes saisonniers peuvent-ils vous contacter directement ?", "Oui, sur une ligne WhatsApp dédiée, avec une réponse garantie en 15 minutes du lundi au vendredi de 9 h à 19 h, même en pleine saison."),
]

PAGES["index"] = (
    "Mutuelle entreprise en Savoie : stations, hôtels, saisonniers · Bonne Cordée",
    "Courtier mutuelle et prévoyance pour les entreprises de montagne en Savoie et Haute-Savoie : hôtels, restaurants, remontées mécaniques, saisonniers, versement santé. Étude gratuite.",
    {"@context": "https://schema.org", "@graph": [ORG_LD, faq_ld(HOME_FAQ)]},
    "",
    f"""<section class="hero hero-alp">
  {ALP_SCENE}
  <div class="wrap">
    <div class="hero-copy">
      <svg class="alp-skis" viewBox="0 0 64 60" aria-hidden="true">{mark_inner(True)}</svg>
      <span class="kicker">Savoie et Haute-Savoie</span>
      <h1 class="hero-h1"><span class="l1">Courtier en mutuelle et prévoyance pour les entreprises de montagne</span>
      <span class="l2">Une saison courte.<br>Une couverture solide.</span>
      <span class="l3">Hôtels, remontées mécaniques, saisonniers.</span></h1>
      <p class="hero-lead">En station, tout se joue en quelques mois : des dizaines de saisonniers à affilier, des contrats courts, des dispenses, des départs en avril. Nous mettons en place une mutuelle et une prévoyance conformes à votre convention, au meilleur prix, et nous gérons la saison avec vous.</p>
      <ul class="hero-proofs">
        <li>{check()}Un conseiller dédié qui connaît les conventions des stations</li>
        <li>{check()}Un WhatsApp pour vos saisonniers : réponse en 15 minutes</li>
        <li>{check()}Plus de 15 assureurs comparés, sans exclusivité</li>
        <li>{check()}Étude gratuite, rappel sous 24 h ouvrées, sans engagement</li>
      </ul>
    </div>
    {lead_form('accueil')}
  </div>
</section>

{photo_strip()}

<section class="band bg-navy on-navy" id="humain">
  <div class="wrap">
    <div class="sec-head" style="max-width:52em">
      <span class="t-label">Notre engagement</span>
      <h2 class="relief-red">En montagne, on avance en cordée.</h2>
      <p class="t-script" style="font-size:clamp(1.4rem,2.6vw,1.8rem);color:var(--mustard)">Vous gérez la saison. On gère la protection sociale.</p>
      <p>Recrutement en novembre, ouverture en décembre, rush des vacances, départs en avril : pendant la saison, vous n'avez pas le temps de suivre chaque affiliation, chaque dispense, chaque versement santé. Nous le faisons pour vous, et nous restons joignables quand un saisonnier se blesse ou a une question.</p>
    </div>
    <div class="rules" style="color:var(--ink)">
      <div class="rule"><span class="tag">avant la saison</span><h3>Tout est prêt</h3><p>Décision de l'employeur à jour, formulaires de dispense, kit d'arrivée : vos saisonniers sont affiliés ou dispensés dès le premier jour.</p></div>
      <div class="rule"><span class="tag">pendant la saison</span><span class="num">15 min</span><h3>Un WhatsApp pour vos équipes</h3><p>Une ligne dédiée à vos salariés, réponse garantie en 15 minutes en semaine. Pour vous : rappel sous 24 h ouvrées.</p></div>
      <div class="rule"><span class="tag">en fin de saison</span><h3>Les départs gérés</h3><p>Portabilité mentionnée, assureur prévenu, saisonnier informé : il reste couvert jusqu'à la saison suivante s'il touche le chômage.</p></div>
      <div class="rule"><span class="tag">entre deux saisons</span><h3>Le bon prix</h3><p>L'intersaison est le bon moment pour remettre les assureurs en concurrence, à garanties au moins égales.</p></div>
    </div>
  </div>
</section>

<section class="band bg-cream" id="metiers">
  <div class="wrap">
    <div class="sec-head"><span class="t-label">Les entreprises de montagne, notre spécialité</span><h2>Un seul courtier, de la vallée au sommet</h2><p>Hôtel, restaurant d'altitude, exploitant de remontées, magasin de location, école de ski : choisissez votre cas.</p></div>
    {posters_block()}
  </div>
</section>

<section class="band bg-navy on-navy" id="obligations">
  <div class="wrap">
    <div class="sec-head"><span class="t-label">Ce qui est obligatoire</span><h2 class="relief-red">Quatre règles pour la saison</h2><p>Un contrat mal calibré ne se voit pas tant que tout va bien. Il se voit le jour où un saisonnier se blesse sur les pistes ou lors d'un contrôle URSSAF.</p></div>
    <div class="rules" style="color:var(--ink)">
      <div class="rule"><span class="tag">mutuelle</span><span class="num">50 %</span><h3>Au moins, à votre charge</h3><p>Pour chaque salarié, saisonniers compris, sauf dispense écrite et justifiée.</p></div>
      <div class="rule"><span class="tag">contrats courts</span><span class="num">125 %</span><h3>Le versement santé d'un CDD</h3><p>Un saisonnier de moins de 3 mois dispensé reçoit un versement santé : votre participation × 125 %, ou 27,84 € par mois en référence 2026 à temps plein.</p></div>
      <div class="rule"><span class="tag">fin de saison</span><span class="num">12</span><h3>Mois de portabilité au plus</h3><p>Le saisonnier indemnisé par l'assurance chômage garde ses garanties gratuitement, pendant la durée de son contrat.</p></div>
      <div class="rule"><span class="tag">cadres</span><span class="num">1,50 %</span><h3>De la tranche A</h3><p>Sans prévoyance cadres, l'employeur doit lui-même 144 180 € en cas de décès en 2026.</p></div>
    </div>
    <p style="margin-top:26px"><a class="btn btn-red" href="{L('obligations-montagne')}">Lire le guide complet des obligations</a></p>
  </div>
</section>

{montagne_table()}

<section class="band bg-cream" id="actualites">
  <div class="wrap">
    <div class="sec-head"><span class="t-label">Actualités</span><h2>Ce qui change pour la saison 2026-2027</h2></div>
    <div class="rules">
      <div class="rule"><span class="tag">2026</span><span class="num">22,27 €</span><h3>Référence du versement santé</h3><p>Montant mensuel de référence 2026 pour un temps plein (7,44 € en Alsace-Moselle), quand la participation réelle de l'employeur n'est pas connue.</p></div>
      <div class="rule"><span class="tag">1er janvier 2026</span><h3>Remontées : APICIL et l'OCIRP recommandés</h3><p>Pour la prévoyance de la branche des remontées mécaniques et domaines skiables. Recommandés, pas imposés.</p></div>
      <div class="rule"><span class="tag">27 octobre 2025</span><h3>Réembauche des saisonniers</h3><p>Remontées mécaniques : demande avant le 31 mars pour l'été et le 15 septembre pour l'hiver (avenant n° 87).</p></div>
    </div>
  </div>
</section>

{steps_block()}

<section class="band bg-teal" id="outils">
  <div class="wrap">
    <div class="sec-head"><span class="t-label">Outils gratuits</span><h2 class="relief-cream">Faites le point en 2 minutes</h2><p>Deux outils pensés pour les entreprises de montagne, sans inscription.</p></div>
    <div class="rules" style="color:var(--ink)">
      <div class="rule"><span class="tag">simulateur</span><h3>Combien coûte votre protection sociale ?</h3><p>Mutuelle au tarif de votre contrat, prévoyance au taux de votre convention, cadres, forfait social : le coût employeur mensuel et annuel.</p><p><a class="btn btn-navy btn-sm" href="{L('outils')}#simulateur">Lancer le simulateur</a></p></div>
      <div class="rule"><span class="tag">check-up</span><h3>Êtes-vous prêt pour la saison ?</h3><p>Neuf questions, et la liste des points à corriger avant l'arrivée des saisonniers.</p><p><a class="btn btn-navy btn-sm" href="{L('outils')}#checkup">Faire le check-up</a></p></div>
    </div>
  </div>
</section>

{testimonials_block()}
{insurers_block()}
{faq_block(HOME_FAQ)}
""")


# ---------------------------------------------------------------- PAGES MÉTIER
def metier_page(slug, title, desc, crumb, h1, sub, lead, pid, alt, faq, points, wwc, bg="bg-mustard", h1cls="relief-red", subcolor="var(--red)", extra="", value_txt="La loi et votre convention fixent des garanties minimales. Notre travail : trouver le contrat conforme au meilleur tarif, puis gérer la saison à votre place."):
    rules = "".join(f'<div class="rule"><span class="tag">{t}</span><h3>{h}</h3><p>{p}</p></div>' for t, h, p in points)
    PAGES[slug] = (
        title, desc, {"@context": "https://schema.org", "@graph": [ORG_LD, faq_ld(faq), page_meta(title.split(' · ')[0])]}, slug,
        page_hero(bg, crumb, h1, sub, lead, photo_ill(pid, alt), h1cls, subcolor, on_navy=(bg == "bg-navy")) +
        f"""<section class="band bg-cream">
  <div class="wrap">
    <div class="sec-head"><span class="t-label">Ce que nous vérifions</span><h2>Les points clés</h2></div>
    <div class="rules">{rules}</div>
  </div>
</section>
{extra}
{value_block(value_txt)}
{steps_block()}
<section class="band bg-mustard">
  <div class="wrap split">
    <div class="sec-head" style="margin:0"><span class="t-label">Étude gratuite</span><h2>Votre contrat est-il conforme, et au bon prix ?</h2><p style="color:var(--ink)">Envoyez-nous votre demande : nous vérifions votre contrat actuel et vous présentons des offres comparées, sans engagement.</p></div>
    {lead_form(slug, "Demande d'étude")}
  </div>
</section>
{wwc_links(wwc)}
{faq_block(faq, 'Vos questions')}
""")


metier_page("saisonniers",
    "Mutuelle des saisonniers en station : dispenses, versement santé, portabilité · Bonne Cordée",
    "Saisonniers de station de ski : mutuelle dès l'embauche, dispense des CDD de moins de 3 mois, versement santé 2026 (125 %, 22,27 € de référence), portabilité entre deux saisons.",
    "Saisonniers", "Saisonniers :", "couverts toute la saison.",
    "Un saisonnier est un salarié comme les autres : mutuelle, prévoyance, maintien de salaire selon sa convention. Mais les contrats courts ont leurs règles : dispense, versement santé, portabilité. Voici comment ne rien rater.",
    "1735441984733-3dd209fd2fc0", "Rue enneigée d'une station de ski",
    [("Un saisonnier de 4 mois peut-il refuser la mutuelle ?", "La dispense « contrat de moins de 3 mois » ne s'applique pas. Il peut en revanche être dispensé pour d'autres motifs prévus par les textes, par exemple s'il est déjà couvert par une mutuelle collective obligatoire, avec un justificatif."),
     ("Comment calculer le versement santé ?", "Montant que vous auriez payé pour sa mutuelle × 125 % pour un CDD, au prorata des heures. Si ce montant n'est pas connu, la référence 2026 est de 22,27 € par mois à temps plein, soit 27,84 € pour un CDD."),
     ("Mes saisonniers ont-ils droit à la prévoyance ?", "Oui, selon les règles de votre convention. Dans les remontées mécaniques par exemple, le salaire de référence d'un saisonnier est reconstitué sur 12 mois à partir de ses mois travaillés.")],
    [("arrivée", "Affilié ou dispensé dès le 1er jour", "Chaque saisonnier est affilié à l'embauche, ou remplit une demande de dispense écrite et justifiée. Nous préparons le kit d'arrivée."),
     ("contrats courts", "Le versement santé", "Pour un CDD de moins de 3 mois dispensé et titulaire d'une mutuelle responsable : votre participation × 125 %, au prorata des heures."),
     ("départ", "La portabilité", "S'il est indemnisé par l'assurance chômage, le saisonnier garde ses garanties gratuitement pendant la durée de son contrat, 12 mois au plus."),
     ("retour", "La saison suivante", "Réaffiliation à chaque nouvelle saison : nous gardons l'historique pour que rien ne se perde d'une année sur l'autre.")],
    [("ccn-hcr-protection-sociale-saisonniers-extras", "La protection sociale des saisonniers et des extras"), ("portabilite-mutuelle-salaries-quittant-entreprise", "La portabilité pour les salariés qui partent"), ("dispenses-affiliation-mutuelle-cas-autorises", "Les dispenses d'affiliation autorisées")],
    "bg-red", "relief-cream", "var(--mustard)",
    extra=f"""<section class="band bg-cream">
  <div class="wrap narrow prose">
    <div class="sec-head"><span class="t-label">Le versement santé en 2026</span><h2>Combien verser à un saisonnier dispensé ?</h2></div>
    <div class="table-wrap"><table>
      <thead><tr><th>Situation</th><th>Calcul</th><th>Exemple, temps plein</th></tr></thead>
      <tbody>
        <tr><td>Votre participation à la mutuelle est connue</td><td>Participation mensuelle × 125 % (CDD)</td><td class="num">20 € × 125 % = 25 €</td></tr>
        <tr><td>Participation inconnue (référence 2026)</td><td>22,27 € × 125 %</td><td class="num">27,84 €</td></tr>
        <tr><td>Alsace-Moselle (référence 2026)</td><td>7,44 € × 125 %</td><td class="num">9,30 €</td></tr>
      </tbody></table></div>
    <p>Au prorata des heures : un saisonnier à mi-temps reçoit la moitié. Le salarié doit fournir l'attestation de sa mutuelle responsable. Deux contrats successifs de moins de 3 mois qui dépassent ensemble 3 mois : le versement n'est dû que pour le premier. Le versement est exonéré de cotisations sociales mais soumis à la CSG et à la CRDS, et au forfait social à partir de 11 salariés.</p>
    <p class="fine">Source : <a href="{SP}" rel="nofollow noopener" target="_blank">service-public.fr, obligation de l'employeur en matière de complémentaire santé</a> (mise à jour du 20 janvier 2026).</p>
    {cta_inline("Une saison qui démarre ? Nous préparons vos formulaires et calculons vos versements santé.", "Préparer ma saison")}
  </div>
</section>""",
    value_txt="Des dizaines d'arrivées en décembre, des départs en avril : la protection sociale des saisonniers demande de la rigueur. Nous la gérons de bout en bout.")

metier_page("hotels-restaurants",
    "Mutuelle et prévoyance des hôtels et restaurants de station · Bonne Cordée",
    "Hôtel, restaurant d'altitude, bar, discothèque en station : la convention HCR (IDCC 1979), prévoyance 0,86 %, saisonniers, cadres, et comment payer le juste prix.",
    "Hôtels & restaurants", "Hôtels, restaurants,", "bars d'altitude.",
    "Hôtel de station, restaurant d'altitude, bar après-ski : vous appliquez la convention des hôtels, cafés et restaurants. Elle impose une prévoyance précise et une mutuelle pour toute l'équipe, saisonniers compris.",
    "1610803523148-a0052fa341bb", "Chalet en bois sur une montagne enneigée",
    [("Mes saisonniers ont-ils droit à la prévoyance HCR ?", "Oui. La prévoyance de branche s'applique aux salariés non-cadres de la convention, à 0,86 % de la tranche A partagé à parts égales."),
     ("Suis-je obligé de prendre l'assureur de la branche ?", "Non. La branche référence une offre (KLESIA et Malakoff Humanis, avec l'action sociale HCR Bien-être), mais vous pouvez choisir un autre assureur respectant les garanties."),
     ("Un chef de cuisine cadre change-t-il quelque chose ?", "Oui : pour chaque cadre, l'employeur consacre au moins 1,50 % de la tranche A à la prévoyance. Sans contrat, il doit 144 180 € en cas de décès en 2026.")],
    [("prévoyance", "0,86 % de la tranche A", "Pour les non-cadres, à parts égales : arrêt de travail, invalidité, décès, rente éducation. Nous vérifions que vos bulletins le suivent."),
     ("garanties", "Les minimums HCR", "Indemnités portant le revenu à 70 % du salaire après 90 jours d'arrêt, invalidité 45 % ou 70 %, capital décès de 150 % du salaire annuel, rente éducation 12 % ou 18 %."),
     ("mutuelle", "Au moins 50 % employeur", "Pour chaque salarié, saisonniers compris, sauf dispense écrite. Le tarif se négocie : nous comparons."),
     ("cadres", "La prévoyance cadres", "Chef de cuisine, directeur d'hôtel : 1,50 % de la tranche A à votre charge, dès l'embauche ou la promotion.")],
    [("prevoyance-hcr", "La prévoyance de la convention HCR"), ("ccn-hcr-protection-sociale-saisonniers-extras", "Saisonniers et extras en HCR"), ("comparatif-mutuelle-hcr", "Comparer les mutuelles HCR")],
    "bg-mustard",
    extra=f"""<section class="band bg-cream">
  <div class="wrap narrow prose">
    <p>Pour aller plus loin sur la convention des hôtels, cafés et restaurants, notre site spécialisé <a href="https://www.tous-couverts.fr/" target="_blank" rel="noopener">Tous Couverts</a> détaille toutes les règles. Bonne Cordée s'occupe en plus de ce qui est propre aux stations : saisons, contrats courts, versement santé, portabilité entre deux saisons.</p>
  </div>
</section>""")

metier_page("remontees-mecaniques",
    "Prévoyance des remontées mécaniques et domaines skiables (IDCC 454) · Bonne Cordée",
    "Remontées mécaniques et domaines skiables : prévoyance de branche, APICIL et OCIRP recommandés depuis 2026, garanties cadres, saisonniers, réembauche. Étude gratuite.",
    "Remontées mécaniques", "Remontées mécaniques,", "domaines skiables.",
    "Conducteurs, perchmans, pisteurs-secouristes, nivoculteurs : la convention des remontées mécaniques et domaines skiables (IDCC 454) a son propre régime de prévoyance, avec un nouvel organisme recommandé depuis le 1er janvier 2026.",
    "1775642126954-a918219028ed", "Télésiège montant une pente enneigée",
    [("Faut-il passer par APICIL ?", "Non. Depuis le 1er janvier 2026, APICIL Prévoyance, associé à l'OCIRP, est l'organisme recommandé par la branche. Recommandé ne veut pas dire imposé : un autre assureur respectant les garanties de branche reste possible."),
     ("Comment est calculée la prévoyance d'un saisonnier ?", "Selon les documents de l'organisme recommandé, quand le salarié n'a pas travaillé de façon continue sur les 12 derniers mois, son salaire de référence est reconstitué sur 12 mois à partir de la moyenne de ses mois complets travaillés."),
     ("Et la mutuelle ?", "Les règles générales s'appliquent : mutuelle obligatoire pour les salariés, au moins 50 % payés par l'employeur, dispenses écrites et versement santé pour les contrats courts.")],
    [("prévoyance", "Le régime de branche", "Tous les salariés, cadres et non-cadres : décès, rente éducation, incapacité, invalidité. Nous vérifions que votre contrat suit le régime."),
     ("organisme", "APICIL et l'OCIRP recommandés", "Depuis le 1er janvier 2026. Nous comparons honnêtement l'offre recommandée et le marché."),
     ("saisonniers", "Réembauche prioritaire", "Avenant n° 87 du 27 octobre 2025 : demande avant le 31 mars pour l'été et le 15 septembre pour l'hiver."),
     ("cadres", "1,50 % de la tranche 1", "Financé par l'employeur pour les cadres ; au-delà, partage selon le contrat.")],
    [("guide-prevoyance", "Le guide de la prévoyance d'entreprise"), ("prevoyance-cadres-obligation-agirc-article-7", "La prévoyance cadres obligatoire"), ("portabilite-mutuelle-salaries-quittant-entreprise", "La portabilité entre deux saisons")],
    "bg-navy", "relief-cream", "var(--mustard)",
    extra=f"""<section class="band bg-cream">
  <div class="wrap narrow prose">
    <div class="sec-head"><span class="t-label">Exemple : les cadres</span><h2>Le régime de base des cadres chez l'organisme recommandé</h2></div>
    <div class="table-wrap"><table>
      <thead><tr><th>Garantie (régime de base, cadres)</th><th>Niveau</th></tr></thead>
      <tbody>
        <tr><td>Capital décès</td><td>200 % du salaire (seul sans enfant), 250 % (avec enfant, ou marié, pacsé, concubin), double effet de 100 %</td></tr>
        <tr><td>Obsèques</td><td>100 % du plafond mensuel, soit 4 005 € en 2026</td></tr>
        <tr><td>Rente éducation, par enfant</td><td>5 % jusqu'à 12 ans, 10 % de 12 à 18 ans, 15 % de 18 à 26 ans en cas d'études</td></tr>
        <tr><td>Arrêt de travail</td><td>80 % du salaire de référence, en relais du maintien de l'employeur (après 90 jours si moins d'un an d'ancienneté)</td></tr>
        <tr><td>Invalidité</td><td>45 % (1re catégorie), 80 % (2e et 3e catégories)</td></tr>
        <tr><td>Cotisation totale</td><td>1,53 % de la tranche 1 et 2,55 % de la tranche 2 (base, au 1er juillet 2025)</td></tr>
      </tbody></table></div>
    <p>Pour les non-cadres, nous vous communiquons le tableau en vigueur lors de l'étude. Ces niveaux sont ceux de l'organisme recommandé : un autre assureur doit offrir au moins les garanties de la branche.</p>
    <p class="fine">Sources : <a href="{APICIL_RM}" rel="nofollow noopener" target="_blank">APICIL, accord de branche remontées mécaniques</a>, <a href="{APICIL_RM_G}" rel="nofollow noopener" target="_blank">tableau des garanties cadres</a>, <a href="{APICIL_RM_C}" rel="nofollow noopener" target="_blank">cotisations cadres</a>, <a href="{AV87}" rel="nofollow noopener" target="_blank">avenant n° 87</a>. Les textes de la convention et les notices font foi.</p>
    {cta_inline("Exploitant de domaine skiable ? Comparons votre contrat à l'offre recommandée et au marché.")}
  </div>
</section>""")

metier_page("moniteurs-independants",
    "Mutuelle et prévoyance des moniteurs de ski et indépendants de montagne · Bonne Cordée",
    "Moniteur de ski, guide, accompagnateur, loueur indépendant : pas de mutuelle d'entreprise, peu d'indemnités en arrêt. Comment protéger vos revenus de saison.",
    "Indépendants", "Moniteurs, guides,", "indépendants de montagne.",
    "Moniteur de ski, guide de haute montagne, accompagnateur, artisan de station : votre revenu se gagne en quelques mois, et s'arrête si vous vous blessez. Aucune mutuelle d'entreprise ne vous couvre : votre protection dépend de vos choix.",
    "1596473537047-50758f115d04", "Skieur sur une pente enneigée",
    [("Un moniteur indépendant a-t-il une mutuelle obligatoire ?", "Non : en tant que travailleur indépendant, il n'est couvert par aucun contrat d'entreprise. Il choisit librement sa mutuelle et sa prévoyance."),
     ("Mes cotisations sont-elles déductibles ?", "Au régime réel, les cotisations des contrats dits « Madelin » sont déductibles du bénéfice imposable, dans certaines limites. Un micro-entrepreneur ne peut pas les déduire."),
     ("Que se passe-t-il si je me blesse en pleine saison ?", "Vous touchez les indemnités journalières des indépendants, calculées sur vos revenus passés, après un délai de carence. Pour un revenu concentré sur une saison, une prévoyance individuelle est souvent indispensable.")],
    [("revenu", "Protéger la saison", "Des indemnités journalières dès les premiers jours si vous le choisissez, calées sur votre revenu de saison."),
     ("invalidité", "Le risque du métier", "Une blessure grave peut mettre fin à une carrière : une rente d'invalidité adaptée protège l'avenir."),
     ("famille", "Un capital décès", "Pour la famille, en cas de coup dur en montagne. Nous vérifions les exclusions liées aux sports et aux activités professionnelles."),
     ("fiscalité", "Madelin au régime réel", "Cotisations déductibles dans certaines limites ; nous calibrons avec votre expert-comptable.")],
    [("prevoyance-tns-arret-maladie-perte-revenus", "La prévoyance des indépendants : arrêt et perte de revenus"), ("mutuelle-tns-madelin-comment-choisir", "Mutuelle des indépendants : comment choisir"), ("contrat-madelin-tns-avantages-plafonds-2025", "Contrat Madelin : avantages et plafonds")],
    "bg-teal", "relief-cream", "var(--mustard)",
    value_txt="Pas de convention, pas d'employeur : votre protection dépend de vos choix. Nous comparons les contrats individuels et vérifions les exclusions liées à votre métier.")

# ---------------------------------------------------------------- OBLIGATIONS (page pilier)
OBL_FAQ = [
    ("Quelle convention s'applique à mon entreprise de station ?", "Celle de votre activité principale : hôtels, cafés, restaurants (IDCC 1979), remontées mécaniques et domaines skiables (IDCC 454), commerce selon votre activité. Le numéro figure sur vos bulletins de paie."),
    ("Un saisonnier en CDD de 2 mois doit-il être affilié ?", "Il peut demander une dispense s'il a une mutuelle individuelle responsable ; l'employeur lui verse alors un versement santé. Sans demande de dispense, il est affilié."),
    ("Que risque un employeur sans contrat conforme ?", "Un redressement URSSAF sur les contributions exonérées, et l'obligation de verser lui-même les prestations que le contrat aurait dû payer : indemnités, rente d'invalidité ou capital décès."),
    ("Et pour un cadre ?", "L'employeur consacre au moins 1,50 % de la tranche A à sa prévoyance, à sa seule charge. Sans contrat, il doit trois plafonds annuels de la Sécurité sociale en cas de décès, soit 144 180 € en 2026."),
]
PAGES["obligations-montagne"] = (
    "Mutuelle et prévoyance des entreprises de montagne : obligations 2026 · Bonne Cordée",
    "Guide 2026 pour les entreprises de station : mutuelle obligatoire, saisonniers, versement santé, portabilité, prévoyance HCR et remontées mécaniques, cadres. Exemple chiffré.",
    {"@context": "https://schema.org", "@graph": [ORG_LD, faq_ld(OBL_FAQ), page_meta("Mutuelle et prévoyance des entreprises de montagne : obligations 2026")]},
    "obligations-montagne",
    page_hero("bg-cream2", "Obligations", "Les règles de la saison,", "version 2026",
              "Ce que la loi et les conventions des stations imposent à l'employeur en mutuelle et en prévoyance, saisonniers compris, et ce qui reste à négocier.",
              photo_ill("1551524392-9a61031f0246", "Village au pied d'une montagne enneigée")) +
    f"""<section class="band bg-cream" style="padding-top:20px">
  <div class="wrap narrow prose">
    <p style="font-size:.9rem;color:var(--muted)">Mis à jour le 11 novembre 2026 · Rédigé par l'équipe de WealthWise Conseil, courtier immatriculé à l'ORIAS sous le n° 24000251</p>
    <div class="callout"><strong>L'essentiel en 2026</strong>Mutuelle obligatoire pour chaque salarié, <b>saisonniers compris</b>, payée <b>au moins à 50 %</b> par l'employeur. Contrats de moins de 3 mois : dispense possible avec <b>versement santé</b> (participation × 125 %, référence 22,27 € par mois). Prévoyance selon la convention : <b>0,86 % de la tranche A</b> dans les hôtels, cafés et restaurants ; régime de branche avec <b>APICIL et l'OCIRP recommandés</b> dans les remontées mécaniques. Cadres : <b>1,50 % de la tranche A</b>.</div>

    <h2>Ce qui est obligatoire, ce qui se négocie</h2>
    <div class="table-wrap"><table>
      <thead><tr><th>Imposé</th><th>Libre, donc négociable</th></tr></thead>
      <tbody>
        <tr><td>Une mutuelle au moins égale au panier de soins légal et aux garanties de votre convention</td><td>L'assureur et le tarif : les organismes recommandés ne sont pas imposés</td></tr>
        <tr><td>Au moins 50 % de la cotisation à la charge de l'employeur</td><td>Une participation plus élevée, la famille, des options</td></tr>
        <tr><td>La prévoyance de votre convention et celle des cadres</td><td>Le niveau au-dessus du minimum</td></tr>
        <tr><td>Le versement santé pour les CDD courts dispensés</td><td>Le service : qui répond aux saisonniers, qui gère les arrêts</td></tr>
      </tbody></table></div>
    {cta_inline("Votre contrat est-il prêt pour la saison ? Vérification gratuite.")}

    <h2>Les saisonniers</h2>
    <ul>
      <li><strong>Affiliation</strong> dès l'embauche, sauf dispense écrite et justifiée.</li>
      <li><strong>Contrat de moins de 3 mois</strong> : dispense possible si le salarié a une mutuelle individuelle responsable ; l'employeur lui verse le versement santé.</li>
      <li><strong>Versement santé 2026</strong> : participation de l'employeur × 125 % pour un CDD, au prorata des heures ; référence 22,27 € par mois (7,44 € en Alsace-Moselle) si la participation n'est pas connue.</li>
      <li><strong>Portabilité</strong> : le saisonnier indemnisé par l'assurance chômage garde ses garanties gratuitement pendant la durée de son contrat, 12 mois au plus.</li>
      <li><strong>Réembauche</strong> dans les remontées mécaniques : priorité aux saisonniers des saisons précédentes qui en font la demande avant le 31 mars (été) ou le 15 septembre (hiver).</li>
    </ul>

    <h2>Hôtels, cafés, restaurants de station</h2>
    <ul>
      <li>prévoyance des non-cadres : 0,86 % de la tranche A, à parts égales ;</li>
      <li>garanties minimales : revenu porté à 70 % du salaire après 90 jours d'arrêt, invalidité 45 % ou 70 %, capital décès de 150 % du salaire annuel, rente éducation de 12 % ou 18 % ;</li>
      <li>offre référencée par la branche (KLESIA et Malakoff Humanis, avec l'action sociale HCR Bien-être), sans obligation d'y adhérer.</li>
    </ul>

    <h2>Remontées mécaniques et domaines skiables</h2>
    <ul>
      <li>régime de prévoyance de branche pour tous les salariés, cadres et non-cadres ;</li>
      <li>APICIL Prévoyance, associé à l'OCIRP, recommandé depuis le 1er janvier 2026 ;</li>
      <li>pour un saisonnier, salaire de référence reconstitué sur 12 mois selon l'organisme recommandé.</li>
    </ul>
    <p>Le détail des garanties cadres est sur notre page <a href="{L('remontees-mecaniques')}">remontées mécaniques</a>.</p>

    <h2>Combien ça coûte : un exemple</h2>
    <div class="table-wrap"><table>
      <thead><tr><th>Hôtel-restaurant de station : 4 permanents et 12 saisonniers non-cadres à 2 000 €, mutuelle à 40 € par salarié</th><th>Par mois en saison</th></tr></thead>
      <tbody>
        <tr><td>Mutuelle : 16 × 40 € × 50 %</td><td class="num">320,00 €</td></tr>
        <tr><td>Prévoyance : 16 × 2 000 € × 0,86 % × 50 %</td><td class="num">137,60 €</td></tr>
        <tr><td>Forfait social : 8 % de la part patronale (plus de 11 salariés)</td><td class="num">36,61 €</td></tr>
        <tr><td><strong>Coût employeur</strong></td><td class="num"><strong>494,21 €</strong></td></tr>
      </tbody></table></div>
    <p>Le tarif de 40 € est un exemple : il dépend de votre contrat, de l'âge de l'équipe et du niveau de garanties. Si 3 saisonniers en CDD de 2 mois sont dispensés, ils sortent de la mutuelle et reçoivent chacun un versement santé de 20 € × 125 % = 25 € par mois. Le forfait social s'applique selon l'effectif apprécié par les règles de la Sécurité sociale.</p>

    <h2>Ce que nous faisons concrètement</h2>
    <ul>
      <li><strong>Avant la saison</strong> : audit de conformité, décision de l'employeur à jour, kit d'arrivée des saisonniers.</li>
      <li><strong>Un comparatif chiffré</strong> sur plus de 15 assureurs, organismes recommandés compris.</li>
      <li><strong>Pendant la saison</strong> : affiliations, dispenses, versements santé, WhatsApp dédié avec réponse en 15 minutes.</li>
      <li><strong>En fin de saison</strong> : portabilité, sorties déclarées, préparation de la saison suivante.</li>
    </ul>
    <p><a class="btn btn-red" href="{L('devis')}">Demander mon audit gratuit</a></p>

    <h2>Sources</h2>
    <ul style="font-size:.92rem">
      <li><a href="{SP}" rel="nofollow noopener" target="_blank">service-public.fr : obligation de l'employeur en matière de complémentaire santé, versement santé 2026</a></li>
      <li><a href="{APICIL_RM}" rel="nofollow noopener" target="_blank">APICIL : prévoyance de la convention des remontées mécaniques et domaines skiables</a></li>
      <li><a href="{AV87}" rel="nofollow noopener" target="_blank">Avenant n° 87 du 27 octobre 2025 (saisonniers, remontées mécaniques)</a></li>
      <li><a href="https://www.tous-couverts.fr/obligations-convention-hcr" target="_blank" rel="noopener">Les obligations de la convention HCR, sur Tous Couverts</a></li>
    </ul>
    <p style="font-size:.85rem;color:var(--muted)">Règles à jour en novembre 2026. Les textes des conventions publiés sur Légifrance et les notices des assureurs font foi.</p>
  </div>
</section>
{value_block("En station, la saison ne laisse pas de place à l'improvisation. Nous préparons, comparons et gérons, pour que vous puissiez vous concentrer sur vos clients.")}
{wwc_links([("ccn-hcr-protection-sociale-saisonniers-extras", "La protection sociale des saisonniers"), ("due-decision-unilaterale-employeur-guide", "La décision unilatérale de l'employeur"), ("prevoyance-cadres-obligation-agirc-article-7", "La prévoyance cadres obligatoire")])}
{faq_block(OBL_FAQ, 'Obligations : vos questions')}
""")

# ---------------------------------------------------------------- DIRIGEANTS
DIR_FAQ = [
    ("Je suis gérant majoritaire de SARL : le contrat de mes salariés me couvre-t-il ?", "Non. Le gérant majoritaire est travailleur non salarié : il relève de contrats individuels, dont les cotisations peuvent être déductibles sous conditions (dispositif Madelin)."),
    ("Je suis président de SAS : suis-je couvert ?", "Si vous êtes rémunéré, vous êtes assimilé salarié et pouvez être couvert par le contrat collectif, à condition que l'acte de mise en place et le contrat le prévoient."),
    ("Pourquoi une garantie frais généraux ?", "Si vous vous arrêtez en pleine saison, le loyer, les salaires et les crédits continuent. Une garantie frais généraux les prend en charge pendant votre arrêt."),
]
PAGES["dirigeants"] = (
    "Mutuelle et prévoyance des dirigeants d'entreprise de montagne · Bonne Cordée",
    "Hôtelier, restaurateur, exploitant en station : quelle mutuelle et quelle prévoyance pour protéger votre revenu et votre saison, selon votre statut ?",
    {"@context": "https://schema.org", "@graph": [ORG_LD, faq_ld(DIR_FAQ)]},
    "dirigeants",
    page_hero("bg-teal", "Dirigeants", "Et vous, le patron ?", "Qui protège votre saison ?",
              "Une saison se joue en quelques mois. Si vous vous arrêtez en février, le chiffre d'affaires s'effondre mais les charges restent. Le contrat de vos salariés ne vous protège pas forcément : tout dépend de votre statut.",
              photo_ill("1529512602959-fd0ccd7cb261", "Vue sur une montagne enneigée"), "relief-cream", "var(--mustard)") +
    f"""<section class="band bg-cream">
  <div class="wrap">
    <div class="sec-head"><span class="t-label">Selon votre statut</span><h2>Quel régime pour vous ?</h2></div>
    <div class="table-wrap"><table>
      <thead><tr><th>Forme de l'entreprise</th><th>Statut social</th><th>Mutuelle et prévoyance</th></tr></thead>
      <tbody>
        <tr><td>Entreprise individuelle</td><td>Travailleur non salarié</td><td>Contrats individuels, cotisations déductibles sous conditions (dispositif Madelin)</td></tr>
        <tr><td>Gérant majoritaire de SARL</td><td>Travailleur non salarié</td><td>Contrats individuels, cotisations déductibles sous conditions (dispositif Madelin)</td></tr>
        <tr><td>Gérant minoritaire ou égalitaire de SARL rémunéré</td><td>Assimilé salarié</td><td>Peut être couvert par le contrat collectif si l'acte le prévoit</td></tr>
        <tr><td>Président de SAS rémunéré</td><td>Assimilé salarié</td><td>Peut être couvert par le contrat collectif si l'acte le prévoit</td></tr>
      </tbody></table></div>
    <div class="rules" style="margin-top:28px">
      <div class="rule"><span class="tag">revenu</span><h3>Protéger votre revenu</h3><p>Une prévoyance individuelle calée sur votre revenu réel, même concentré sur la saison.</p></div>
      <div class="rule"><span class="tag">frais fixes</span><h3>L'hiver continue de coûter</h3><p>Loyer, salaires, crédits, location du fonds : une garantie frais généraux les prend en charge pendant votre arrêt.</p></div>
      <div class="rule"><span class="tag">santé</span><h3>Votre propre mutuelle</h3><p>Si vous n'êtes pas couvert par le contrat collectif, une mutuelle individuelle adaptée à votre famille.</p></div>
      <div class="rule"><span class="tag">associés</span><h3>Protéger l'associé</h3><p>Le décès ou l'invalidité d'un associé fragilise l'entreprise. Une assurance croisée se prévoit à froid, entre deux saisons.</p></div>
    </div>
  </div>
</section>
<section class="band bg-mustard">
  <div class="wrap split">
    <div class="sec-head" style="margin:0"><span class="t-label">Étude gratuite</span><h2>Protégez le patron aussi.</h2><p style="color:var(--ink)">Indiquez « Ma protection de dirigeant » dans votre besoin : nous étudions votre statut et vos garanties actuelles.</p></div>
    {lead_form('dirigeants', "Demande d'étude · Dirigeant")}
  </div>
</section>
{wwc_links([("protection-dirigeant-tns-assimile-salarie-differences", "Dirigeant indépendant ou assimilé salarié : les différences"), ("gerant-restaurant-hotel-mutuelle-prevoyance-statut", "Gérant d'hôtel ou de restaurant : quel statut, quelle protection"), ("contrat-madelin-tns-avantages-plafonds-2025", "Contrat Madelin : avantages et plafonds")])}
{faq_block(DIR_FAQ, 'Dirigeants : vos questions')}
""")

# ---------------------------------------------------------------- OUTILS
CHECKS = [
    ("Votre décision de l'employeur prévoit-elle les dispenses des contrats courts ?", "Mettre à jour la décision de l'employeur avec les dispenses applicables aux saisonniers."),
    ("Chaque saisonnier est-il affilié, ou dispensé par écrit avec justificatif, dès son arrivée ?", "Préparer un kit d'arrivée : affiliation ou demande de dispense signée et justifiée."),
    ("Versez-vous le versement santé aux CDD de moins de 3 mois dispensés ?", "Calculer et verser le versement santé : participation × 125 %, au prorata des heures."),
    ("Payez-vous au moins 50 % de la cotisation de mutuelle ?", "Ajuster la participation employeur à au moins 50 %."),
    ("Votre prévoyance suit-elle le taux et les garanties de votre convention ?", "Mettre le contrat de prévoyance au niveau de votre convention (0,86 % de la tranche A en HCR, par exemple)."),
    ("Si vous employez un cadre, a-t-il sa prévoyance à 1,50 % de la tranche A ?", "Souscrire la prévoyance cadres dès l'embauche ou la promotion."),
    ("La portabilité est-elle mentionnée sur le certificat de travail des saisonniers qui partent ?", "Mentionner la portabilité et prévenir l'assureur à chaque fin de contrat."),
    ("L'acte de mise en place a-t-il été remis à chaque salarié, avec une preuve ?", "Remettre l'acte de mise en place à chaque salarié et conserver la preuve de remise."),
    ("Votre contrat a-t-il été remis en concurrence depuis moins de 3 ans ?", "Remettre le contrat en concurrence à l'intersaison, à garanties au moins égales."),
]
check_items = "".join(
    f'<li class="check-item" data-fix="{fix}"><span>{q}</span><span class="yn" role="radiogroup" aria-label="{q}">'
    f'<label><input type="radio" name="q{i}" value="oui"><span class="y">Oui</span></label>'
    f'<label><input type="radio" name="q{i}" value="non"><span class="n">Non</span></label>'
    + (f'<label><input type="radio" name="q{i}" value="na"><span class="na">Sans objet</span></label>' if i in (2, 5) else "")
    + '</span></li>' for i, (q, fix) in enumerate(CHECKS))
PAGES["outils"] = (
    "Simulateur et check-up mutuelle et prévoyance pour entreprises de montagne · Bonne Cordée",
    "Outils gratuits pour les entreprises de station : simulateur du coût de la mutuelle et de la prévoyance, et check-up « prêt pour la saison » en 9 questions.",
    {"@context": "https://schema.org", "@graph": [ORG_LD]},
    "outils",
    page_hero("bg-teal", "Outils", "Faites le point.", "Avant l'arrivée des saisonniers.",
              "Un simulateur pour chiffrer le coût de votre protection sociale, et un check-up pour repérer ce qui manque avant que la saison ne commence.",
              photo_ill("1551288049-bebda4e38f71", "Tableaux de bord et graphiques sur un écran"), "relief-cream", "var(--mustard)") +
    f"""<section class="band bg-cream" id="simulateur">
  <div class="wrap">
    <div class="sec-head"><span class="t-label">Simulateur</span><h2>Combien coûte la protection sociale de votre équipe ?</h2><p>Les valeurs proposées sont des exemples (hôtel-restaurant en HCR) : remplacez-les par les vôtres.</p></div>
    <form class="tool" onsubmit="return false">
      <div class="tool-grid">
        <div class="field"><label class="lbl" for="s-nc">Salariés non-cadres (saisonniers compris)</label><input id="s-nc" type="number" min="0" step="1" value="12"></div>
        <div class="field"><label class="lbl" for="s-salnc">Salaire brut moyen (€/mois)</label><input id="s-salnc" type="number" min="0" step="50" value="2000"></div>
        <div class="field"><label class="lbl" for="s-mut">Tarif de votre mutuelle (€ par salarié et par mois)</label><input id="s-mut" type="number" min="0" step="1" value="40"></div>
        <div class="field"><label class="lbl" for="s-prev">Taux de prévoyance de votre convention (%)</label><input id="s-prev" type="number" min="0" step="0.01" value="0.86"></div>
        <div class="field"><label class="lbl" for="s-c">Salariés cadres</label><input id="s-c" type="number" min="0" step="1" value="1"></div>
        <div class="field"><label class="lbl" for="s-salc">Salaire brut moyen cadre (€/mois)</label><input id="s-salc" type="number" min="0" step="50" value="3800"></div>
        <div class="field"><label class="lbl" for="s-part">Part de la mutuelle payée par l'employeur (%)</label><input id="s-part" type="number" min="50" max="100" step="1" value="50"></div>
      </div>
      <div class="tool-out" aria-live="polite">
        <div class="kpi"><span>Coût employeur / mois</span><strong id="o-mois">—</strong></div>
        <div class="kpi"><span>Coût employeur / an</span><strong id="o-an">—</strong></div>
        <div class="kpi"><span>Reste à payer par un salarié / mois</span><strong id="o-sal">—</strong><small>Mutuelle + prévoyance, non-cadre</small></div>
      </div>
      <p id="o-detail" style="color:var(--muted);font-size:.92rem"></p>
      <p class="fine">Hypothèses : mutuelle au tarif que vous indiquez, part employeur d'au moins 50 % ; prévoyance au taux indiqué sur la tranche A (jusqu'à 4 005 € par mois en 2026), partagée à parts égales (0,86 % en hôtels, cafés, restaurants) ; cadres : 1,50 % de la tranche A en plus, à la charge de l'employeur ; forfait social de 8 % à partir de 11 salariés. Coût annuel calculé sur 12 mois : pour une saison, multipliez le coût mensuel par le nombre de mois. Estimation indicative, non contractuelle.</p>
    </form>
  </div>
</section>
<section class="band bg-cream2" id="checkup">
  <div class="wrap narrow">
    <div class="sec-head"><span class="t-label">Check-up</span><h2>Êtes-vous prêt pour la saison ?</h2><p>Neuf questions. Le bilan s'affiche au fur et à mesure.</p></div>
    <form class="tool" onsubmit="return false">
      <ul class="check-list">{check_items}</ul>
      <div class="score" id="checkup-result" hidden><strong></strong><p></p><ul></ul></div>
      <p><a class="btn btn-red" href="{L('devis')}">Faire corriger ces points gratuitement</a></p>
    </form>
  </div>
</section>
""")

# ---------------------------------------------------------------- DEVIS
PAGES["devis"] = (
    "Demande d'étude gratuite · Bonne Cordée",
    "Demandez une étude gratuite de la mutuelle et de la prévoyance de votre entreprise de montagne. Rappel sous 24 h ouvrées.",
    {"@context": "https://schema.org", "@graph": [ORG_LD]},
    "devis",
    f"""<section class="hero">
  <div class="wrap">
    <div class="hero-copy">
      <span class="kicker">Étude gratuite · sans engagement</span>
      <h1 class="hero-h1"><span class="l1">Demande d'étude mutuelle et prévoyance pour votre entreprise de montagne :</span>
      <span class="l2 relief-red">Préparons<br>la saison.</span>
      <span class="l3">15 minutes suffisent.</span></h1>
      <p class="hero-lead">Remplissez la fiche : un conseiller WealthWise Conseil vous répond sous 24 h ouvrées, par téléphone, en visio ou sur WhatsApp.</p>
      <ul class="hero-proofs">
        <li>{check()}Ayez sous la main votre contrat actuel et un bulletin de paie</li>
        <li>{check()}Indiquez votre effectif permanent et le nombre de saisonniers</li>
        <li>{check()}Ou appelez directement le 01 87 66 70 31</li>
      </ul>
    </div>
    {lead_form('devis', "Fiche de demande")}
  </div>
</section>
""")
