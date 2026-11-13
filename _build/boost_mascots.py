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
