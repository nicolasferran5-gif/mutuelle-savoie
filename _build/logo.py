"""Logo Bonne Cordée : deux skis croisés vus de profil (spatules recourbées), l'un rouge Savoie, l'autre blanc neige, et un petit drapeau de la Savoie (croix blanche sur fond rouge).
Les noms de constantes reprennent ceux du moteur commun (COBALT = couleur principale, AMBER = accent, etc.)."""
COBALT = "#C8102E"   # rouge Savoie
PAPER = "#F7F9FB"
INK = "#1B2A41"
AMBER = "#2F5D50"    # vert sapin
AMBER_D = "#22463C"
SKY = "#DCE8F2"
SUN = "#F2D27A"


def _ski(angle, fill, line, flip=False):
    # un ski vu de profil : planche fine, spatule recourbée en crochet, talon arrondi, fixation
    sx = -1 if flip else 1
    return (f'<g transform="rotate({angle} 32 33) translate(32 0) scale({sx} 1) translate(-29.8 0)">'
            f'<path d="M30 58V17C30 9 26 4.5 20.5 4.8c-1.6.1-1.9 2-.4 2.4C24 8.4 25.6 12 25.6 17V58c0 1.6 4.4 1.6 4.4 0Z" '
            f'fill="{fill}" stroke="{line}" stroke-width="1.5" stroke-linejoin="round"/>'
            f'<rect x="30" y="41" width="4.2" height="8" rx="1.2" fill="{line}"/>'
            f'<path d="M30 45h4.2" stroke="{fill}" stroke-width="1.2"/></g>')


def mark_inner(dark=False):
    line = PAPER if dark else INK
    return (
        _ski(-24, COBALT, line) + _ski(24, SKY if not dark else PAPER, line, flip=True) +
        f'<rect x="45" y="1.5" width="12" height="12" rx="2.5" fill="{COBALT}" stroke="{line}" stroke-width="1.3"/>'
        f'<path d="M51 3.5v8M47 7.5h8" stroke="{PAPER}" stroke-width="2.2"/>'
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
            f'<g transform="translate(0 2)">{mark_inner(False)}</g></svg>')
