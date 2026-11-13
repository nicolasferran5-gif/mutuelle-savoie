# Mascottes : {D} foncé du site, {A} couleur de marque, {Y} accent clair, {W} blanc
EYE = lambda x, y, r=3.4: f'<circle cx="{x}" cy="{y}" r="{r}" fill="{{W}}"/><circle cx="{x+.6}" cy="{y+.4}" r="{r/2}" fill="{{D}}"/>'
DOT = lambda x, y, r=2.2: f'<circle cx="{x}" cy="{y}" r="{r}" fill="{{D}}"/><circle cx="{x+.7}" cy="{y-.7}" r="{r/3}" fill="{{W}}"/>'
M = {
 "manchot": ('<ellipse cx="25" cy="59" rx="6" ry="2.8" fill="{Y}"/><ellipse cx="39" cy="59" rx="6" ry="2.8" fill="{Y}"/>'
   '<path d="M15 32c-6 6-7 14-3 20 3-3 5-8 5-13Z" fill="{D}"/><path d="M49 32c6 6 7 14 3 20-3-3-5-8-5-13Z" fill="{D}"/>'
   '<path d="M32 4c11 0 18 9 18 26 0 16-6 28-18 28S14 46 14 30C14 13 21 4 32 4Z" fill="{D}"/>'
   '<path d="M32 21c7 0 11.5 6 11.5 16 0 10-4 17.5-11.5 17.5S20.5 47 20.5 37c0-10 4.5-16 11.5-16Z" fill="{W}"/>'
   + EYE(25.5,17,3.6) + EYE(38.5,17,3.6) +
   '<path d="M28 22.5h8l-4 5Z" fill="{Y}" stroke="{Y}" stroke-width="1.6" stroke-linejoin="round"/>'
   '<path d="M32 33l-7-4v8ZM32 33l7-4v8Z" fill="{A}" stroke="{A}" stroke-width="1.4" stroke-linejoin="round"/><circle cx="32" cy="33" r="2" fill="{A}"/>'
   '<circle cx="32" cy="41" r="1.3" fill="{D}"/><circle cx="32" cy="46.5" r="1.3" fill="{D}"/>'),
 "lion": ("".join(f'<circle cx="{32+22*__import__("math").cos(i*0.5236):.1f}" cy="{33+22*__import__("math").sin(i*0.5236):.1f}" r="8" fill="{{A}}"/>' for i in range(12)) +
   '<circle cx="32" cy="33" r="22" fill="{A}"/><circle cx="20" cy="19" r="5" fill="{Y}"/><circle cx="44" cy="19" r="5" fill="{Y}"/>'
   '<circle cx="32" cy="35" r="16" fill="{Y}"/>' + DOT(25.5,32) + DOT(38.5,32) +
   '<ellipse cx="32" cy="41" rx="7.5" ry="5.5" fill="{W}"/><path d="M29 38.5h6l-3 3.4Z" fill="{D}" stroke="{D}" stroke-width="1.2" stroke-linejoin="round"/>'
   '<path d="M32 42v2.2M28.4 45.2q1.8 1.6 3.600-.8 1.800 2.400 3.600.8" fill="none" stroke="{D}" stroke-width="1.5" stroke-linecap="round"/>'),
 "coq": ('<ellipse cx="26" cy="59" rx="5.5" ry="2.6" fill="{Y}"/><ellipse cx="38" cy="59" rx="5.5" ry="2.6" fill="{Y}"/>'
   '<circle cx="25" cy="11" r="5.5" fill="{A}"/><circle cx="32" cy="8" r="6.2" fill="{A}"/><circle cx="39" cy="11" r="5.500" fill="{A}"/>'
   '<path d="M49 36c7 2 9 9 6 15-4-1-7-4-8-8Z" fill="{D}"/>'
   '<path d="M32 10c10 0 17 9 17 24 0 14-7 24-17 24S15 48 15 34c0-15 7-24 17-24Z" fill="{D}"/>'
   '<path d="M32 30c6 0 10 5 10 13s-4 13-10 13-10-5-10-13 4-13 10-13Z" fill="{W}"/>'
   + EYE(25.5,21,3.6) + EYE(38.5,21,3.6) +
   '<path d="M28 26.500h8l-4 5.500Z" fill="{Y}" stroke="{Y}" stroke-width="1.600" stroke-linejoin="round"/>'
   '<path d="M32 33c2.600 0 3.600 2.400 3 4.800-.5 2-1.600 3.200-3 3.200s-2.500-1.200-3-3.200c-.6-2.400.4-4.800 3-4.800Z" fill="{A}"/>'),
 "chouette": ('<ellipse cx="26" cy="59" rx="5" ry="2.4" fill="{Y}"/><ellipse cx="38" cy="59" rx="5" ry="2.400" fill="{Y}"/>'
   '<path d="M14 8l10 6H14ZM50 8 40 14h10Z" fill="{D}" stroke="{D}" stroke-width="3" stroke-linejoin="round"/>'
   '<path d="M32 8c12 0 19 9 19 25 0 15-7 25-19 25S13 48 13 33C13 17 20 8 32 8Z" fill="{D}"/>'
   '<path d="M32 34c6.500 0 10.500 4.500 10.500 11S38.500 56 32 56s-10.500-4.500-10.500-11S25.500 34 32 34Z" fill="{W}"/>'
   '<circle cx="23.500" cy="24" r="8.200" fill="{W}"/><circle cx="40.500" cy="24" r="8.200" fill="{W}"/>'
   '<circle cx="23.500" cy="24" r="8.200" fill="none" stroke="{Y}" stroke-width="2.400"/><circle cx="40.500" cy="24" r="8.200" fill="none" stroke="{Y}" stroke-width="2.400"/>'
   '<circle cx="24.500" cy="24.500" r="3.400" fill="{D}"/><circle cx="39.500" cy="24.500" r="3.400" fill="{D}"/><circle cx="25.600" cy="23.400" r="1.100" fill="{W}"/><circle cx="40.600" cy="23.400" r="1.100" fill="{W}"/>'
   '<path d="M29.500 30h5l-2.500 4.500Z" fill="{Y}" stroke="{Y}" stroke-width="1.400" stroke-linejoin="round"/>'
   '<path d="M28.500 42l-3 3 3 3M35.500 42l3 3-3 3" fill="none" stroke="{A}" stroke-width="2.200" stroke-linecap="round" stroke-linejoin="round"/>'),
 "ours": ('<circle cx="15" cy="17" r="8.500" fill="{D}"/><circle cx="49" cy="17" r="8.500" fill="{D}"/><circle cx="15" cy="17" r="4" fill="{A}"/><circle cx="49" cy="17" r="4" fill="{A}"/>'
   '<circle cx="32" cy="34" r="23" fill="{D}"/>' + EYE(23.5,29,3.6) + EYE(40.5,29,3.6) +
   '<ellipse cx="32" cy="42" rx="10.500" ry="8" fill="{W}"/><ellipse cx="32" cy="38.500" rx="3.600" ry="2.600" fill="{D}"/>'
   '<path d="M32 41v2.600M28 45.500q4 3 8 0" fill="none" stroke="{D}" stroke-width="1.700" stroke-linecap="round"/>'
   '<circle cx="50" cy="50" r="9" fill="{A}" stroke="{W}" stroke-width="2.400"/><path d="M50 45v10M45 50h10" stroke="{W}" stroke-width="3" stroke-linecap="round"/>'),
 "castor": ('<circle cx="16" cy="16" r="6.500" fill="{D}"/><circle cx="48" cy="16" r="6.500" fill="{D}"/><circle cx="16" cy="16" r="3" fill="{Y}"/><circle cx="48" cy="16" r="3" fill="{Y}"/>'
   '<path d="M32 9c13 0 22 9 22 22 0 12-9 21-22 21S10 43 10 31C10 18 19 9 32 9Z" fill="{D}"/>' + EYE(23.5,26,3.6) + EYE(40.5,26,3.6) +
   '<ellipse cx="32" cy="38" rx="12" ry="8.500" fill="{Y}"/><ellipse cx="32" cy="33.500" rx="4" ry="2.800" fill="{D}"/>'
   '<path d="M26.500 43.500h5.200v10.500a1.600 1.600 0 0 1-1.600 1.600h-2a1.600 1.600 0 0 1-1.600-1.600ZM32.300 43.500h5.200V54a1.600 1.600 0 0 1-1.600 1.600h-2a1.600 1.600 0 0 1-1.600-1.600Z" fill="{W}" stroke="{D}" stroke-width="1.600" stroke-linejoin="round"/>'
   '<path d="M48 47l1.300 3 3 1.300-3 1.300-1.300 3-1.300-3-3-1.300 3-1.300Z" fill="{A}"/>'),
 "oiseau": ('<path d="M52 8v34" stroke="{D}" stroke-width="2.600" stroke-linecap="round"/><path d="M52 9l-13 5 13 5Z" fill="{Y}" stroke="{Y}" stroke-width="1.600" stroke-linejoin="round"/>'
   '<path d="M24 56v5M32 56v5" stroke="{Y}" stroke-width="2.600" stroke-linecap="round"/>'
   '<path d="M8 40l-6-4 2 8Z" fill="{D}" stroke="{D}" stroke-width="2" stroke-linejoin="round"/>'
   '<circle cx="27" cy="38" r="20" fill="{A}"/><ellipse cx="29" cy="45" rx="11" ry="10" fill="{W}"/>'
   '<path d="M13 38c4-4 11-3 13 3-5 3-11 2-13-3Z" fill="{D}"/>' + EYE(31,30,3.8) +
   '<path d="M40 33l8 3-8 3.500Z" fill="{Y}" stroke="{Y}" stroke-width="1.600" stroke-linejoin="round"/>'),
 "escargot": ('<path d="M13 28l-3-11M19 27l2-11" stroke="{D}" stroke-width="2.600" stroke-linecap="round"/><circle cx="10" cy="15" r="3" fill="{D}"/><circle cx="21" cy="14" r="3" fill="{D}"/>'
   '<path d="M8 40c0-8 4-13 9-13s8 4 8 10v8h34c2 0 3 2 2 4-2 4-6 6-12 6H16c-5 0-8-6-8-15Z" fill="{D}"/>'
   '<circle cx="40" cy="31" r="19" fill="{A}"/><path d="M40 31m0-12a12 12 0 1 1-12 12 8 8 0 1 1 8 8 4.500 4.500 0 1 1 4.500-4.500" fill="none" stroke="{W}" stroke-width="3" stroke-linecap="round"/>'
   '<circle cx="15" cy="36" r="2" fill="{W}"/><path d="M12.500 42q2.500 2 5 0" fill="none" stroke="{W}" stroke-width="1.700" stroke-linecap="round"/>'
   '<path d="M36 12l4-4 4 4" fill="none" stroke="{Y}" stroke-width="2.600" stroke-linecap="round" stroke-linejoin="round"/>'),
 "brebis": ("".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{{C}}" stroke="{{D}}" stroke-width="2"/>' for x,y,r in [(15,30,9),(49,30,9),(13,44,9),(51,44,9),(22,53,9),(42,53,9),(32,56,9),(22,20,9),(42,20,9)]) +
   '<circle cx="32" cy="38" r="20" fill="{C}"/>'
   '<path d="M17 30c-5 0-8 2-9 5 4 1 8 0 10-2ZM47 30c5 0 8 2 9 5-4 1-8 0-10-2Z" fill="{D}"/>'
   '<path d="M32 22c7 0 11 6 11 14 0 9-4 16-11 16s-11-7-11-16c0-8 4-14 11-14Z" fill="{D}"/>' + EYE(27,34,3.2) + EYE(37,34,3.200) +
   '<path d="M29.500 43q2.500 2.400 5 0" fill="none" stroke="{W}" stroke-width="1.700" stroke-linecap="round"/>'
   '<path d="M16 17c0-6 7-10 16-10s16 4 16 10c0 3-7 5-16 5s-16-2-16-5Z" fill="{A}"/><path d="M32 7V3" stroke="{A}" stroke-width="2.600" stroke-linecap="round"/>'),
 "renard": ('<path d="M9 8l15 9-11 11ZM55 8 40 17l11 11Z" fill="{A}" stroke="{A}" stroke-width="3" stroke-linejoin="round"/><path d="M13 14l7 4.500-5 5ZM51 14l-7 4.500 5 5Z" fill="{D}"/>'
   '<path d="M32 12c13 0 22 8 22 20 0 6-3 11-8 16-5 5-9 9-14 9s-9-4-14-9c-5-5-8-10-8-16 0-12 9-20 22-20Z" fill="{A}"/>'
   '<path d="M10 34c6 0 12 4 16 10l6 13c-5 0-9-4-14-9-4-4-7-9-8-14ZM54 34c-6 0-12 4-16 10l-6 13c5 0 9-4 14-9 4-4 7-9 8-14Z" fill="{C}"/>'
   + DOT(23.5,30,2.6) + DOT(40.5,30,2.6) +
   '<path d="M28.500 51h7l-3.500 4.500Z" fill="{D}" stroke="{D}" stroke-width="1.800" stroke-linejoin="round"/>'),
}
