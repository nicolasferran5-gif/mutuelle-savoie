# -*- coding: utf-8 -*-
"""Guides de fond communs à tous les sites (droit commun de la mutuelle et de la prévoyance d'entreprise).

Chaque guide est écrit une fois, puis adapté au site par trois variables :
  {pub}  le public du site, avec son article ("des hôtels, cafés, bars et restaurants")
  {conv} la convention collective du site
  {ob}   le lien vers la page « obligations » du site, qui porte les chiffres propres à la convention
Chiffres : barèmes 2026 (plafond mensuel 4 005 €, plafond annuel 48 060 €). À relire chaque mois de janvier.
"""

MAJ = "2026-11-13"

GUIDES = [
    {
        "slug": "mettre-en-place-mutuelle-entreprise",
        "cat": "Mise en place",
        "title": "Mettre en place une mutuelle d'entreprise {pub} : les 6 étapes",
        "desc": "Choix du contrat, écrit de mise en place, information des salariés, affiliations et dispenses, paie : la marche à suivre pour l'employeur, étape par étape.",
        "body": """
<p class="lead-p">Tout employeur du secteur privé doit proposer une mutuelle à ses salariés, dès le premier. Pour les employeurs {pub}, s'ajoutent les règles de {conv}. Voici l'ordre dans lequel procéder pour être en règle sans y passer des semaines.</p>
<h2>Qui doit mettre en place une mutuelle d'entreprise ?</h2>
<p>Toutes les entreprises du secteur privé, quelle que soit leur taille, depuis le 1er janvier 2016. L'obligation commence à la première embauche, y compris pour un salarié à temps partiel ou un apprenti. Le dirigeant, lui, n'est couvert par ce contrat que s'il a un statut de salarié.</p>
<h2>Étape 1 : vérifier ce que votre convention impose</h2>
<p>La loi fixe un socle minimal, mais votre convention collective peut exiger davantage : un niveau de garanties plus élevé, une part employeur supérieure à 50 %, une ancienneté maximale avant affiliation, voire un organisme recommandé. C'est le point de départ, car un contrat conforme à la loi mais pas à la convention expose l'employeur. Les règles propres à votre branche sont détaillées dans <a href="{ob}">notre page sur vos obligations</a>.</p>
<h2>Étape 2 : choisir le contrat et sa structure de cotisation</h2>
<p>Trois décisions pèsent sur le prix : le niveau de garanties (le minimum de la branche ou mieux), la structure de cotisation (tarif unique, « isolé / famille » ou « adulte / enfant ») et la présence d'options facultatives payées par les salariés. Un courtier met plusieurs assureurs en concurrence sur le même cahier des charges, ce qui permet de comparer des offres réellement comparables.</p>
<h2>Étape 3 : rédiger l'écrit qui met en place le régime</h2>
<p>La mutuelle se met en place par l'un de ces trois actes :</p>
<ul>
<li><strong>une décision unilatérale de l'employeur</strong>, le cas le plus fréquent dans les petites entreprises ;</li>
<li><strong>un accord collectif</strong>, négocié avec les représentants du personnel ;</li>
<li><strong>un référendum</strong>, c'est-à-dire un projet de l'employeur approuvé par la majorité des salariés.</li>
</ul>
<p>Cet écrit précise les salariés concernés, les garanties, la répartition de la cotisation et les cas de dispense. Il doit être remis à chaque salarié, avec une preuve de remise (émargement ou accusé de réception). Sans cette preuve, l'URSSAF peut remettre en cause les exonérations de charges.</p>
<h2>Étape 4 : informer les salariés et recueillir les dispenses</h2>
<p>Chaque salarié reçoit la notice d'information de l'assureur. Ceux qui peuvent et veulent refuser la mutuelle remplissent une demande de dispense écrite, datée et signée, accompagnée du justificatif prévu. L'employeur conserve ces documents : ce sont eux que le contrôleur demandera.</p>
<h2>Étape 5 : affilier et paramétrer la paie</h2>
<p>Les salariés sont affiliés auprès de l'assureur, puis la cotisation est ajoutée au bulletin de paie : part salariale en retenue, part employeur en avantage soumis à la CSG et à la CRDS. La déclaration sociale nominative transmet ensuite les informations à l'assureur chaque mois.</p>
<h2>Étape 6 : faire vivre le contrat</h2>
<p>Un régime se suit dans le temps : affiliation à chaque embauche, portabilité à chaque départ, mise à jour de l'écrit quand la convention change, remise en concurrence quand le tarif dérive. C'est la partie la plus souvent négligée, et celle que nous prenons en charge pour nos clients.</p>
<h2>Combien de temps faut-il ?</h2>
<p>Comptez deux à quatre semaines entre la première demande et l'affiliation des salariés : quelques jours pour le comparatif, une à deux semaines pour le choix et la rédaction de l'écrit, puis les affiliations.</p>
""",
        "faq": [
            ("La mutuelle d'entreprise est-elle obligatoire dès le premier salarié ?", "Oui. Depuis le 1er janvier 2016, tout employeur du secteur privé doit proposer une complémentaire santé collective à ses salariés, dès la première embauche, et en financer au moins la moitié."),
            ("Peut-on mettre en place la mutuelle sans accord des salariés ?", "Oui, par une décision unilatérale de l'employeur. Les salariés déjà présents peuvent alors refuser d'y adhérer si une part de la cotisation est à leur charge."),
            ("Que risque un employeur sans mutuelle d'entreprise ?", "Un salarié peut lui réclamer le remboursement de ses frais de santé et des dommages et intérêts. En cas de contrat non conforme, l'URSSAF peut réintégrer la part employeur dans l'assiette des cotisations sociales."),
        ],
    },
    {
        "slug": "dispenses-mutuelle-entreprise",
        "cat": "Dispenses",
        "title": "Dispense de mutuelle d'entreprise : les cas autorisés pour les salariés {pub}",
        "desc": "Qui peut refuser la mutuelle de l'entreprise, avec quel justificatif et jusqu'à quand : les dispenses de droit et celles que l'employeur doit prévoir par écrit.",
        "body": """
<p class="lead-p">La mutuelle d'entreprise est obligatoire, mais certains salariés peuvent la refuser. Les cas sont limités et chaque refus doit être écrit. Pour les employeurs {pub}, c'est le premier point contrôlé par l'URSSAF.</p>
<h2>Un salarié peut-il refuser la mutuelle de l'entreprise ?</h2>
<p>Oui, mais seulement s'il entre dans un cas de dispense prévu par les textes, et à sa demande. L'employeur ne peut ni imposer une dispense, ni en inventer une. Il existe deux familles de dispenses : celles que le salarié peut faire valoir dans toutes les entreprises, et celles qui n'existent que si l'écrit de mise en place les prévoit.</p>
<h2>Les dispenses que tout salarié peut demander</h2>
<div class="table-wrap"><table>
<thead><tr><th>Situation du salarié</th><th>Justificatif</th><th>Durée</th></tr></thead>
<tbody>
<tr><td>Bénéficiaire de la complémentaire santé solidaire</td><td>Attestation de droits</td><td>Tant que l'aide est versée</td></tr>
<tr><td>Déjà couvert par un contrat individuel au moment de l'embauche ou de la mise en place</td><td>Attestation du contrat</td><td>Jusqu'à l'échéance du contrat individuel</td></tr>
<tr><td>Déjà couvert par un autre régime collectif obligatoire, y compris par celui de son conjoint</td><td>Attestation à fournir chaque année</td><td>Tant que la couverture dure</td></tr>
<tr><td>Contrat court dont la couverture obligatoire durerait moins de 3 mois, avec une mutuelle responsable par ailleurs</td><td>Attestation de la mutuelle personnelle</td><td>Durée du contrat</td></tr>
<tr><td>Salarié présent avant une mise en place par décision de l'employeur, si une part de la cotisation est à sa charge</td><td>Refus écrit</td><td>Sans limite</td></tr>
</tbody></table></div>
<h2>Les dispenses à prévoir dans l'écrit de mise en place</h2>
<p>Ces cas ne valent que s'ils figurent dans la décision de l'employeur ou dans l'accord :</p>
<ul>
<li>les salariés en contrat à durée déterminée et les apprentis dont le contrat dure <strong>au moins 12 mois</strong>, s'ils justifient d'une couverture individuelle ;</li>
<li>les salariés en contrat à durée déterminée et les apprentis dont le contrat dure <strong>moins de 12 mois</strong>, même sans autre couverture ;</li>
<li>les salariés à temps partiel et les apprentis pour qui la cotisation représenterait <strong>au moins 10 % de leur rémunération brute</strong>.</li>
</ul>
<p>Votre convention collective peut ajouter ou encadrer certains cas : vérifiez-les dans <a href="{ob}">notre page sur vos obligations</a>.</p>
<h2>Comment doit se présenter la demande ?</h2>
<p>La demande est écrite, datée et signée par le salarié. Elle mentionne le cas invoqué et indique que le salarié a été informé des conséquences de son choix : il renonce à la part payée par l'employeur et à la portabilité. L'employeur la conserve avec le justificatif, et redemande ce justificatif chaque année quand la dispense dépend d'une autre couverture.</p>
<h2>Que se passe-t-il si une dispense n'est pas justifiée ?</h2>
<p>Le régime peut perdre son caractère collectif et obligatoire. L'URSSAF est alors en droit de soumettre à cotisations sociales la part employeur versée pour l'ensemble des salariés, avec un redressement qui peut remonter sur trois ans. Un salarié non affilié et non dispensé peut aussi réclamer à l'employeur le remboursement de ses frais de santé.</p>
<h2>Et le versement santé ?</h2>
<p>Les salariés en contrat très court ou à temps très partiel qui ont fait valoir une dispense et financent eux-mêmes une mutuelle responsable peuvent recevoir de l'employeur une aide appelée versement santé. Elle remplace la part employeur qu'ils n'ont pas reçue.</p>
""",
        "faq": [
            ("Un salarié couvert par la mutuelle de son conjoint peut-il refuser celle de l'entreprise ?", "Oui, si la mutuelle du conjoint est un régime collectif et obligatoire qui le couvre en tant qu'ayant droit. Il doit fournir une attestation chaque année."),
            ("Une dispense de mutuelle peut-elle être donnée oralement ?", "Non. La demande doit être écrite et signée par le salarié, et conservée par l'employeur avec le justificatif. Une dispense orale n'a aucune valeur lors d'un contrôle."),
            ("Un salarié dispensé peut-il changer d'avis ?", "Oui. Il peut demander à tout moment à rejoindre la mutuelle de l'entreprise, et doit le faire dès que sa situation ne correspond plus au cas de dispense."),
        ],
    },
    {
        "slug": "changer-de-mutuelle-entreprise",
        "cat": "Changer de contrat",
        "title": "Changer de mutuelle d'entreprise : quand et comment résilier",
        "desc": "Résiliation à tout moment après un an pour la mutuelle, à l'échéance pour la prévoyance : les délais, les étapes et les documents à mettre à jour côté employeur.",
        "body": """
<p class="lead-p">Un tarif qui augmente chaque année, un service de gestion injoignable, une convention qui a changé : les raisons de changer de contrat ne manquent pas. Les employeurs {pub} peuvent le faire plus facilement qu'ils ne le pensent, à condition de respecter l'ordre des étapes.</p>
<h2>Quand peut-on résilier une mutuelle d'entreprise ?</h2>
<p>Deux possibilités coexistent :</p>
<ul>
<li><strong>À tout moment après un an de contrat.</strong> Depuis le 1er décembre 2020, un contrat de complémentaire santé peut être résilié sans frais ni justification une fois la première année écoulée. La résiliation prend effet un mois après la réception de la demande par l'assureur.</li>
<li><strong>À l'échéance annuelle</strong>, en général le 31 décembre, en respectant le préavis prévu au contrat, le plus souvent deux mois.</li>
</ul>
<h2>Et pour la prévoyance ?</h2>
<p>La résiliation à tout moment ne concerne pas les contrats de prévoyance. Ils se résilient à l'échéance annuelle, avec le préavis prévu au contrat. Il faut donc anticiper : pour un contrat qui se termine le 31 décembre avec deux mois de préavis, la lettre doit partir avant la fin du mois d'octobre.</p>
<div class="callout"><strong>À retenir</strong>Un changement de prévoyance se prépare avec soin quand des salariés sont en arrêt de travail : le nouvel assureur doit reprendre les engagements en cours, et ce point se négocie avant de résilier.</div>
<h2>Les étapes, dans l'ordre</h2>
<ol>
<li><strong>Comparer avant de résilier.</strong> On ne résilie qu'une fois le nouveau contrat choisi, pour ne laisser aucun salarié sans couverture.</li>
<li><strong>Vérifier la conformité du nouveau contrat</strong> à votre convention collective : garanties minimales, part employeur, catégories de salariés. Voir <a href="{ob}">vos obligations</a>.</li>
<li><strong>Mettre à jour l'écrit de mise en place</strong> si les garanties, la cotisation ou sa répartition changent, et le remettre aux salariés.</li>
<li><strong>Résilier l'ancien contrat.</strong> Le nouvel assureur peut s'en charger pour vous, sur mandat.</li>
<li><strong>Informer les salariés</strong> et leur remettre la nouvelle notice d'information.</li>
<li><strong>Transférer la portabilité</strong> : les anciens salariés qui en bénéficient passent sur le nouveau contrat.</li>
</ol>
<h2>Faut-il consulter les représentants du personnel ?</h2>
<p>Dans les entreprises dotées d'un comité social et économique, celui-ci est informé et consulté avant toute modification des garanties collectives. Si le régime a été mis en place par accord collectif ou par référendum, sa modification suit la même voie.</p>
<h2>Que deviennent les salariés pendant le changement ?</h2>
<p>Rien ne change pour eux si les dates sont bien enchaînées : l'ancien contrat s'arrête la veille du jour où le nouveau commence. Ils reçoivent une nouvelle carte de tiers payant et, si besoin, les identifiants de leur nouvel espace en ligne.</p>
<h2>Quand cela vaut-il la peine de changer ?</h2>
<p>Trois signaux doivent alerter : une hausse de tarif deux années de suite sans explication chiffrée, un contrat qui n'a pas suivi les dernières évolutions de la convention, ou des salariés qui se plaignent des remboursements ou des délais. Dans ces cas, une mise en concurrence prend quelques jours et ne coûte rien.</p>
""",
        "faq": [
            ("Peut-on changer de mutuelle d'entreprise en cours d'année ?", "Oui, dès que le contrat a plus d'un an. La résiliation prend effet un mois après la réception de la demande par l'assureur, sans frais ni pénalité."),
            ("Qui s'occupe de la résiliation de l'ancien contrat ?", "L'employeur peut envoyer lui-même la demande, ou donner mandat au nouvel assureur ou à son courtier, qui s'en charge à sa place."),
            ("Les salariés doivent-ils donner leur accord pour changer de mutuelle ?", "Non si le régime résulte d'une décision de l'employeur, mais ils doivent être informés et recevoir le nouvel écrit et la nouvelle notice. Un accord collectif ou un référendum se modifie dans les mêmes formes."),
        ],
    },
    {
        "slug": "prevoyance-collective-obligatoire",
        "cat": "Prévoyance",
        "title": "Prévoyance d'entreprise : est-elle obligatoire pour les employeurs {pub} ?",
        "desc": "Cadres, non-cadres, maintien de salaire, arrêt de travail, invalidité, décès : ce que la loi et les conventions imposent, et comment la prévoyance prend le relais.",
        "body": """
<p class="lead-p">Contrairement à la mutuelle, la prévoyance n'est pas imposée à tous les employeurs par une loi unique. Elle devient obligatoire par deux voies : le statut de cadre et la convention collective. Les employeurs {pub} sont concernés par les deux.</p>
<h2>À quoi sert la prévoyance ?</h2>
<p>Elle protège le revenu du salarié et de sa famille quand il ne peut plus travailler :</p>
<ul>
<li><strong>arrêt de travail</strong> : des indemnités qui complètent celles de la Sécurité sociale ;</li>
<li><strong>invalidité</strong> : une rente qui complète la pension d'invalidité ;</li>
<li><strong>décès</strong> : un capital versé aux proches, parfois une rente pour le conjoint ou pour les études des enfants.</li>
</ul>
<h2>Pour les cadres : une obligation nationale</h2>
<p>Tout employeur doit financer seul, pour chacun de ses cadres, une prévoyance d'au moins <strong>1,50 % de la tranche A du salaire</strong>, c'est-à-dire de la part du salaire comprise sous le plafond de la Sécurité sociale (4 005 € par mois en 2026). Cette cotisation doit être affectée en priorité au risque décès. Pour un cadre payé au plafond ou au-dessus, cela représente au plus 60,08 € par mois.</p>
<div class="callout"><strong>La sanction</strong>Si un cadre décède alors que l'employeur n'a pas souscrit ce contrat, l'entreprise doit verser elle-même à ses proches un capital égal à trois plafonds annuels de la Sécurité sociale, soit 144 180 € en 2026.</div>
<h2>Pour les non-cadres : la convention collective décide</h2>
<p>La plupart des conventions imposent une prévoyance aux non-cadres, avec un taux de cotisation, une répartition entre employeur et salarié et des garanties minimales. Les règles de {conv} sont détaillées dans <a href="{ob}">notre page sur vos obligations</a>.</p>
<h2>Le maintien de salaire : ce que l'employeur doit déjà</h2>
<p>Même sans contrat de prévoyance, la loi oblige l'employeur à compléter les indemnités de la Sécurité sociale pendant un arrêt maladie, pour les salariés qui ont au moins un an d'ancienneté :</p>
<div class="table-wrap"><table>
<thead><tr><th>Période</th><th>Rémunération maintenue</th><th>Durée</th></tr></thead>
<tbody>
<tr><td>Première période</td><td>90 % du salaire brut</td><td>30 jours, plus 10 jours par tranche de 5 ans d'ancienneté</td></tr>
<tr><td>Seconde période</td><td>Deux tiers du salaire brut</td><td>30 jours, plus 10 jours par tranche de 5 ans d'ancienneté</td></tr>
</tbody></table></div>
<p>Chaque période est plafonnée à 90 jours. En cas de maladie ordinaire, le versement commence après 7 jours d'arrêt. Beaucoup de conventions prévoient mieux : une ancienneté plus courte, un délai réduit ou un taux supérieur.</p>
<h2>Simulateur : qui paie quoi pendant un arrêt maladie ?</h2>
<p>Choisissez l'ancienneté du salarié et déplacez le curseur : vous voyez d'où vient son revenu, jour après jour, selon la loi.</p>
{sim}
<h2>Comment la prévoyance prend-elle le relais ?</h2>
<p>Le contrat de prévoyance intervient de deux façons. Il peut rembourser à l'employeur le maintien de salaire qu'il verse, ce qui protège la trésorerie d'une petite entreprise. Et il prend la suite quand le maintien de salaire s'arrête, pour que le salarié ne tombe pas aux seules indemnités de la Sécurité sociale. Le point à surveiller est la franchise : le nombre de jours après lequel l'assureur commence à payer doit correspondre à la fin du maintien de salaire.</p>
<h2>Combien coûte une prévoyance ?</h2>
<p>La cotisation s'exprime en pourcentage du salaire brut. Elle dépend des garanties, de l'âge moyen de l'équipe, du métier et du nombre d'arrêts passés. À garanties égales, les écarts entre assureurs sont réels, ce qui justifie de comparer.</p>
""",
        "faq": [
            ("La prévoyance est-elle obligatoire dans toutes les entreprises ?", "Elle l'est pour tous les cadres, à hauteur de 1,50 % de la tranche A du salaire à la charge de l'employeur. Pour les non-cadres, elle est obligatoire quand la convention collective le prévoit, ce qui est le cas de la plupart des branches."),
            ("Quelle différence entre mutuelle et prévoyance ?", "La mutuelle rembourse les frais de santé. La prévoyance remplace le revenu perdu en cas d'arrêt de travail, d'invalidité ou de décès."),
            ("Qui paie la prévoyance des cadres ?", "L'employeur, seul, pour la cotisation minimale de 1,50 % de la tranche A. Des garanties supplémentaires peuvent être partagées avec le salarié."),
        ],
    },
    {
        "slug": "cout-mutuelle-entreprise-employeur",
        "cat": "Coût",
        "title": "Coût d'une mutuelle d'entreprise pour l'employeur : calcul, charges et exonérations",
        "desc": "Part employeur de 50 % au moins, CSG et CRDS, forfait social dès 11 salariés, plafond d'exonération : ce que coûte réellement une mutuelle d'entreprise en 2026.",
        "body": """
<p class="lead-p">Le prix affiché par l'assureur n'est qu'une partie du coût. Pour les employeurs {pub}, le budget réel dépend de la part prise en charge, des contributions sociales et de la façon dont la cotisation est structurée.</p>
<h2>Quelle part l'employeur doit-il payer ?</h2>
<p>Au moins 50 % de la cotisation qui finance la couverture obligatoire du salarié. Rien n'oblige à financer la part du conjoint et des enfants, ni les options facultatives. Votre convention collective peut imposer une part plus élevée : vérifiez-le dans <a href="{ob}">notre page sur vos obligations</a>.</p>
<h2>La part employeur est-elle soumise à cotisations ?</h2>
<p>Quand le contrat est collectif, obligatoire et responsable, la part payée par l'employeur est exonérée de cotisations de Sécurité sociale, dans une limite annuelle par salarié. Elle reste soumise à deux prélèvements.</p>
<div class="table-wrap"><table>
<thead><tr><th>Prélèvement</th><th>Taux</th><th>Qui est concerné</th></tr></thead>
<tbody>
<tr><td>CSG et CRDS</td><td>9,70 % de la part employeur</td><td>Toutes les entreprises, retenue sur le salaire du salarié</td></tr>
<tr><td>Forfait social</td><td>8 % de la part employeur</td><td>Entreprises de 11 salariés et plus, à la charge de l'employeur</td></tr>
</tbody></table></div>
<h2>Quel est le plafond d'exonération ?</h2>
<p>Les contributions de l'employeur à la mutuelle et à la prévoyance sont exonérées dans la limite, par salarié et par an, de 6 % du plafond annuel de la Sécurité sociale plus 1,5 % de sa rémunération, sans dépasser 12 % du plafond annuel. En 2026, avec un plafond de 48 060 €, cela donne 2 883,60 € plus 1,5 % du salaire, dans la limite de 5 767,20 €. Les contrats courants restent très en dessous.</p>
<h2>Et pour le salarié ?</h2>
<p>Sa part est retenue sur son salaire et déductible de son revenu imposable, dans certaines limites. En revanche, la part payée par l'employeur pour la mutuelle s'ajoute à son revenu imposable : c'est la raison pour laquelle le net imposable du bulletin de paie est supérieur au net versé.</p>
<h2>Un exemple de calcul</h2>
<p>Prenons une cotisation de 50 € par mois pour un salarié, financée à 50 % par l'employeur, dans une entreprise de 15 salariés. Le montant de la cotisation est une hypothèse, choisie pour illustrer le calcul.</p>
<div class="table-wrap"><table>
<thead><tr><th>Ligne</th><th>Calcul</th><th>Montant mensuel</th></tr></thead>
<tbody>
<tr><td>Part employeur</td><td>50 % de 50 €</td><td>25,00 €</td></tr>
<tr><td>Forfait social</td><td>8 % de 25 €</td><td>2,00 €</td></tr>
<tr><td><strong>Coût pour l'employeur</strong></td><td></td><td><strong>27,00 €</strong></td></tr>
<tr><td>Part du salarié</td><td>50 % de 50 €</td><td>25,00 €</td></tr>
<tr><td>CSG et CRDS retenues au salarié</td><td>9,70 % de 25 €</td><td>2,43 €</td></tr>
</tbody></table></div>
<h2>Calculez votre coût employeur</h2>
<p>Saisissez la cotisation de votre contrat, la part que vous prenez en charge et votre effectif.</p>
{calc}
<h2>Qu'est-ce qui fait varier le prix d'un contrat ?</h2>
<ul>
<li><strong>le niveau de garanties</strong> : minimum de la branche ou couverture renforcée ;</li>
<li><strong>la structure de cotisation</strong> : tarif unique, « isolé / famille » ou « adulte / enfant » ;</li>
<li><strong>l'âge moyen et la composition de l'équipe</strong> ;</li>
<li><strong>la région et le métier</strong> ;</li>
<li><strong>les remboursements passés</strong>, pour les contrats de plus d'un an.</li>
</ul>
<h2>Comment réduire la facture sans dégrader la couverture ?</h2>
<p>Trois leviers fonctionnent : caler la part employeur sur la seule couverture obligatoire du salarié, rendre facultatives les garanties que peu de salariés utilisent, et remettre le contrat en concurrence avec des données précises sur l'équipe. Le troisième est celui qui rapporte le plus, et celui pour lequel un courtier est utile.</p>
""",
        "faq": [
            ("Quelle est la part minimale de l'employeur dans la mutuelle d'entreprise ?", "50 % de la cotisation correspondant à la couverture obligatoire du salarié. La convention collective peut prévoir davantage."),
            ("Le forfait social s'applique-t-il aux petites entreprises ?", "Non. Le forfait social de 8 % sur la part employeur de la mutuelle et de la prévoyance ne concerne que les entreprises de 11 salariés et plus."),
            ("La mutuelle d'entreprise est-elle déductible pour l'employeur ?", "Oui. La part employeur est une charge déductible du résultat de l'entreprise. Elle est en outre exonérée de cotisations de Sécurité sociale dans une limite annuelle, si le contrat est collectif, obligatoire et responsable."),
        ],
    },
    {
        "slug": "portabilite-mutuelle-prevoyance",
        "cat": "Départ d'un salarié",
        "title": "Portabilité de la mutuelle et de la prévoyance : les règles pour l'employeur",
        "desc": "Qui y a droit, pendant combien de temps, qui paie et ce que l'employeur doit faire au départ d'un salarié : la portabilité expliquée étape par étape.",
        "body": """
<p class="lead-p">Quand un salarié quitte l'entreprise, il peut garder gratuitement sa mutuelle et sa prévoyance pendant un temps. Pour les employeurs {pub}, où les départs sont fréquents, c'est une formalité à ne pas oublier.</p>
<h2>Qu'est-ce que la portabilité ?</h2>
<p>C'est le maintien, sans cotisation, des garanties de mutuelle et de prévoyance de l'entreprise au profit d'un ancien salarié indemnisé par l'assurance chômage. Elle existe dans toutes les entreprises du secteur privé.</p>
<h2>Qui y a droit ?</h2>
<p>L'ancien salarié doit remplir trois conditions :</p>
<ul>
<li>son contrat de travail a pris fin pour un motif ouvrant droit à l'assurance chômage : licenciement, sauf faute lourde, rupture conventionnelle, fin de contrat à durée déterminée, démission reconnue légitime ;</li>
<li>il était couvert par le contrat de l'entreprise avant son départ ;</li>
<li>il justifie auprès de l'assureur de sa prise en charge par l'assurance chômage.</li>
</ul>
<p>Un salarié qui avait fait valoir une dispense n'a pas droit à la portabilité de la mutuelle.</p>
<h2>Combien de temps dure-t-elle ?</h2>
<p>Aussi longtemps que le dernier contrat de travail, ou que les derniers contrats successifs chez le même employeur, dans la limite de <strong>12 mois</strong>. Elle s'arrête plus tôt si l'ancien salarié retrouve un emploi ou cesse d'être indemnisé.</p>
<div class="table-wrap"><table>
<thead><tr><th>Durée du dernier contrat</th><th>Durée de la portabilité</th></tr></thead>
<tbody>
<tr><td>2 mois</td><td>2 mois</td></tr>
<tr><td>8 mois</td><td>8 mois</td></tr>
<tr><td>3 ans</td><td>12 mois (plafond)</td></tr>
</tbody></table></div>
<h2>Qui paie ?</h2>
<p>Ni l'ancien salarié, ni l'employeur directement : le coût est mutualisé, c'est-à-dire intégré aux cotisations payées par l'entreprise et les salariés en poste.</p>
<h2>Ce que l'employeur doit faire</h2>
<ol>
<li><strong>Mentionner la portabilité sur le certificat de travail</strong> remis au salarié.</li>
<li><strong>Informer l'assureur</strong> de la fin du contrat de travail.</li>
<li><strong>Conserver la trace</strong> de ces deux démarches.</li>
</ol>
<div class="callout"><strong>À retenir</strong>Si l'employeur oublie d'informer le salarié ou l'assureur et que l'ancien salarié se retrouve sans couverture, celui-ci peut lui demander réparation.</div>
<h2>Quelles garanties sont maintenues ?</h2>
<p>Celles en vigueur dans l'entreprise : si le contrat change pendant la période, l'ancien salarié suit le nouveau contrat. Ses ayants droit déjà couverts restent couverts. En prévoyance, les indemnités versées ne peuvent pas dépasser le montant des allocations chômage qu'il aurait perçues.</p>
<h2>Et après la portabilité ?</h2>
<p>L'ancien salarié peut demander à l'assureur, dans les six mois, un contrat individuel aux garanties proches, à tarif encadré les premières années. C'est une démarche personnelle, qui ne concerne plus l'employeur.</p>
""",
        "faq": [
            ("La portabilité de la mutuelle est-elle payante pour l'ancien salarié ?", "Non. Elle est gratuite pour lui : son coût est intégré aux cotisations de l'entreprise et des salariés en poste."),
            ("Un salarié qui démissionne a-t-il droit à la portabilité ?", "Seulement si sa démission est reconnue légitime par l'assurance chômage et qu'il est indemnisé. Une démission ordinaire n'ouvre pas droit à la portabilité."),
            ("Combien de temps dure la portabilité ?", "Une durée égale à celle du dernier contrat de travail, dans la limite de 12 mois."),
        ],
    },
    {
        "slug": "versement-sante-contrats-courts",
        "cat": "Contrats courts",
        "title": "Versement santé : l'aide de l'employeur pour les contrats courts et les temps très partiels",
        "desc": "Qui a droit au versement santé, comment le calculer en 2026 (montant de référence de 22,27 €, coefficients de 105 % et 125 %) et comment le mettre en place.",
        "body": """
<p class="lead-p">Certains salariés ne restent pas assez longtemps, ou ne travaillent pas assez d'heures, pour que la mutuelle de l'entreprise ait un sens. Pour eux existe le versement santé. Les employeurs {pub} y recourent souvent pour les contrats très courts.</p>
<h2>Qu'est-ce que le versement santé ?</h2>
<p>Une somme versée chaque mois par l'employeur à un salarié qui n'est pas couvert par la mutuelle de l'entreprise, pour l'aider à payer sa mutuelle personnelle. Elle remplace la part employeur qu'il n'a pas reçue.</p>
<h2>Quels salariés sont concernés ?</h2>
<ul>
<li>les salariés en contrat à durée déterminée ou en contrat de mission dont la durée ne dépasse pas <strong>3 mois</strong> ;</li>
<li>les salariés à temps partiel dont la durée de travail ne dépasse pas <strong>15 heures par semaine</strong>.</li>
</ul>
<p>Ils doivent être couverts par ailleurs par un contrat de complémentaire santé responsable, qu'ils financent eux-mêmes, et en justifier. Le salarié qui bénéficie de la complémentaire santé solidaire ou d'une autre couverture collective obligatoire n'y a pas droit.</p>
<h2>Comment se met-il en place ?</h2>
<p>De deux façons : soit le salarié demande à être dispensé de la mutuelle de l'entreprise et réclame le versement santé, ce qui est un droit pour lui ; soit un accord de branche ou d'entreprise, ou à défaut une décision de l'employeur, prévoit que ces salariés sont couverts par ce moyen plutôt que par le contrat collectif.</p>
<h2>Comment le calculer en 2026 ?</h2>
<p>Le versement est égal à un montant de référence multiplié par un coefficient.</p>
<div class="table-wrap"><table>
<thead><tr><th>Élément</th><th>Valeur 2026</th></tr></thead>
<tbody>
<tr><td>Montant de référence</td><td>La contribution que l'employeur aurait payée pour ce salarié ; à défaut de pouvoir la déterminer, un forfait de 22,27 € par mois (7,44 € en Alsace-Moselle)</td></tr>
<tr><td>Proratisation</td><td>Selon les heures travaillées dans le mois, rapportées à 151,67 heures</td></tr>
<tr><td>Coefficient pour un contrat à durée indéterminée</td><td>105 %</td></tr>
<tr><td>Coefficient pour un contrat à durée déterminée ou de mission</td><td>125 %</td></tr>
</tbody></table></div>
<h2>Un exemple</h2>
<p>Un salarié en contrat à durée déterminée d'un mois travaille 60 heures. Avec le forfait de référence : 22,27 € × 60 ÷ 151,67 = 8,81 €, puis 8,81 € × 125 % = <strong>11,01 €</strong> de versement santé pour le mois.</p>
<h2>Quel est son régime social ?</h2>
<p>Le versement santé suit le même régime que la part employeur d'une mutuelle collective : exonéré de cotisations de Sécurité sociale dans les mêmes limites, soumis à la CSG et à la CRDS, et au forfait social dans les entreprises de 11 salariés et plus.</p>
<h2>Les erreurs à éviter</h2>
<ul>
<li>verser l'aide sans avoir le justificatif de la mutuelle personnelle du salarié ;</li>
<li>oublier la proratisation selon les heures ;</li>
<li>appliquer le versement santé à un salarié qui ne remplit pas les conditions de durée.</li>
</ul>
<p>Les règles propres à votre branche figurent dans <a href="{ob}">notre page sur vos obligations</a>.</p>
""",
        "faq": [
            ("Le versement santé est-il obligatoire ?", "Oui, dès qu'un salarié qui remplit les conditions le demande et justifie d'une mutuelle responsable personnelle. L'employeur ne peut pas le refuser."),
            ("Quel est le montant de référence du versement santé en 2026 ?", "À défaut de pouvoir déterminer la contribution de l'employeur, le forfait est de 22,27 € par mois, ou 7,44 € en Alsace-Moselle, à proratiser selon les heures travaillées."),
            ("Un apprenti peut-il recevoir le versement santé ?", "Oui, s'il est en contrat de 3 mois au plus ou travaille 15 heures par semaine au plus, et s'il justifie d'une mutuelle responsable personnelle."),
        ],
    },
    {
        "slug": "protection-sociale-dirigeant",
        "cat": "Dirigeant",
        "title": "Mutuelle et prévoyance du dirigeant : gérant majoritaire ou président de SAS",
        "desc": "Le dirigeant est-il couvert par le contrat de ses salariés ? Statut de travailleur non salarié ou d'assimilé salarié, contrats « Madelin », arrêt de travail : les règles.",
        "body": """
<p class="lead-p">Beaucoup de dirigeants {pub} découvrent le jour d'un arrêt de travail qu'ils n'étaient pas couverts comme leurs salariés. Tout dépend du statut social.</p>
<h2>Le dirigeant est-il couvert par le contrat de ses salariés ?</h2>
<p>Cela dépend de son statut. Un dirigeant affilié au régime général, dit assimilé salarié, peut rejoindre le contrat collectif sous conditions. Un travailleur non salarié ne le peut pas : il doit souscrire ses propres contrats.</p>
<div class="table-wrap"><table>
<thead><tr><th>Dirigeant</th><th>Statut social</th><th>Mutuelle et prévoyance</th></tr></thead>
<tbody>
<tr><td>Gérant majoritaire de SARL, gérant d'EURL associé unique, entrepreneur individuel</td><td>Travailleur non salarié</td><td>Contrats personnels, déductibles sous conditions</td></tr>
<tr><td>Président de SAS ou de SASU, gérant minoritaire ou égalitaire de SARL rémunéré</td><td>Assimilé salarié</td><td>Peut être couvert par le contrat collectif de l'entreprise, sous conditions</td></tr>
</tbody></table></div>
<h2>Le travailleur non salarié</h2>
<p>Sa protection de base est plus faible que celle d'un salarié, surtout en cas d'arrêt de travail et d'invalidité. Il complète par des contrats individuels de mutuelle et de prévoyance, souvent appelés contrats « Madelin ». Leurs cotisations sont déductibles du revenu professionnel, dans des limites qui dépendent de ce revenu.</p>
<h2>L'assimilé salarié</h2>
<p>Le président de SAS rémunéré cotise au régime général, mais pas à l'assurance chômage. Il peut bénéficier du contrat collectif de l'entreprise si l'acte de mise en place le prévoit et si la décision est régulièrement prise par l'organe compétent de la société. Il relève alors, en général, de la catégorie des cadres, avec la prévoyance correspondante.</p>
<div class="callout"><strong>Point de vigilance</strong>Un président de SAS qui ne se verse pas de rémunération n'acquiert pas de droits aux indemnités journalières. La mutuelle collective peut lui rester ouverte, mais la prévoyance calculée sur le salaire ne lui verserait rien.</div>
<h2>Que se passe-t-il en cas d'arrêt de travail ?</h2>
<p>Le dirigeant ne bénéficie pas du maintien de salaire que la loi impose pour les salariés, sauf s'il cumule son mandat avec un vrai contrat de travail. Sans prévoyance, son revenu peut chuter dès les premiers jours, alors que les charges de l'entreprise continuent.</p>
<h2>Les trois garanties à regarder</h2>
<ul>
<li><strong>les indemnités journalières</strong> en cas d'arrêt, avec une franchise adaptée à votre trésorerie ;</li>
<li><strong>la rente d'invalidité</strong>, en vérifiant comment le contrat définit l'invalidité : par rapport à votre métier, ou à tout métier ;</li>
<li><strong>le capital décès</strong>, et la garantie des frais généraux, qui paie les charges fixes de l'entreprise pendant votre arrêt.</li>
</ul>
<h2>Et le conjoint qui travaille dans l'entreprise ?</h2>
<p>Le conjoint doit avoir un statut : collaborateur, salarié ou associé. Sa protection sociale en dépend entièrement. Un conjoint salarié est couvert comme les autres salariés ; un conjoint collaborateur relève du régime des indépendants et a besoin de ses propres contrats.</p>
""",
        "faq": [
            ("Un gérant majoritaire de SARL peut-il adhérer à la mutuelle de ses salariés ?", "Non. Travailleur non salarié, il n'entre pas dans le contrat collectif des salariés et doit souscrire une mutuelle et une prévoyance individuelles, déductibles sous conditions."),
            ("Un président de SAS est-il couvert par la prévoyance de l'entreprise ?", "Il peut l'être s'il est rémunéré, si l'acte de mise en place l'inclut et si la société l'a décidé régulièrement. Sans rémunération, une prévoyance calculée sur le salaire ne lui verse rien."),
            ("Qu'est-ce qu'un contrat Madelin ?", "Un contrat de mutuelle, de prévoyance ou de retraite souscrit par un travailleur non salarié, dont les cotisations sont déductibles de son revenu professionnel dans certaines limites."),
        ],
    },
]
