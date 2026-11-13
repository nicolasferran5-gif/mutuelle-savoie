# -*- coding: utf-8 -*-
"""Logos dessinés : un objet du métier par site, à plat et en couleurs (pas de personnage).
Couleurs : {D} foncé du site, {A} couleur de marque, {Y} accent clair, {S} couleur secondaire, {W} blanc, {C} crème."""
STAR = lambda x, y, s=1, c="{Y}": f'<path transform="translate({x} {y}) scale({s})" d="M0-5 1.5-1.5 5 0 1.5 1.5 0 5-1.5 1.5-5 0-1.5-1.5Z" fill="{c}"/>'
M = {
 "cloche": ('<path d="M24 12c-3-3 3-5 0-8M32 13c-3-3 3-5 0-9M40 12c-3-3 3-5 0-8" fill="none" stroke="{S}" stroke-width="2.6" stroke-linecap="round"/>'
   '<ellipse cx="32" cy="51" rx="27" ry="5" fill="{D}"/><path d="M8 49a24 24 0 0 1 48 0Z" fill="{A}"/>'
   '<path d="M14 44a18 18 0 0 1 10-15" fill="none" stroke="{W}" stroke-width="3.4" stroke-linecap="round" opacity=".85"/>'
   '<path d="M8 49h48" stroke="{Y}" stroke-width="3.4" stroke-linecap="round"/><circle cx="32" cy="22" r="4.4" fill="{Y}"/>' + STAR(53,23) + STAR(9,27,.7,"{S}")),
 "ciseaux": ('<path d="M27 37 43 6c3 5 3 11 0 16L33 40Z" fill="{D}"/><path d="M37 37 21 6c-3 5-3 11 0 16l10 18Z" fill="{S}"/>'
   '<circle cx="20" cy="49" r="8.5" fill="none" stroke="{A}" stroke-width="5.4"/><circle cx="44" cy="49" r="8.5" fill="none" stroke="{A}" stroke-width="5.4"/>'
   '<circle cx="32" cy="34" r="3" fill="{Y}"/>' + STAR(54,14) + STAR(9,24,.7)),
 "pain": ('<path d="M24 14c-3-3 3-5 0-8M32 14c-3-3 3-5 0-8M40 14c-3-3 3-5 0-8" fill="none" stroke="{S}" stroke-width="2.6" stroke-linecap="round"/>'
   '<path d="M6 44c0-14 11-25 26-25s26 11 26 25v6a4 4 0 0 1-4 4H10a4 4 0 0 1-4-4Z" fill="{A}"/>'
   '<path d="M6 46h52v4a4 4 0 0 1-4 4H10a4 4 0 0 1-4-4Z" fill="{D}" opacity=".28"/>'
   '<path d="M20 27l5 12M32 24v14M44 27l-5 12" fill="none" stroke="{Y}" stroke-width="4" stroke-linecap="round"/>' + STAR(55,17)),
 "ecran": ('<rect x="8" y="9" width="48" height="34" rx="6" fill="{D}"/><rect x="12.500" y="13.500" width="39" height="25" rx="3" fill="{W}"/>'
   '<path d="M25 20l-6 6 6 6M39 20l6 6-6 6" fill="none" stroke="{A}" stroke-width="3.400" stroke-linecap="round" stroke-linejoin="round"/><path d="M34.500 18.500l-5 15" stroke="{Y}" stroke-width="3.400" stroke-linecap="round"/>'
   '<path d="M3 48h58v2a6 6 0 0 1-6 6H9a6 6 0 0 1-6-6Z" fill="{A}"/><rect x="26" y="48" width="12" height="3" rx="1.500" fill="{W}" opacity=".7"/>' + STAR(57,7,.7)),
 "croix": ('<path d="M23 6h18a3 3 0 0 1 3 3v11h11a3 3 0 0 1 3 3v18a3 3 0 0 1-3 3H44v11a3 3 0 0 1-3 3H23a3 3 0 0 1-3-3V44H9a3 3 0 0 1-3-3V23a3 3 0 0 1 3-3h11V9a3 3 0 0 1 3-3Z" fill="{A}"/>'
   '<g transform="rotate(-40 32 32)"><rect x="17" y="25" width="30" height="14" rx="7" fill="{W}"/><path d="M32 25h8a7 7 0 0 1 0 14h-8Z" fill="{Y}"/><path d="M22 29h6" stroke="{A}" stroke-width="2" stroke-linecap="round" opacity=".5"/></g>' + STAR(55,9) + STAR(8,56,.7,"{S}")),
 "dent": ('<circle cx="32" cy="33" r="27" fill="{A}"/>'
   '<path d="M23 15c-6 0-10 4.500-10 10.500 0 5.500 2.800 8.800 3.900 14.300 1 5 1.700 11.200 5 11.200 3.500 0 3.300-8.400 5.500-12.300 1.100-2 2.600-2.700 4.600-2.700s3.500.7 4.600 2.700c2.200 3.900 2 12.300 5.500 12.300 3.300 0 4-6.200 5-11.200 1.100-5.500 3.900-8.800 3.900-14.300C51 19.500 47 15 41 15c-3.900 0-6 2-9 2s-5.100-2-9-2Z" fill="{W}"/>'
   '<path d="M19 26c0-3 1.600-5.200 4.400-6" fill="none" stroke="{A}" stroke-width="2.400" stroke-linecap="round" opacity=".45"/>' + STAR(52,12,1.1) + STAR(11,50,.7,"{W}")),
 "golf": ('<circle cx="50" cy="13" r="6" fill="{Y}"/><path d="M2 50c8-9 20-13 30-13s22 4 30 13v4a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4Z" fill="{A}"/>'
   '<path d="M2 52c8-6 20-9 30-9s22 3 30 9v2a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4Z" fill="{D}" opacity=".22"/>'
   '<path d="M27 8v36" stroke="{D}" stroke-width="3" stroke-linecap="round"/><path d="M27 8l17 6.500L27 21Z" fill="{S}" stroke="{S}" stroke-width="1.600" stroke-linejoin="round"/>'
   '<ellipse cx="27" cy="45" rx="6" ry="2" fill="{D}"/><circle cx="43" cy="42" r="4.600" fill="{W}"/>'),
 "maison": ('<rect x="42" y="12" width="7" height="13" rx="1.500" fill="{D}"/><path d="M12 30h40v22a4 4 0 0 1-4 4H16a4 4 0 0 1-4-4Z" fill="{C}"/><path d="M12 30h40v6H12Z" fill="{D}" opacity=".12"/>'
   '<path d="M5 33 32 9l27 24" fill="none" stroke="{A}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>'
   '<path d="M26 56V43a6 6 0 0 1 12 0v13Z" fill="{D}"/><circle cx="35" cy="48" r="1.500" fill="{Y}"/><rect x="16" y="38" width="7" height="7" rx="1.500" fill="{Y}"/><rect x="41" y="38" width="7" height="7" rx="1.500" fill="{Y}"/>' + STAR(9,13,.8)),
 "beret": ('<path d="M33 15c1-4 1-7-1-10" fill="none" stroke="{D}" stroke-width="3.400" stroke-linecap="round"/>'
   '<path d="M3 34c0-12 13-20 29-20s29 8 29 20c0 6-13 10-29 10S3 40 3 34Z" fill="{A}"/>'
   '<path d="M11 31c2-6 8-10 16-11.500" fill="none" stroke="{W}" stroke-width="3.400" stroke-linecap="round" opacity=".8"/>'
   '<path d="M13 41c5 3 12 4 19 4s14-1 19-4v5c0 3-8 6-19 6s-19-3-19-6Z" fill="{D}"/>' + STAR(55,14) + STAR(8,17,.7,"{S}")),
 "burger": ('<path d="M7 28c0-11 11-18 25-18s25 7 25 18Z" fill="{Y}"/><circle cx="22" cy="19" r="1.500" fill="{W}"/><circle cx="32" cy="16" r="1.500" fill="{W}"/><circle cx="42" cy="19" r="1.500" fill="{W}"/><circle cx="27" cy="23" r="1.500" fill="{W}"/><circle cx="38" cy="23.500" r="1.500" fill="{W}"/>'
   '<path d="M5 31c4-3 6 3 10 0s6 3 10 0 6 3 10 0 6 3 10 0 6 3 10 0 4 0 4 0v4H5Z" fill="{S}"/>'
   '<rect x="6" y="35" width="52" height="8" rx="4" fill="{D}"/><path d="M8 41h48l-10 6-6-3-8 3-6-3-8 3Z" fill="{A}"/>'
   '<path d="M7 47h50v3a7 7 0 0 1-7 7H14a7 7 0 0 1-7-7Z" fill="{Y}"/>'),
}

# Dessins des cartes métiers (même style que les logos). Choisis par mot-clé dans le titre de la carte.
P = {
 "hotel": '<rect x="12" y="14" width="40" height="44" rx="4" fill="{A}"/><rect x="18" y="6" width="28" height="10" rx="3" fill="{D}"/><path d="M24 11h16" stroke="{Y}" stroke-width="3" stroke-linecap="round"/>'
          '<g fill="{Y}"><rect x="18" y="22" width="7" height="7" rx="1.5"/><rect x="28.500" y="22" width="7" height="7" rx="1.500"/><rect x="39" y="22" width="7" height="7" rx="1.500"/><rect x="18" y="33" width="7" height="7" rx="1.500"/><rect x="39" y="33" width="7" height="7" rx="1.500"/></g>'
          '<rect x="28.500" y="33" width="7" height="7" rx="1.500" fill="{W}"/><path d="M26 58V49a6 6 0 0 1 12 0v9Z" fill="{D}"/><rect x="6" y="56" width="52" height="4" rx="2" fill="{D}"/>',
 "assiette": '<circle cx="34" cy="34" r="20" fill="{W}" stroke="{D}" stroke-width="3"/><circle cx="34" cy="34" r="12" fill="{A}"/><path d="M28 34a6 6 0 0 1 6-6" fill="none" stroke="{W}" stroke-width="2.600" stroke-linecap="round" opacity=".8"/>'
             '<path d="M8 10v12a4 4 0 0 0 8 0V10M12 10v46" fill="none" stroke="{D}" stroke-width="3.400" stroke-linecap="round"/><path d="M58 56V10c-5 4-6 14-4 24h4" fill="{S}" stroke="{S}" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>',
 "tasse": '<path d="M24 12c-3-3 3-5 0-8M34 12c-3-3 3-5 0-8" fill="none" stroke="{S}" stroke-width="2.800" stroke-linecap="round"/><path d="M10 20h38v16a16 16 0 0 1-16 16h-6a16 16 0 0 1-16-16Z" fill="{A}"/>'
          '<path d="M48 25h4a7 7 0 0 1 0 14h-5" fill="none" stroke="{A}" stroke-width="4.400" stroke-linecap="round"/><path d="M10 20h38v6H10Z" fill="{D}" opacity=".3"/><rect x="6" y="54" width="46" height="5" rx="2.500" fill="{D}"/><path d="M16 30v6a10 10 0 0 0 5 8.600" fill="none" stroke="{W}" stroke-width="3" stroke-linecap="round" opacity=".7"/>',
 "livre": '<path d="M8 12c8-3 16-3 24 2v42c-8-5-16-5-24-2Z" fill="{A}"/><path d="M56 12c-8-3-16-3-24 2v42c8-5 16-5 24-2Z" fill="{S}"/><path d="M32 14v42" stroke="{D}" stroke-width="3" stroke-linecap="round"/>'
          '<path d="M14 22c4-1 8-1 12 .800M14 30c4-1 8-1 12 .800M38 22.800c4-1.800 8-1.800 12-.800M38 30.800c4-1.800 8-1.800 12-.800" fill="none" stroke="{W}" stroke-width="2.600" stroke-linecap="round" opacity=".85"/><path d="M42 6h8v16l-4-3-4 3Z" fill="{Y}"/>',
 "fleur": '<g fill="{A}"><ellipse cx="32" cy="18" rx="8" ry="13"/><ellipse cx="32" cy="18" rx="8" ry="13" transform="rotate(72 32 32)"/><ellipse cx="32" cy="18" rx="8" ry="13" transform="rotate(144 32 32)"/><ellipse cx="32" cy="18" rx="8" ry="13" transform="rotate(216 32 32)"/><ellipse cx="32" cy="18" rx="8" ry="13" transform="rotate(288 32 32)"/></g>'
          '<circle cx="32" cy="32" r="8" fill="{Y}"/><circle cx="32" cy="32" r="3.500" fill="{D}"/>',
 "barbier": '<rect x="22" y="8" width="20" height="6" rx="3" fill="{D}"/><rect x="22" y="50" width="20" height="6" rx="3" fill="{D}"/><rect x="24" y="14" width="16" height="36" fill="{W}" stroke="{D}" stroke-width="2.400"/>'
            '<path d="M24 20l16-6v6l-16 6ZM24 32l16-6v6l-16 6ZM24 44l16-6v6l-16 6Z" fill="{A}"/><path d="M24 26l16-6M24 38l16-6" stroke="{S}" stroke-width="3"/><circle cx="32" cy="5" r="3" fill="{Y}"/><rect x="18" y="56" width="28" height="4" rx="2" fill="{D}"/>',
 "diplome": '<path d="M32 10 4 24l28 14 28-14Z" fill="{D}"/><path d="M14 31v13c5 5 11 7 18 7s13-2 18-7V31l-18 9Z" fill="{A}"/><path d="M56 26v16" stroke="{Y}" stroke-width="3" stroke-linecap="round"/><circle cx="56" cy="45" r="4" fill="{Y}"/>',
 "gateau": '<circle cx="32" cy="9" r="5" fill="{A}"/><path d="M12 30c0-10 9-17 20-17s20 7 20 17c0 4-4 6-7 4-2 4-8 4-10 0-2 3-6 3-8 0-3 3-9 2-10-2-3 1-5-0-5-2Z" fill="{C}" stroke="{D}" stroke-width="2.400" stroke-linejoin="round"/>'
           '<path d="M14 34h36l-5 22a3 3 0 0 1-3 2H22a3 3 0 0 1-3-2Z" fill="{A}"/><path d="M24 36l2 20M32 36v22M40 36l-2 20" stroke="{D}" stroke-width="2.200" opacity=".35"/><circle cx="24" cy="22" r="1.800" fill="{Y}"/><circle cx="38" cy="20" r="1.800" fill="{S}"/><circle cx="32" cy="26" r="1.800" fill="{Y}"/>',
 "boutique": '<rect x="10" y="26" width="44" height="30" rx="3" fill="{C}"/><path d="M6 14h52l-3 14H9Z" fill="{A}"/><path d="M16 14l-2 14M26 14l-1 14M38 14l1 14M48 14l2 14" stroke="{W}" stroke-width="5" opacity=".9"/>'
             '<path d="M9 28a6 6 0 0 0 11.500 0 6 6 0 0 0 11.500 0 6 6 0 0 0 11.500 0 6 6 0 0 0 11.500 0Z" fill="{D}"/><rect x="16" y="38" width="14" height="11" rx="2" fill="{Y}"/><path d="M36 56V40a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v16Z" fill="{D}"/><rect x="6" y="55" width="52" height="4" rx="2" fill="{D}"/>',
 "compas": '<circle cx="32" cy="10" r="5" fill="{Y}" stroke="{D}" stroke-width="2.600"/><path d="M29 14 16 54M35 14l13 40" stroke="{D}" stroke-width="4.400" stroke-linecap="round"/><path d="M14 44c11 8 25 8 36 0" fill="none" stroke="{A}" stroke-width="4" stroke-linecap="round"/>'
           '<path d="M16 54l-2 6 5-4Z" fill="{A}" stroke="{A}" stroke-width="2" stroke-linejoin="round"/><circle cx="48" cy="56" r="3" fill="{S}"/>',
 "ampoule": '<path d="M32 4v5M10 14l4 3M54 14l-4 3M6 32h5M58 32h-5" stroke="{Y}" stroke-width="3" stroke-linecap="round"/><path d="M32 14a16 16 0 0 1 9 29v5H23v-5a16 16 0 0 1 9-29Z" fill="{Y}" stroke="{D}" stroke-width="2.600" stroke-linejoin="round"/>'
            '<path d="M27 31l5 5 5-5M32 36v12" fill="none" stroke="{D}" stroke-width="2.400" stroke-linecap="round" stroke-linejoin="round"/><rect x="23" y="48" width="18" height="6" rx="2" fill="{A}"/><rect x="26" y="54" width="12" height="5" rx="2.500" fill="{D}"/>',
 "mallette": '<path d="M24 20v-6a4 4 0 0 1 4-4h8a4 4 0 0 1 4 4v6" fill="none" stroke="{D}" stroke-width="4" stroke-linecap="round"/><rect x="6" y="20" width="52" height="34" rx="6" fill="{A}"/><path d="M6 34c9 4 17 6 26 6s17-2 26-6v-8a6 6 0 0 0-6-6H12a6 6 0 0 0-6 6Z" fill="{D}" opacity=".3"/>'
             '<rect x="27" y="34" width="10" height="10" rx="2.500" fill="{Y}" stroke="{D}" stroke-width="2.400"/>',
 "equipe": '<circle cx="15" cy="24" r="8" fill="{S}"/><path d="M2 54a13 13 0 0 1 26 0Z" fill="{S}"/><circle cx="49" cy="24" r="8" fill="{Y}"/><path d="M36 54a13 13 0 0 1 26 0Z" fill="{Y}"/>'
           '<circle cx="32" cy="20" r="10" fill="{A}" stroke="{W}" stroke-width="3"/><path d="M14 58a18 18 0 0 1 36 0Z" fill="{A}" stroke="{W}" stroke-width="3" stroke-linejoin="round"/>',
 "dirigeant": '<circle cx="32" cy="18" r="12" fill="{Y}"/><path d="M8 58c0-14 10-22 24-22s24 8 24 22Z" fill="{D}"/><path d="M24 37l8 10 8-10Z" fill="{W}"/><path d="M32 43l-3.500 4 3.500 12 3.500-12Z" fill="{A}"/>',
 "calendrier": '<rect x="8" y="12" width="48" height="46" rx="7" fill="{W}" stroke="{D}" stroke-width="3"/><path d="M8 19a7 7 0 0 1 7-7h34a7 7 0 0 1 7 7v7H8Z" fill="{A}"/><path d="M20 6v10M44 6v10" stroke="{D}" stroke-width="4" stroke-linecap="round"/>'
               '<path d="M32 33v16M24 41h16" stroke="{S}" stroke-width="5" stroke-linecap="round"/><circle cx="17" cy="35" r="2.400" fill="{Y}"/><circle cx="47" cy="49" r="2.400" fill="{Y}"/>',
 "parasol": '<circle cx="50" cy="12" r="7" fill="{Y}"/><path d="M4 30a24 24 0 0 1 48 0Z" fill="{A}"/><path d="M20 30c0-9 3-18 8-22 5 4 8 13 8 22Z" fill="{W}" opacity=".9"/><path d="M28 30v24" stroke="{D}" stroke-width="3.400" stroke-linecap="round"/>'
            '<path d="M2 58c6-5 12-5 18 0s12 5 18 0 12-5 18 0" fill="none" stroke="{S}" stroke-width="3.400" stroke-linecap="round"/>',
 "document": '<path d="M14 6h26l12 12v36a4 4 0 0 1-4 4H14a4 4 0 0 1-4-4V10a4 4 0 0 1 4-4Z" fill="{W}" stroke="{D}" stroke-width="3" stroke-linejoin="round"/><path d="M40 6v12h12Z" fill="{A}" stroke="{D}" stroke-width="3" stroke-linejoin="round"/>'
             '<path d="M18 26h20M18 34h14" stroke="{S}" stroke-width="3.400" stroke-linecap="round"/><circle cx="42" cy="46" r="11" fill="{A}" stroke="{W}" stroke-width="3"/><path d="M37 46l4 4 6.500-7" fill="none" stroke="{W}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>',
}
KEYS = [("hôtel", "hotel"), ("café", "tasse"), ("bar", "barbier"), ("guide", "livre"), ("obligation", "document"), ("esthétique", "fleur"), ("apprenti", "diplome"), ("enseignant", "diplome"),
        ("pâtisserie", "gateau"), ("vente", "boutique"), ("artisan", "boutique"), ("commerce", "boutique"), ("bureau", "compas"), ("conseil", "ampoule"), ("cadre", "mallette"),
        ("équip", "equipe"), ("négociateur", "equipe"), ("arrêt", "calendrier"), ("tourisme", "parasol"), ("titulaire", "dirigeant"), ("praticien", "dirigeant"), ("dirigeant", "dirigeant"),
        ("franchis", "dirigeant"), ("indépendant", "dirigeant"), ("restaurants", "assiette")]


def pick(label):
    """Clé du dessin pour un titre de carte ; None : on prend le dessin du logo du site."""
    low = label.lower()
    if low.startswith("cafés") or "café" in low: return "tasse"
    for k, v in KEYS:
        if k in low: return v
    return None

# Logos : pictogramme plein, deux tons, dans une tuile à la couleur du site (entre l'icône au trait et le dessin détaillé).
G = {
 "cloche": '<path d="M13 42a19 19 0 0 1 38 0Z" fill="{W}"/><rect x="9" y="44.500" width="46" height="5.500" rx="2.750" fill="{W}"/><circle cx="32" cy="19" r="4.200" fill="{Y}"/><path d="M20 38a12 12 0 0 1 7-9" fill="none" stroke="{A}" stroke-width="3" stroke-linecap="round" opacity=".55"/>',
 "ciseaux": '<path d="M28 38 42 11c3 5 3 10 0 15l-9 13Z" fill="{W}"/><path d="M36 38 22 11c-3 5-3 10 0 15l9 13Z" fill="{W}" opacity=".8"/><circle cx="22" cy="46" r="6.500" fill="none" stroke="{W}" stroke-width="5"/><circle cx="42" cy="46" r="6.500" fill="none" stroke="{W}" stroke-width="5"/><circle cx="32" cy="34" r="2.800" fill="{Y}"/>',
 "pain": '<path d="M9 44c0-13 10-22 23-22s23 9 23 22v3a4 4 0 0 1-4 4H13a4 4 0 0 1-4-4Z" fill="{W}"/><path d="M22 30l4 10M32 28v11M42 30l-4 10" fill="none" stroke="{Y}" stroke-width="4" stroke-linecap="round"/>',
 "ecran": '<rect x="10" y="13" width="44" height="30" rx="6" fill="{W}"/><path d="M26 22l-6 6 6 6M38 22l6 6-6 6" fill="none" stroke="{A}" stroke-width="3.600" stroke-linecap="round" stroke-linejoin="round"/><path d="M34 20l-4 16" stroke="{Y}" stroke-width="3.600" stroke-linecap="round"/><rect x="6" y="46" width="52" height="6" rx="3" fill="{W}"/>',
 "croix": '<path d="M25 9h14a2 2 0 0 1 2 2v12h12a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H41v12a2 2 0 0 1-2 2H25a2 2 0 0 1-2-2V41H11a2 2 0 0 1-2-2V25a2 2 0 0 1 2-2h12V11a2 2 0 0 1 2-2Z" fill="{W}"/><g transform="rotate(-40 32 32)"><rect x="20" y="26.500" width="24" height="11" rx="5.500" fill="{A}"/><path d="M32 26.500h6.500a5.500 5.500 0 0 1 0 11H32Z" fill="{Y}"/></g>',
 "dent": '<path d="M23 12c-6 0-10 4.500-10 10.500 0 5.500 2.800 8.800 3.900 14.300 1 5 1.700 12.200 5 12.200 3.500 0 3.300-9.400 5.500-13.300 1.100-2 2.600-2.700 4.600-2.700s3.500.7 4.600 2.700c2.200 3.900 2 13.300 5.500 13.300 3.300 0 4-7.200 5-12.200 1.100-5.500 3.900-8.800 3.900-14.300C51 16.500 47 12 41 12c-3.900 0-6 2-9 2s-5.100-2-9-2Z" fill="{W}"/><path d="M47 6l1.600 4 4 1.600-4 1.600-1.600 4-1.600-4-4-1.600 4-1.600Z" fill="{Y}"/>',
 "golf": '<path d="M6 50c8-8 17-11 26-11s18 3 26 11v2a3 3 0 0 1-3 3H9a3 3 0 0 1-3-3Z" fill="{W}"/><path d="M27 10v34" stroke="{W}" stroke-width="3.600" stroke-linecap="round"/><path d="M27 10l18 7-18 7Z" fill="{Y}" stroke="{Y}" stroke-width="1.600" stroke-linejoin="round"/><circle cx="42" cy="44" r="3.600" fill="{A}"/>',
 "maison": '<path d="M32 9 7 31h7v20a3 3 0 0 0 3 3h30a3 3 0 0 0 3-3V31h7Z" fill="{W}"/><path d="M27 54V42a5 5 0 0 1 10 0v12Z" fill="{A}"/><rect x="28" y="24" width="8" height="8" rx="2" fill="{Y}"/>',
 "beret": '<path d="M33 17c1-4 1-6-1-9" fill="none" stroke="{W}" stroke-width="3.600" stroke-linecap="round"/><path d="M5 35c0-11 12-19 27-19s27 8 27 19c0 6-12 9-27 9S5 41 5 35Z" fill="{W}"/><path d="M14 43c5 2.500 11 3.500 18 3.500s13-1 18-3.500v4c0 3-8 5.500-18 5.500s-18-2.500-18-5.500Z" fill="{Y}"/>',
 "burger": '<path d="M9 28c0-10 10-16 23-16s23 6 23 16Z" fill="{W}"/><rect x="7" y="31.500" width="50" height="7" rx="3.500" fill="{Y}"/><path d="M9 42h46v3a7 7 0 0 1-7 7H16a7 7 0 0 1-7-7Z" fill="{W}"/>',
}
