"""Logo Bonne Cordée : un sommet enneigé protégé par un arc (le contrat), avec la croix blanche sur fond rouge de la Savoie en étincelle.
Les noms de constantes reprennent ceux du moteur commun (COBALT = couleur principale, AMBER = accent, etc.)."""
COBALT = "#C8102E"   # rouge Savoie
PAPER = "#F7F9FB"
INK = "#1B2A41"
AMBER = "#2F5D50"    # vert sapin
AMBER_D = "#22463C"
SKY = "#DCE8F2"


def mark_inner(dark=False):
    line = PAPER if dark else INK
    return (
        f'<path d="M6 30C6 15 17 4 32 4s26 11 26 26" fill="none" stroke="{COBALT}" stroke-width="3.4" stroke-linecap="round"/>'
        f'<path d="M10 54L27 22l8 13 6-8 13 27Z" fill="{SKY}" stroke="{line}" stroke-width="2.6" stroke-linejoin="round"/>'
        f'<path d="M21 33l6-11 6 10-3 3-3-3-3 3Z" fill="{PAPER}" stroke="{line}" stroke-width="2.2" stroke-linejoin="round"/>'
        f'<rect x="45" y="3" width="11" height="11" rx="2" fill="{COBALT}"/>'
        f'<path d="M50.5 5.5v6M47.5 8.5h6" stroke="{PAPER}" stroke-width="2" stroke-linecap="round"/>'
    )


def mark_svg(dark=False, cls="logo-mark", standalone=False):
    ns = ' xmlns="http://www.w3.org/2000/svg"' if standalone else ""
    return f'<svg{ns} class="{cls}" viewBox="0 0 64 60" aria-hidden="true">{mark_inner(dark)}</svg>'


def pastille_svg(standalone=False, cls="pastille"):
    ns = ' xmlns="http://www.w3.org/2000/svg"' if standalone else ""
    return (f'<svg{ns} class="{cls}" viewBox="0 0 120 120" aria-hidden="true"><rect x="2" y="2" width="116" height="116" rx="34" fill="{PAPER}"/>'
            f'<rect x="8" y="8" width="104" height="104" rx="29" fill="none" stroke="{COBALT}" stroke-width="1.6"/>'
            f'<g transform="translate(24 25) scale(1.13)">{mark_inner(False)}</g></svg>')


def favicon_svg():
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="16" fill="{PAPER}"/>'
            f'<g transform="translate(3 3) scale(.9)">{mark_inner(False)}</g></svg>')
