"""Articles du blog Bonne Cordée.
   Dans les corps d'articles, {{L:slug}} devient un lien interne au site ; les liens vers WealthWise Conseil sont absolus."""

WWC = "https://www.wealthwiseconseil.fr"

AUTHOR = ("Rédigé par l'équipe de <a href=\"" + WWC + "/\">WealthWise Conseil</a>, le cabinet de courtage indépendant qui porte "
          "la marque Bonne Cordée (ORIAS n° 24000251). Article d'information générale : vos règles dépendent de votre convention collective, "
          "de vos contrats et de votre situation.")

ARTICLES = [
{
 "slug": 'mutuelle-entreprise-assureur-comparateur-ou-courtier-station',
 "title": "Assureur en direct, comparateur ou courtier : comment choisir la mutuelle d'un hôtel de station ?",
 "short": 'Assureur, comparateur ou courtier ?',
 "desc": "Trois façons de souscrire une mutuelle d'entreprise, ce que chacune comprend vraiment, et les questions à poser avant de signer.",
 "date": "2026-11-13", "minutes": 5, "cat": 'Choisir', "color": 'bg-teal', "icon": 'i-chalet',
 "body": """
<p class="lead-p">Quand un hôtel de station cherche une mutuelle pour ses salariés, trois portes s'ouvrent : appeler un assureur, remplir un comparateur en ligne ou passer par un courtier. Le prix affiché se ressemble, le service beaucoup moins.</p>
<h2>L'assureur en direct : une seule offre, la sienne</h2>
<p>Un assureur, une mutuelle ou une institution de prévoyance vous propose ses propres contrats. C'est simple et rapide, mais vous n'avez aucun point de comparaison : impossible de savoir si le tarif est bon pour votre équipe, ni si un concurrent couvre mieux le même risque.</p>
<h2>Le comparateur en ligne : rapide, mais sans vérification</h2>
<p>Un comparateur affiche en quelques minutes les offres de ses partenaires. Il ne vérifie pas que le contrat respecte votre convention collective, ne rédige pas vos documents et ne vous suit pas après la signature. Vos coordonnées sont en général transmises à plusieurs assureurs, qui vous rappellent ensuite.</p>
<h2>Le courtier : il travaille pour vous</h2>
<p>Un courtier est un professionnel indépendant, immatriculé à l'ORIAS. Il représente son client, pas un assureur. Il met plusieurs organismes en concurrence sur le même cahier des charges, vérifie la conformité à la convention, et doit vous remettre par écrit les raisons de son conseil. Il reste ensuite votre interlocuteur pour les affiliations, les départs et les sinistres.</p>
<p>Il est rémunéré par une commission incluse dans la cotisation, versée par l'assureur : l'étude ne vous est pas facturée.</p>
<h2>Ce qui compte pour les entreprises de montagne de Savoie et de Haute-Savoie</h2>
<p>En station, tout se joue sur quelques mois : des dizaines de saisonniers arrivent en décembre et repartent en avril, souvent logés par l'employeur, parfois d'une saison sur l'autre. Un contrat standard, pensé pour une entreprise de bureau, colle rarement à ce profil.</p>
<h2>Les cinq questions à poser avant de signer</h2>
<ul>
<li>Le contrat respecte-t-il toutes les garanties minimales de ma convention collective ? Voir <a href="{{L:obligations-montagne}}">vos obligations</a>.</li>
<li>Qui rédige l'écrit de mise en place et les modèles de dispense ?</li>
<li>Qui mes salariés appellent-ils quand un remboursement bloque ?</li>
<li>Comment le tarif évoluera-t-il, et sur quelles données ?</li>
<li>Combien d'offres ont été comparées, et lesquelles ?</li>
</ul>
<p>Si l'interlocuteur ne sait pas répondre aux deux premières, le contrat risque d'être conforme sur le papier et fragile le jour d'un contrôle.</p>
<h2>En pratique</h2>
<p>Pour une petite équipe, la différence de prix entre les trois voies est souvent faible. La différence se fait sur la conformité et le suivi. C'est ce que nous faisons : comparer, vérifier, rédiger, puis rester joignables. <a href="{{L:devis}}">Demandez votre étude gratuite</a>.</p>
""",
},
{
 "slug": 'passer-a-11-salaries-mutuelle-prevoyance-station',
 "title": "Passer à 11 salariés : ce qui change pour la mutuelle et la prévoyance d'un hôtel de station",
 "short": 'Passer à 11 salariés',
 "desc": 'Forfait social de 8 % sur la part employeur, règle des cinq ans, comité social et économique : ce que déclenche le seuil de 11 salariés.',
 "date": "2026-11-13", "minutes": 5, "cat": 'Effectif', "color": 'bg-red', "icon": 'i-peak',
 "body": """
<p class="lead-p">L'embauche du onzième salarié est un cap. Pour la mutuelle et la prévoyance, elle déclenche une contribution que un hôtel de station ne payait pas jusque-là : le forfait social. Elle ne s'applique pas du jour au lendemain, et c'est une bonne nouvelle.</p>
<h2>Qu'est-ce que le forfait social ?</h2>
<p>C'est une contribution de <strong>8 %</strong> due par l'employeur sur la part qu'il finance pour la mutuelle et la prévoyance de ses salariés. Les entreprises de moins de 11 salariés en sont exonérées.</p>
<h2>Un exemple chiffré</h2>
<p>Prenons une cotisation de mutuelle de 50 € par mois et par salarié, prise en charge à 50 % par l'employeur. Le montant est une hypothèse, pour illustrer le calcul.</p>
<div class="table-wrap"><table>
<thead><tr><th>Effectif</th><th>Part employeur</th><th>Forfait social</th><th>Coût mensuel</th></tr></thead>
<tbody>
<tr><td>10 salariés</td><td>250 €</td><td>Non dû</td><td>250 €</td></tr>
<tr><td>11 salariés</td><td>275 €</td><td>22 €</td><td>297 €</td></tr>
<tr><td>15 salariés</td><td>375 €</td><td>30 €</td><td>405 €</td></tr>
</tbody></table></div>
<p>Le forfait social s'applique aussi à la part employeur de la prévoyance, y compris celle des cadres.</p>
<h2>La règle des cinq ans</h2>
<p>Le seuil ne joue pas dès la première embauche au-delà de dix. L'effectif retenu est une moyenne annuelle, calculée selon les règles de la Sécurité sociale, et le franchissement du seuil n'est pris en compte que lorsqu'il a été atteint ou dépassé pendant <strong>cinq années civiles consécutives</strong>. Une entreprise qui dépasse 11 salariés cette année a donc, en principe, plusieurs années devant elle. Faites confirmer votre situation par votre expert-comptable : le calcul de l'effectif réserve des surprises.</p>
<h2>Ce que le seuil change aussi</h2>
<ul>
<li><strong>Le comité social et économique</strong> devient obligatoire quand l'effectif atteint 11 salariés pendant douze mois consécutifs. Il porte les réclamations des salariés, y compris sur la mutuelle ; à partir de 50 salariés, il doit être consulté avant toute modification des garanties.</li>
<li><strong>Le poids face aux assureurs</strong> augmente : à partir d'une dizaine de salariés, le tarif se négocie plus facilement.</li>
</ul>
<h2>Pour les entreprises de montagne de Savoie et de Haute-Savoie</h2>
<p>En station, tout se joue sur quelques mois : des dizaines de saisonniers arrivent en décembre et repartent en avril, souvent logés par l'employeur, parfois d'une saison sur l'autre. Le calcul de l'effectif moyen en tient compte : un salarié à temps partiel ou présent une partie de l'année ne compte pas pour un.</p>
<h2>Comment s'y préparer</h2>
<p>Trois réflexes : suivre son effectif moyen chaque année, intégrer les 8 % dans le budget avant qu'ils ne soient dus, et profiter du cap pour remettre le contrat en concurrence. Un exploitant qui tient un hôtel, un restaurant d'altitude et un magasin de location a souvent trois contrats. Notre <a href="/guides/cout-mutuelle-entreprise-employeur">guide du coût employeur</a> contient un calculateur pour faire le compte avec vos chiffres.</p>
""",
},
{
 "slug": 'tarif-unique-isole-famille-adulte-enfant-station',
 "title": 'Tarif unique, isolé/famille ou adulte/enfant : quelle structure de cotisation pour un hôtel de station ?',
 "short": 'Quelle structure de cotisation ?',
 "desc": "La structure de cotisation décide de ce que paient l'employeur et chaque salarié. Les trois modèles, leurs effets, et celui qui convient à votre équipe.",
 "date": "2026-11-13", "minutes": 5, "cat": 'Cotisation', "color": 'bg-navy', "icon": 'i-rope',
 "body": """
<p class="lead-p">Deux contrats aux garanties identiques peuvent coûter très différemment selon la façon dont la cotisation est découpée. C'est la structure de cotisation, et c'est souvent le premier réglage à revoir d'un hôtel de station.</p>
<h2>Les trois structures courantes</h2>
<div class="table-wrap"><table>
<thead><tr><th>Structure</th><th>Principe</th><th>Qui est avantagé</th></tr></thead>
<tbody>
<tr><td>Tarif unique</td><td>Un seul prix par salarié, qu'il couvre une personne ou toute sa famille</td><td>Les familles nombreuses</td></tr>
<tr><td>Isolé / famille</td><td>Un prix pour le salarié seul, un autre pour le salarié et sa famille</td><td>Les salariés seuls, qui ne paient plus pour les autres</td></tr>
<tr><td>Adulte / enfant</td><td>Un prix par adulte couvert, un prix par enfant, souvent gratuit à partir du troisième</td><td>Chacun paie au plus près de sa situation</td></tr>
</tbody></table></div>
<h2>Ce que finance l'employeur</h2>
<p>La loi impose à l'employeur de payer au moins 50 % de la cotisation qui couvre <strong>le salarié</strong>, pour sa couverture obligatoire. Rien ne l'oblige à financer la part du conjoint et des enfants, sauf si la convention collective ou l'écrit de mise en place le prévoit. Avec un tarif unique « famille », l'employeur finance la moitié d'un prix calculé pour des foyers entiers, même si la plupart de ses salariés sont seuls.</p>
<h2>Quelle structure pour les entreprises de montagne de Savoie et de Haute-Savoie ?</h2>
<p>En station, tout se joue sur quelques mois : des dizaines de saisonniers arrivent en décembre et repartent en avril, souvent logés par l'employeur, parfois d'une saison sur l'autre.</p>
<p>Deux repères pour décider. Si la plupart des salariés sont seuls, ou déjà couverts par ailleurs, une structure « isolé / famille » ou « adulte / enfant » est en général plus juste : la part employeur est calée sur le salarié, et la couverture du conjoint et des enfants devient une option, payée par ceux qui en ont besoin. Si presque tous ont une famille à couvrir, le tarif unique reste simple à gérer et lisible sur le bulletin de paie.</p>
<h2>Le piège de la couverture familiale obligatoire</h2>
<p>Si l'écrit de mise en place rend la couverture des ayants droit obligatoire, tous les salariés paient le tarif famille. Des dispenses existent, notamment pour le salarié dont le conjoint est déjà couvert par un autre contrat obligatoire, mais elles doivent être prévues et justifiées par écrit. Vérifiez ce point avant de changer de structure : voir <a href="{{L:obligations-montagne}}">vos obligations</a>.</p>
<h2>Comment changer de structure</h2>
<ol>
<li>Demander à l'assureur, ou à un courtier, de chiffrer les trois structures sur votre effectif réel.</li>
<li>Comparer le coût pour l'employeur et pour trois salariés types : seul, en couple, avec enfants.</li>
<li>Mettre à jour l'écrit de mise en place et le remettre aux salariés.</li>
<li>Informer chacun de ce qui change sur son bulletin de paie.</li>
</ol>
<p>Nous faisons ce chiffrage gratuitement : <a href="{{L:devis}}">envoyez-nous votre contrat actuel</a> et la composition de votre équipe.</p>
""",
},
{
 "slug": 'cotisation-mutuelle-augmente-que-faire-station',
 "title": 'La cotisation de mutuelle augmente chaque année : que peut faire un hôtel de station ?',
 "short": 'La mutuelle augmente : que faire ?',
 "desc": "Pourquoi le tarif monte, quels documents demander à l'assureur, et les quatre leviers pour reprendre la main sans dégrader la couverture.",
 "date": "2026-11-13", "minutes": 5, "cat": 'Tarif', "color": 'bg-mustard', "icon": 'i-lift',
 "body": """
<p class="lead-p">Chaque automne, le courrier arrive : la cotisation augmentera au 1er janvier. Beaucoup d'employeurs signent sans discuter. Un hôtel de station a pourtant plusieurs moyens d'agir, à condition de s'y prendre avant la fin de l'année.</p>
<h2>Pourquoi le tarif augmente</h2>
<ul>
<li><strong>Les dépenses de santé progressent</strong> chaque année, et une part croissante est transférée de la Sécurité sociale vers les mutuelles.</li>
<li><strong>Le plafond de la Sécurité sociale</strong>, sur lequel beaucoup de cotisations sont indexées, est revalorisé chaque 1er janvier. Il est de 4 005 € par mois en 2026.</li>
<li><strong>Les remboursements de votre équipe</strong> : si le contrat a beaucoup remboursé, l'assureur ajuste le prix.</li>
<li><strong>L'âge moyen</strong> de l'équipe, qui monte avec l'ancienneté.</li>
</ul>
<h2>Le document à demander : les comptes de résultats</h2>
<p>Pour un contrat collectif, l'assureur doit remettre chaque année à l'employeur un rapport sur les comptes du contrat. Il compare les cotisations encaissées et les remboursements versés. C'est la pièce qui permet de savoir si la hausse est justifiée, et de négocier chiffres en main. Sur un très petit effectif, le contrat est souvent mutualisé avec d'autres entreprises et le détail est plus limité : demandez-le quand même.</p>
<h2>Quatre leviers pour agir</h2>
<ol>
<li><strong>Négocier</strong> la hausse avec l'assureur, comptes à l'appui.</li>
<li><strong>Revoir la structure de cotisation</strong> : tarif unique, « isolé / famille » ou « adulte / enfant ».</li>
<li><strong>Ajuster les garanties</strong> : garder une base conforme à la convention et passer en option ce que peu de salariés utilisent.</li>
<li><strong>Mettre en concurrence</strong> : un contrat de mutuelle de plus d'un an peut être résilié à tout moment, avec un mois de délai.</li>
</ol>
<h2>Pour les entreprises de montagne de Savoie et de Haute-Savoie</h2>
<p>En station, tout se joue sur quelques mois : des dizaines de saisonniers arrivent en décembre et repartent en avril, souvent logés par l'employeur, parfois d'une saison sur l'autre. Ces caractéristiques pèsent sur le tarif : un assureur qui connaît le métier les tarifera mieux qu'un autre.</p>
<h2>Le calendrier à respecter</h2>
<p>Pour la mutuelle, vous pouvez agir toute l'année dès que le contrat a plus d'un an. Pour la prévoyance, la résiliation se fait à l'échéance, avec un préavis souvent de deux mois : pour un contrat qui se termine le 31 décembre, la décision se prend avant la fin octobre. Notre <a href="/guides/changer-de-mutuelle-entreprise">guide pour changer de mutuelle</a> détaille les étapes.</p>
<h2>Ce qu'il ne faut pas faire</h2>
<p>Baisser les garanties sous le minimum de la convention collective pour contenir le prix. Le contrat deviendrait non conforme, avec un risque de redressement bien supérieur à l'économie réalisée. Avant toute modification, vérifiez <a href="{{L:obligations-montagne}}">vos obligations</a>, ou <a href="{{L:devis}}">confiez-nous le comparatif</a>.</p>
""",
},
{
 "slug": 'conjoint-enfants-mutuelle-entreprise-station',
 "title": "Conjoint et enfants : faut-il les couvrir dans la mutuelle d'un hôtel de station ?",
 "short": 'Couvrir conjoint et enfants ?',
 "desc": "Couverture familiale obligatoire ou facultative, qui paie, quelles dispenses pour les couples : ce que l'employeur doit décider et écrire.",
 "date": "2026-11-13", "minutes": 5, "cat": 'Famille', "color": 'bg-teal', "icon": 'i-chalet',
 "body": """
<p class="lead-p">« Est-ce que ma femme et mes enfants sont couverts ? » C'est la première question d'un salarié à l'embauche. La réponse dépend d'un choix de l'employeur, que beaucoup ignorent avoir fait. Voici comment trancher d'un hôtel de station.</p>
<h2>Ce que la loi impose</h2>
<p>La loi oblige l'employeur à couvrir <strong>le salarié</strong>. Elle n'impose pas de couvrir son conjoint ni ses enfants. C'est la convention collective, ou à défaut l'écrit de mise en place, qui décide. Commencez par vérifier ce que prévoit votre branche : voir <a href="{{L:obligations-montagne}}">vos obligations</a>.</p>
<h2>Deux façons de couvrir la famille</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Couverture familiale obligatoire</th><th>Couverture familiale facultative</th></tr></thead>
<tbody>
<tr><td>Qui est couvert</td><td>Le salarié, son conjoint et ses enfants, d'office</td><td>Le salarié ; il ajoute sa famille s'il le souhaite</td></tr>
<tr><td>Qui paie la part de la famille</td><td>Employeur et salarié, selon la répartition prévue</td><td>Le salarié seul, en général</td></tr>
<tr><td>Régime social de la part employeur</td><td>Exonérée dans les limites habituelles</td><td>Une participation de l'employeur à une couverture facultative est soumise à cotisations</td></tr>
</tbody></table></div>
<h2>Qui sont les ayants droit ?</h2>
<p>Le contrat les définit. On y trouve en général le conjoint, le partenaire de pacte civil de solidarité ou le concubin, et les enfants à charge jusqu'à un âge fixé par le contrat, souvent prolongé pendant les études.</p>
<h2>Le cas des couples</h2>
<p>Quand la couverture familiale est obligatoire, un salarié dont le conjoint est déjà couvert par un autre contrat collectif obligatoire peut demander à en être dispensé, si l'écrit de mise en place le prévoit. Et quand deux conjoints travaillent dans la même entreprise, l'un peut être couvert comme ayant droit de l'autre, pour éviter de payer deux fois. Ces demandes sont écrites et justifiées chaque année.</p>
<h2>Que choisir pour les entreprises de montagne de Savoie et de Haute-Savoie ?</h2>
<p>En station, tout se joue sur quelques mois : des dizaines de saisonniers arrivent en décembre et repartent en avril, souvent logés par l'employeur, parfois d'une saison sur l'autre.</p>
<p>La couverture familiale facultative convient quand les situations sont très variées : chacun paie pour la sienne, et le budget de l'employeur ne dépend pas de la composition des foyers. La couverture familiale obligatoire a du sens dans une équipe stable, où presque tous les salariés ont une famille, et quand l'employeur veut en faire un avantage pour fidéliser.</p>
<h2>Ce qu'il faut écrire</h2>
<ul>
<li>dans l'écrit de mise en place : qui est couvert, à titre obligatoire ou facultatif, et qui paie quoi ;</li>
<li>les cas de dispense ouverts aux salariés ;</li>
<li>la définition des ayants droit, reprise de la notice de l'assureur.</li>
</ul>
<p>Un doute sur ce que prévoit votre contrat actuel ? <a href="{{L:devis}}">Envoyez-le-nous</a> : nous vous disons en clair qui est couvert, et à quel prix.</p>
""",
},
{
 'slug': 'saisonnier-station-mutuelle-obligatoire',
 'title': 'Saisonnier en station : la mutuelle est-elle obligatoire ?',
 'short': 'Saisonniers : la mutuelle',
 'desc': "Un saisonnier a droit à la mutuelle de l'entreprise dès l'embauche, avec au moins 50 % payés par l'employeur. Les dispenses possibles et ce que l'employeur doit garder.",
 'date': '2026-11-11',
 'minutes': 4,
 'cat': 'Saisonniers',
 'color': 'bg-red',
 'icon': 'i-rope',
 'body': '\n<p class="lead-p">Chaque hiver, les stations de Savoie et de Haute-Savoie embauchent des milliers de saisonniers. Une question revient à chaque fois : faut-il leur donner la mutuelle de l\'entreprise ? La réponse est oui, avec des exceptions précises.</p>\n<h2>Le principe</h2>\n<p>Un saisonnier est un salarié comme les autres. Depuis 2016, tout employeur doit proposer une mutuelle à ses salariés et en payer au moins la moitié. Le saisonnier est donc affilié dès son arrivée, sauf s\'il demande une dispense.</p>\n<h2>Les dispenses qui concernent souvent les saisonniers</h2>\n<ul>\n<li><strong>contrat de moins de 3 mois</strong> : il peut demander à être dispensé s\'il a une mutuelle individuelle responsable ; l\'employeur lui verse alors un versement santé ;</li>\n<li><strong>déjà couvert</strong> par une mutuelle collective obligatoire, par exemple celle de son conjoint, avec un justificatif ;</li>\n<li><strong>bénéficiaire de la complémentaire santé solidaire</strong> ;</li>\n<li><strong>les autres cas</strong> prévus par votre convention et votre décision de l\'employeur.</li>\n</ul>\n<h2>La forme compte</h2>\n<p>Une dispense n\'existe que si elle est écrite, signée par le salarié et accompagnée de son justificatif. Sans document, il doit être affilié. En cas de contrôle URSSAF, c\'est ce dossier qui protège l\'employeur.</p>\n<h2>Et la prévoyance ?</h2>\n<p>Elle suit les règles de votre convention : 0,86 % de la tranche A, à parts égales, pour les non-cadres des hôtels, cafés et restaurants ; un régime de branche dans les remontées mécaniques. Les dispenses de mutuelle ne s\'y appliquent pas.</p>\n<h2>Ce qui se négocie</h2>\n<p>Le tarif et l\'assureur. Avec beaucoup de saisonniers jeunes, une offre bien choisie peut être plus adaptée que le contrat signé il y a des années. Seule une comparaison le dit.</p>\n<p>Voir notre page <a href="{{L:saisonniers}}">saisonniers</a> et le guide de WealthWise Conseil sur <a href="https://www.wealthwiseconseil.fr/ccn-hcr-protection-sociale-saisonniers-extras">la protection sociale des saisonniers</a>.</p>\n<div class="callout"><strong>Bonne Cordée s\'en occupe</strong>Nous préparons votre kit saisonniers : formulaires, affiliations et dispenses, avant l\'ouverture. <a href="{{L:devis}}">Demander mon étude gratuite</a>, ou appelez le 01 87 66 70 31.</div>'
},
{
 'slug': 'versement-sante-2026-saisonniers-calcul',
 'title': 'Versement santé 2026 : comment le calculer pour vos saisonniers',
 'short': 'Le versement santé 2026',
 'desc': 'Pour un saisonnier en CDD de moins de 3 mois dispensé de mutuelle : participation × 125 %, ou 22,27 € de référence en 2026. Calcul, exemples et conditions.',
 'date': '2026-11-11',
 'minutes': 4,
 'cat': 'Saisonniers',
 'color': 'bg-mustard',
 'icon': 'i-chalet',
 'body': '\n<p class="lead-p">Le versement santé, parfois appelé « chèque santé », remplace la mutuelle d\'entreprise pour certains contrats courts. En station, il concerne beaucoup de saisonniers. Voici comment le calculer en 2026.</p>\n<h2>Qui y a droit ?</h2>\n<ul>\n<li>un salarié en CDD ou en mission de moins de 3 mois ;</li>\n<li>qui a demandé à être dispensé de la mutuelle de l\'entreprise ;</li>\n<li>et qui justifie d\'une mutuelle individuelle responsable, avec une attestation de son assureur.</li>\n</ul>\n<h2>Le calcul</h2>\n<p>Le versement est égal à ce que l\'employeur aurait payé pour sa mutuelle, multiplié par 125 % pour un CDD (105 % pour un CDI), au prorata des heures travaillées par rapport à 151,67 heures par mois.</p>\n<div class="table-wrap"><table>\n<thead><tr><th>Cas, temps plein</th><th>Calcul</th><th>Versement mensuel</th></tr></thead>\n<tbody>\n<tr><td>Participation employeur connue : 20 €</td><td>20 € × 125 %</td><td>25,00 €</td></tr>\n<tr><td>Participation inconnue, référence 2026</td><td>22,27 € × 125 %</td><td>27,84 €</td></tr>\n<tr><td>Alsace-Moselle, référence 2026</td><td>7,44 € × 125 %</td><td>9,30 €</td></tr>\n</tbody></table></div>\n<p>Pour un saisonnier à mi-temps, on divise par deux.</p>\n<h2>Les règles à connaître</h2>\n<ul>\n<li>deux contrats successifs de moins de 3 mois qui dépassent ensemble 3 mois : le versement n\'est dû que pour le premier ;</li>\n<li>un renouvellement de contrat ne déclenche pas de nouveau versement ;</li>\n<li>le versement est exonéré de cotisations sociales, mais soumis à la CSG, à la CRDS et au forfait social à partir de 11 salariés.</li>\n</ul>\n<h2>Le bon réflexe</h2>\n<p>Vérifier l\'attestation de mutuelle responsable avant de verser, et la conserver avec la demande de dispense.</p>\n<p>Source : <a href="https://entreprendre.service-public.gouv.fr/vosdroits/F33754" rel="nofollow noopener" target="_blank">service-public.fr</a>, mise à jour du 20 janvier 2026. Voir aussi notre page <a href="{{L:saisonniers}}">saisonniers</a> et le guide de WealthWise Conseil sur <a href="https://www.wealthwiseconseil.fr/dispenses-affiliation-mutuelle-cas-autorises">les dispenses</a>.</p>\n<div class="callout"><strong>Bonne Cordée s\'en occupe</strong>Nous calculons vos versements santé et préparons les dispenses de toute la saison. <a href="{{L:devis}}">Demander mon étude gratuite</a>, ou appelez le 01 87 66 70 31.</div>'
},
{
 'slug': 'portabilite-entre-deux-saisons',
 'title': 'Entre deux saisons : la portabilité de la mutuelle et de la prévoyance',
 'short': 'La portabilité entre saisons',
 'desc': "Un saisonnier indemnisé par l'assurance chômage garde sa mutuelle et sa prévoyance gratuitement pendant la durée de son contrat. Ce que l'employeur doit faire en avril.",
 'date': '2026-11-11',
 'minutes': 4,
 'cat': 'Saisonniers',
 'color': 'bg-teal',
 'icon': 'i-peak',
 'body': '\n<p class="lead-p">En avril, les stations se vident. Beaucoup de saisonniers ignorent qu\'ils restent couverts après leur départ, parfois jusqu\'à la saison suivante. C\'est la portabilité, et l\'employeur a un rôle à jouer.</p>\n<h2>Qui y a droit ?</h2>\n<ul>\n<li>le saisonnier dont le contrat se termine et qui est indemnisé par l\'assurance chômage ;</li>\n<li>à condition d\'avoir été affilié à la mutuelle et à la prévoyance de l\'entreprise ;</li>\n<li>sauf rupture pour faute lourde.</li>\n</ul>\n<h2>Combien de temps ?</h2>\n<p>La durée du dernier contrat, arrondie au mois supérieur, dans la limite de 12 mois. Un saisonnier embauché de décembre à avril garde ses garanties environ cinq mois, sauf s\'il retrouve un emploi avant, par exemple pour la saison d\'été.</p>\n<h2>Qui paie ?</h2>\n<p>Personne de plus : la portabilité est financée par les cotisations des salariés en poste. Ni l\'ancien salarié, ni l\'employeur ne paient de supplément.</p>\n<h2>Ce que fait l\'employeur en fin de saison</h2>\n<ol>\n<li>mentionner la portabilité dans le certificat de travail ;</li>\n<li>signaler la fin du contrat à l\'assureur ;</li>\n<li>remettre au saisonnier les informations de l\'assureur.</li>\n</ol>\n<h2>Un argument de fidélisation</h2>\n<p>Un saisonnier qui reste couvert jusqu\'à l\'été ou l\'hiver suivant revient plus volontiers. Dans les remontées mécaniques, la convention prévoit d\'ailleurs une priorité de réembauche pour les saisonniers qui en font la demande avant le 31 mars (été) ou le 15 septembre (hiver).</p>\n<p>Voir notre page <a href="{{L:saisonniers}}">saisonniers</a> et le guide de WealthWise Conseil sur <a href="https://www.wealthwiseconseil.fr/portabilite-mutuelle-salaries-quittant-entreprise">la portabilité</a>.</p>\n<div class="callout"><strong>Bonne Cordée s\'en occupe</strong>Avec nous, la fin de saison est gérée : portabilité, sorties, préparation de l\'hiver suivant. <a href="{{L:devis}}">Demander mon étude gratuite</a>, ou appelez le 01 87 66 70 31.</div>'
},
{
 'slug': 'remontees-mecaniques-apicil-ocirp-recommandes-2026',
 'title': "Remontées mécaniques : APICIL et l'OCIRP recommandés depuis 2026",
 'short': 'Remontées : le nouvel organisme',
 'desc': "Depuis le 1er janvier 2026, APICIL Prévoyance et l'OCIRP sont recommandés pour la prévoyance des remontées mécaniques et domaines skiables. Ce que ça change.",
 'date': '2026-11-11',
 'minutes': 4,
 'cat': 'Remontées mécaniques',
 'color': 'bg-navy',
 'icon': 'i-lift',
 'body': '\n<p class="lead-p">La branche des remontées mécaniques et domaines skiables (IDCC 454) a changé d\'organisme recommandé pour sa prévoyance au 1er janvier 2026. Pour les exploitants, c\'est le moment de regarder leur contrat.</p>\n<h2>Ce qui a changé</h2>\n<p>Depuis le 1er janvier 2026, APICIL Prévoyance, associé à l\'OCIRP pour les rentes, est l\'organisme recommandé par la branche. Le régime couvre tous les salariés, cadres et non-cadres : décès, rentes pour les enfants et le conjoint, perte totale d\'autonomie, arrêt de travail et invalidité.</p>\n<h2>Recommandé ne veut pas dire imposé</h2>\n<p>Depuis 2013, une branche ne peut plus obliger les entreprises à adhérer à un assureur. Elle peut en recommander un. Vous restez libre de choisir un autre assureur, à condition que votre contrat offre au moins les garanties de la branche.</p>\n<h2>Un exemple : les cadres</h2>\n<ul>\n<li>capital décès de 200 % à 250 % du salaire selon la situation familiale, avec un double effet ;</li>\n<li>rente éducation de 5 %, 10 % ou 15 % du salaire selon l\'âge de l\'enfant ;</li>\n<li>80 % du salaire en arrêt de travail, en relais du maintien de l\'employeur ;</li>\n<li>invalidité à 45 % ou 80 % ;</li>\n<li>cotisation de base de 1,53 % de la tranche 1 et 2,55 % de la tranche 2 (grille au 1er juillet 2025).</li>\n</ul>\n<h2>Et les saisonniers ?</h2>\n<p>Selon l\'organisme recommandé, quand un salarié n\'a pas travaillé de façon continue sur les 12 derniers mois, son salaire de référence est reconstitué sur 12 mois à partir de ses mois complets travaillés. C\'est important pour le calcul d\'un capital décès ou d\'une indemnité.</p>\n<h2>Ce que nous faisons</h2>\n<p>Nous comparons honnêtement l\'offre recommandée et le marché, garanties ligne par ligne, et nous gérons les entrées et sorties de saison.</p>\n<p>Voir notre page <a href="{{L:remontees-mecaniques}}">remontées mécaniques</a> et le <a href="https://www.wealthwiseconseil.fr/guide-prevoyance">guide de la prévoyance</a> de WealthWise Conseil.</p>\n<div class="callout"><strong>Bonne Cordée s\'en occupe</strong>Exploitant de domaine skiable ? Nous comparons votre contrat à l\'offre recommandée et au marché. <a href="{{L:devis}}">Demander mon étude gratuite</a>, ou appelez le 01 87 66 70 31.</div>'
},
{
 'slug': 'hotel-station-prevoyance-hcr-saisonniers',
 'title': 'Hôtel de station : la prévoyance HCR de vos saisonniers',
 'short': 'Hôtels : la prévoyance HCR',
 'desc': 'Dans un hôtel ou un restaurant de station, la prévoyance HCR couvre aussi les saisonniers : 0,86 % de la tranche A, à parts égales. Garanties et points à vérifier.',
 'date': '2026-11-11',
 'minutes': 4,
 'cat': 'Hôtels & restaurants',
 'color': 'bg-red',
 'icon': 'i-chalet',
 'body': '\n<p class="lead-p">Réceptionnistes, femmes de chambre, cuisiniers, serveurs, plongeurs : dans un hôtel de station, la plupart des salariés sont des saisonniers. Ils relèvent de la convention des hôtels, cafés et restaurants, et de sa prévoyance.</p>\n<h2>Le taux</h2>\n<p>Pour les non-cadres, la prévoyance de branche est de 0,86 % de la tranche A du salaire, partagée à parts égales entre l\'employeur et le salarié. Pour un saisonnier payé 2 000 € brut, cela représente 8,60 € chacun par mois.</p>\n<h2>Les garanties minimales</h2>\n<ul>\n<li>arrêt de travail : indemnités qui portent le revenu à 70 % du salaire après 90 jours d\'arrêt ;</li>\n<li>invalidité : rente de 45 % ou 70 % du salaire ;</li>\n<li>décès : capital de 150 % du salaire annuel ;</li>\n<li>rente éducation : 12 % ou 18 % du salaire par enfant, selon son âge.</li>\n</ul>\n<h2>Les cadres</h2>\n<p>Directeur d\'hôtel, chef de cuisine : pour chaque cadre, l\'employeur consacre au moins 1,50 % de la tranche A à la prévoyance, à sa seule charge. Sans contrat, il doit 144 180 € en cas de décès en 2026.</p>\n<h2>L\'offre de branche</h2>\n<p>La branche référence une offre (KLESIA et Malakoff Humanis, avec l\'action sociale HCR Bien-être). Elle n\'est pas imposée : un autre assureur respectant les garanties reste possible.</p>\n<h2>À vérifier avant l\'ouverture</h2>\n<ul>\n<li>le taux de 0,86 % sur les bulletins ;</li>\n<li>la couverture des saisonniers dès leur arrivée ;</li>\n<li>les cadres et leur 1,50 %.</li>\n</ul>\n<p>Voir notre page <a href="{{L:hotels-restaurants}}">hôtels et restaurants</a> et le guide de WealthWise Conseil sur <a href="https://www.wealthwiseconseil.fr/prevoyance-hcr">la prévoyance HCR</a>.</p>\n<div class="callout"><strong>Bonne Cordée s\'en occupe</strong>Nous vérifions votre prévoyance avant la saison et comparons les offres conformes. <a href="{{L:devis}}">Demander mon étude gratuite</a>, ou appelez le 01 87 66 70 31.</div>'
},
{
 'slug': 'saisonnier-blesse-pistes-accident-travail',
 'title': 'Saisonnier blessé sur les pistes ou au travail : que se passe-t-il ?',
 'short': 'Saisonnier blessé',
 'desc': 'Chute sur une piste verglacée, blessure en cuisine, accident de trajet : démarches, indemnités et rôle de la prévoyance pour un saisonnier de station.',
 'date': '2026-11-11',
 'minutes': 4,
 'cat': 'Arrêt de travail',
 'color': 'bg-teal',
 'icon': 'i-peak',
 'body': '\n<p class="lead-p">En station, les risques sont partout : neige, verglas, escaliers, cuisines, machines. Un saisonnier blessé pendant son travail, c\'est un accident du travail, avec des règles précises.</p>\n<h2>Accident du travail ou pas ?</h2>\n<ul>\n<li><strong>pendant le travail</strong> : c\'est un accident du travail, y compris pour un pisteur sur le domaine ou un serveur en terrasse ;</li>\n<li><strong>sur le trajet</strong> entre le logement et le travail : c\'est un accident de trajet ;</li>\n<li><strong>pendant son temps libre</strong>, en skiant pour lui-même : c\'est un accident de la vie privée.</li>\n</ul>\n<h2>Les démarches</h2>\n<ol>\n<li>porter secours et, si besoin, appeler les secours ;</li>\n<li>remettre la feuille d\'accident au salarié ;</li>\n<li>déclarer l\'accident à la Sécurité sociale dans les 48 heures ;</li>\n<li>noter précisément le lieu, l\'heure et les circonstances.</li>\n</ol>\n<h2>Le salaire pendant l\'arrêt</h2>\n<p>La Sécurité sociale verse des indemnités plus élevées en accident du travail qu\'en maladie. Le complément de l\'employeur dépend de la convention et de l\'ancienneté : beaucoup de saisonniers ont moins d\'un an d\'ancienneté et n\'y ont pas droit.</p>\n<h2>Le rôle de la prévoyance</h2>\n<p>Elle prend le relais si l\'arrêt dure, selon les règles de la convention. Dans les remontées mécaniques, selon l\'organisme recommandé, l\'indemnisation d\'un salarié de moins d\'un an d\'ancienneté intervient après 90 jours d\'arrêt continu ; son salaire de référence est reconstitué sur 12 mois.</p>\n<h2>La fin du contrat pendant l\'arrêt</h2>\n<p>Un CDD saisonnier se termine à sa date, même pendant un arrêt. Les indemnités de la Sécurité sociale et de la prévoyance déjà ouvertes continuent selon les règles du contrat.</p>\n<p>Voir notre page <a href="{{L:saisonniers}}">saisonniers</a> et le <a href="https://www.wealthwiseconseil.fr/guide-prevoyance">guide de la prévoyance</a> de WealthWise Conseil.</p>\n<div class="callout"><strong>Bonne Cordée s\'en occupe</strong>Un saisonnier blessé ? Nous vous guidons dans les démarches avec l\'assureur. <a href="{{L:devis}}">Demander mon étude gratuite</a>, ou appelez le 01 87 66 70 31.</div>'
},
{
 'slug': 'moniteur-ski-independant-proteger-revenus',
 'title': 'Moniteur de ski indépendant : protéger ses revenus de saison',
 'short': 'Moniteurs indépendants',
 'desc': "Un moniteur de ski indépendant n'a ni mutuelle d'entreprise ni maintien de salaire. Comment protéger un revenu concentré sur quelques mois, contrats Madelin compris.",
 'date': '2026-11-11',
 'minutes': 4,
 'cat': 'Indépendants',
 'color': 'bg-mustard',
 'icon': 'i-peak',
 'body': '\n<p class="lead-p">La plupart des moniteurs de ski exercent en indépendants. Leur revenu se gagne en quelques semaines de vacances scolaires, et s\'arrête net en cas de blessure. Leur protection sociale mérite d\'être pensée avant la saison.</p>\n<h2>Ce que vous n\'avez pas</h2>\n<ul>\n<li>pas de mutuelle d\'entreprise : vous la choisissez et la payez vous-même ;</li>\n<li>pas de maintien de salaire ;</li>\n<li>pas de prévoyance collective.</li>\n</ul>\n<h2>Ce que verse la Sécurité sociale</h2>\n<p>En arrêt, les indépendants touchent des indemnités journalières calculées sur leurs revenus des années passées, après un délai de carence. Pour un revenu saisonnier ou irrégulier, elles sont souvent faibles par rapport à ce que représente une semaine de février.</p>\n<h2>Ce qu\'une prévoyance individuelle apporte</h2>\n<ul>\n<li>des indemnités journalières dès les premiers jours si vous le choisissez ;</li>\n<li>une rente si une blessure vous empêche de reprendre le métier ;</li>\n<li>un capital décès pour votre famille.</li>\n</ul>\n<h2>Le piège des exclusions</h2>\n<p>Certains contrats excluent ou limitent les accidents liés aux sports de montagne ou à certaines activités professionnelles. Pour un moniteur, c\'est le premier point à vérifier.</p>\n<h2>La fiscalité</h2>\n<p>Au régime réel, les cotisations des contrats dits « Madelin » sont déductibles du bénéfice, dans certaines limites. En micro-entreprise, elles ne le sont pas.</p>\n<p>Voir notre page <a href="{{L:moniteurs-independants}}">indépendants</a> et le guide de WealthWise Conseil sur <a href="https://www.wealthwiseconseil.fr/prevoyance-tns-arret-maladie-perte-revenus">la prévoyance des indépendants</a>.</p>\n<div class="callout"><strong>Bonne Cordée s\'en occupe</strong>Nous comparons les contrats individuels et vérifions les exclusions liées à votre métier. <a href="{{L:devis}}">Demander mon étude gratuite</a>, ou appelez le 01 87 66 70 31.</div>'
},
{
 'slug': 'preparer-saison-hiver-checklist-protection-sociale',
 'title': "Préparer la saison d'hiver : la checklist mutuelle et prévoyance",
 'short': 'La checklist de la saison',
 'desc': "Avant l'arrivée des saisonniers : décision de l'employeur, kit d'arrivée, dispenses, versement santé, cadres. Une checklist simple pour ouvrir sereinement.",
 'date': '2026-11-11',
 'minutes': 4,
 'cat': 'Saisonniers',
 'color': 'bg-navy',
 'icon': 'i-rope',
 'body': '\n<p class="lead-p">Novembre, les recrutements se bouclent et l\'ouverture approche. C\'est le moment de vérifier que la protection sociale est prête, avant que les saisonniers n\'arrivent par dizaines.</p>\n<h2>En octobre et novembre</h2>\n<ol>\n<li><strong>Relire la décision de l\'employeur</strong> : couvre-t-elle tous les salariés, prévoit-elle les dispenses des contrats courts ?</li>\n<li><strong>Vérifier le contrat</strong> : garanties de votre convention, taux de prévoyance à jour (0,86 % de la tranche A en HCR, par exemple).</li>\n<li><strong>Préparer le kit d\'arrivée</strong> : décision de l\'employeur, notice de l\'assureur, formulaire de dispense.</li>\n<li><strong>Repérer les cadres</strong> : 1,50 % de la tranche A à votre charge.</li>\n</ol>\n<h2>À chaque arrivée</h2>\n<ul>\n<li>remise des documents contre signature ;</li>\n<li>affiliation déclarée à l\'assureur, ou dispense écrite et justifiée ;</li>\n<li>pour un CDD de moins de 3 mois dispensé : calcul du versement santé.</li>\n</ul>\n<h2>Pendant la saison</h2>\n<ul>\n<li>un tableau de suivi : nom, dates, affilié ou dispensé, versement santé ;</li>\n<li>les arrêts déclarés à l\'assureur dès qu\'ils se prolongent.</li>\n</ul>\n<h2>En fin de saison</h2>\n<ul>\n<li>portabilité mentionnée sur chaque certificat de travail ;</li>\n<li>sorties signalées à l\'assureur ;</li>\n<li>bilan : coût, sinistres, et remise en concurrence à l\'intersaison si besoin.</li>\n</ul>\n<p>Notre <a href="{{L:outils}}#checkup">check-up « prêt pour la saison »</a> fait le point en neuf questions. Le guide de WealthWise Conseil sur <a href="https://www.wealthwiseconseil.fr/due-decision-unilaterale-employeur-guide">la décision de l\'employeur</a> détaille son contenu.</p>\n<div class="callout"><strong>Bonne Cordée s\'en occupe</strong>Nous préparons votre saison : documents, affiliations, versements santé, fin de saison. <a href="{{L:devis}}">Demander mon étude gratuite</a>, ou appelez le 01 87 66 70 31.</div>'
},
{
 'slug': 'contrats-courts-dispenses-erreurs-frequentes-station',
 'title': 'Contrats courts et dispenses : les erreurs fréquentes en station',
 'short': 'Les erreurs fréquentes',
 'desc': 'Dispense orale, versement santé oublié, saisonnier de 4 mois dispensé à tort : les erreurs les plus fréquentes en station, et comment les éviter.',
 'date': '2026-11-11',
 'minutes': 4,
 'cat': 'Saisonniers',
 'color': 'bg-red',
 'icon': 'i-chalet',
 'body': '\n<p class="lead-p">Avec des dizaines de contrats courts chaque saison, les erreurs de protection sociale sont fréquentes. Elles ne se voient pas tout de suite, mais elles coûtent cher lors d\'un contrôle ou d\'un sinistre.</p>\n<h2>1. La dispense orale</h2>\n<p>« Il m\'a dit qu\'il avait déjà une mutuelle. » Sans demande écrite et justificatif, la dispense n\'existe pas : le saisonnier aurait dû être affilié.</p>\n<h2>2. Le saisonnier de 4 mois dispensé « contrat court »</h2>\n<p>La dispense des contrats courts vise les contrats de moins de 3 mois. Au-delà, il faut un autre motif, par exemple une couverture collective obligatoire par ailleurs.</p>\n<h2>3. Le versement santé oublié</h2>\n<p>Un CDD de moins de 3 mois dispensé, avec une mutuelle responsable, a droit au versement santé : participation × 125 %, ou 27,84 € par mois en référence 2026 à temps plein.</p>\n<h2>4. La décision de l\'employeur jamais remise</h2>\n<p>Chaque saisonnier doit la recevoir à son arrivée, avec une preuve. Sinon, l\'exonération de cotisations peut être remise en cause.</p>\n<h2>5. La prévoyance oubliée</h2>\n<p>Les dispenses concernent la mutuelle. La prévoyance de votre convention s\'applique aux saisonniers.</p>\n<h2>6. Le chef cadre sans prévoyance cadres</h2>\n<p>Pour un cadre, 1,50 % de la tranche A est obligatoire. Sans contrat, 144 180 € en cas de décès en 2026.</p>\n<h2>7. La portabilité non mentionnée</h2>\n<p>Elle doit figurer sur le certificat de travail en fin de saison.</p>\n<p>Voir notre page <a href="{{L:saisonniers}}">saisonniers</a> et le guide de WealthWise Conseil sur <a href="https://www.wealthwiseconseil.fr/dispenses-affiliation-mutuelle-cas-autorises">les dispenses autorisées</a>.</p>\n<div class="callout"><strong>Bonne Cordée s\'en occupe</strong>Nous auditons votre saison passée et corrigeons ces points avant la prochaine. <a href="{{L:devis}}">Demander mon étude gratuite</a>, ou appelez le 01 87 66 70 31.</div>'
},
{
 'slug': 'restaurant-altitude-cadre-prevoyance-1-50',
 'title': "Chef de cuisine ou directeur d'hôtel cadre : la prévoyance à 1,50 %",
 'short': 'Cadres : 1,50 % de tranche A',
 'desc': "Un salarié cadre impose 1,50 % de prévoyance sur la tranche A, à la charge de l'employeur. Sans contrat, 144 180 € dus en cas de décès en 2026.",
 'date': '2026-11-11',
 'minutes': 3,
 'cat': 'Cadres',
 'color': 'bg-teal',
 'icon': 'i-lift',
 'body': '\n<p class="lead-p">Directeur d\'hôtel, chef de cuisine, responsable d\'exploitation d\'un domaine skiable : en station aussi, les cadres ont une règle de prévoyance particulière, et son oubli coûte très cher.</p>\n<h2>La règle</h2>\n<p>Pour chaque cadre, l\'employeur consacre au moins 1,50 % de la tranche A du salaire à la prévoyance, en priorité à une garantie décès. La tranche A est la partie du salaire jusqu\'au plafond de la Sécurité sociale, 4 005 € par mois en 2026. Cette cotisation est à la charge de l\'employeur.</p>\n<h2>Exemple</h2>\n<p>Un chef de cuisine cadre payé 3 800 € par mois pendant la saison : l\'employeur verse au moins 57 € par mois pour sa prévoyance cadres.</p>\n<h2>La sanction</h2>\n<p>Si un cadre décède sans que cette cotisation ait été versée, l\'employeur doit à sa famille un capital de trois plafonds annuels de la Sécurité sociale : 144 180 € en 2026.</p>\n<h2>Selon la convention</h2>\n<ul>\n<li>hôtels, cafés, restaurants : la prévoyance cadres s\'ajoute aux règles de la branche ;</li>\n<li>remontées mécaniques : chez l\'organisme recommandé, le régime des cadres est financé par l\'employeur à hauteur de 1,50 % de la tranche 1.</li>\n</ul>\n<h2>À vérifier</h2>\n<ul>\n<li>le statut de vos responsables, y compris les saisonniers cadres ;</li>\n<li>un contrat cadre en place dès l\'embauche ou la promotion.</li>\n</ul>\n<p>Voir notre page <a href="{{L:obligations-montagne}}">obligations</a> et le guide de WealthWise Conseil sur <a href="https://www.wealthwiseconseil.fr/prevoyance-cadres-obligation-agirc-article-7">la prévoyance cadres obligatoire</a>.</p>\n<div class="callout"><strong>Bonne Cordée s\'en occupe</strong>Nous vérifions que chaque cadre est couvert dès son arrivée. <a href="{{L:devis}}">Demander mon étude gratuite</a>, ou appelez le 01 87 66 70 31.</div>'
},
]
