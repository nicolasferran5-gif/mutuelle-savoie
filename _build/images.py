"""Images du site Bonne Cordée : icônes (favicon, écran d'accueil) et images de partage (aperçu réseaux sociaux, 1200 x 630).

Usage : python3 _build/images.py          -> crée seulement les images manquantes (icônes, image par défaut, une par article)
        python3 _build/images.py --all    -> régénère tout

Les fichiers sont écrits dans _build/img/ et copiés tels quels par build.py. Nécessite Playwright (Chromium) et Pillow.
"""
import os, sys, html
from logo import favicon_svg, pastille_svg, mark_inner, COBALT, PAPER, INK, AMBER, AMBER_D, SKY
from articles import ARTICLES

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, "img")
OG = os.path.join(IMG, "og")
ALL = "--all" in sys.argv
IVORY = PAPER; TEAL = "#2F5D50"
COLORS = {"bg-red": COBALT, "bg-mustard": AMBER, "bg-teal": TEAL, "bg-navy": INK}
FONT_FILES = [("Manrope", 800, "normal", "manrope-latin-800-normal.woff2"),
              ("Manrope", 700, "normal", "manrope-latin-700-normal.woff2"),
              ("Manrope", 600, "normal", "manrope-latin-600-normal.woff2")]  # polices OFL embarquées dans _build/fonts


def fonts_css():
    import base64
    out = []
    for fam, w, st, f in FONT_FILES:
        b = base64.b64encode(open(os.path.join(HERE, "fonts", f), "rb").read()).decode()
        out.append(f'@font-face{{font-family:"{fam}";font-weight:{w};font-style:{st};src:url(data:font/woff2;base64,{b}) format("woff2")}}')
    return "<style>" + "".join(out) + "</style>"


def square_icon_svg():
    """Icône pleine (sans coins arrondis) pour l'écran d'accueil iPhone / Android."""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" fill="{IVORY}"/>'
            f'<g transform="translate(9 9) scale(.72)">{mark_inner(False)}</g></svg>')


def og_html(label, title_html, accent, size):
    return f"""<!doctype html><html><head><meta charset="utf-8">{fonts_css()}<style>
*{{margin:0;box-sizing:border-box}}
body{{width:1200px;height:630px;background:{PAPER};color:{INK};font-family:"Manrope",sans-serif;position:relative;overflow:hidden;
background-image:radial-gradient(rgba(180,83,42,.13) 1.8px,transparent 1.9px);background-size:26px 26px}}
.big{{position:absolute;right:56px;top:66px;width:290px;height:272px}}
.band{{position:absolute;left:0;top:0;bottom:0;width:18px;background:{accent}}}
.in{{position:absolute;left:88px;right:96px;top:70px;bottom:60px;display:flex;flex-direction:column}}
.label{{align-self:flex-start;font:700 20px/1 "Manrope",sans-serif;letter-spacing:.12em;text-transform:uppercase;color:{SKY};background:{INK};border-radius:8px;padding:13px 18px}}
h1{{margin-top:34px;font:800 {size}px/1.06 "Manrope",sans-serif;color:{INK};max-width:740px;letter-spacing:-.02em}}
h1 em{{font-style:normal;font-weight:800;color:{COBALT}}}
.foot{{margin-top:auto;display:flex;align-items:center;gap:22px}}
.foot svg{{width:112px;height:112px}}
.name{{font:800 46px/1 "Manrope",sans-serif;letter-spacing:-.01em}}
.sub{{font:700 17px/1 "Manrope",sans-serif;letter-spacing:.06em;color:{AMBER_D};margin-top:12px}}
.url{{margin-left:auto;font:600 25px/1 "Manrope",sans-serif;color:{INK}}}
</style></head><body><svg class="big" viewBox="0 0 64 60">{mark_inner(False)}</svg><div class="band"></div><div class="in">
<div class="label">{html.escape(label)}</div><h1>{title_html}</h1>
<div class="foot">{pastille_svg(True, "p")}<div><div class="name">Bonne Cordée</div><div class="sub">Le courtier des entreprises de montagne</div></div><div class="url">mutuelle-savoie.fr</div></div>
</div></body></html>"""


def title_size(t):
    n = len(t)
    return 72 if n <= 40 else 64 if n <= 70 else 56 if n <= 95 else 50


def main():
    from playwright.sync_api import sync_playwright
    from PIL import Image
    os.makedirs(OG, exist_ok=True)
    todo = lambda p: ALL or not os.path.exists(p)
    with sync_playwright() as pw:
        br = pw.chromium.launch()
        pg = br.new_page()

        def svg_png(svg, px, out):
            pg.set_viewport_size({"width": px, "height": px})
            sized = svg.replace("<svg ", '<svg width="%d" height="%d" ' % (px, px), 1)
            pg.set_content('<html><body style="margin:0;background:transparent">' + sized + '</body></html>')
            pg.screenshot(path=out, omit_background=True, clip={"x": 0, "y": 0, "width": px, "height": px})

        if todo(os.path.join(IMG, "favicon.ico")):
            for px in (16, 32, 48, 96, 192, 512):
                svg_png(favicon_svg(), px, os.path.join(IMG, f"_fav{px}.png"))
            os.replace(os.path.join(IMG, "_fav96.png"), os.path.join(IMG, "favicon-96x96.png"))
            os.replace(os.path.join(IMG, "_fav192.png"), os.path.join(IMG, "icon-192.png"))
            os.replace(os.path.join(IMG, "_fav512.png"), os.path.join(IMG, "icon-512.png"))
            big = Image.open(os.path.join(IMG, "_fav48.png"))
            big.save(os.path.join(IMG, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48)])
            for px in (16, 32, 48):
                os.remove(os.path.join(IMG, f"_fav{px}.png"))
            svg_png(square_icon_svg(), 180, os.path.join(IMG, "apple-touch-icon.png"))
            print("icônes OK")

        def og(label, title_html, plain, accent, out):
            pg.set_viewport_size({"width": 1200, "height": 630})
            pg.set_content(og_html(label, title_html, accent, title_size(plain)), wait_until="networkidle")
            pg.evaluate("document.fonts.ready")
            pg.screenshot(path=out, clip={"x": 0, "y": 0, "width": 1200, "height": 630})
            print("image de partage OK", os.path.basename(out))

        p = os.path.join(IMG, "og-default.png")
        if todo(p):
            og("Savoie · Haute-Savoie · stations", "Une saison courte.<br>Une couverture<br><em style=\"white-space:nowrap\">solide.</em>",
               "Une saison courte. Une couverture solide.", COBALT, p)
        for a in ARTICLES:
            p = os.path.join(OG, a["slug"] + ".png")
            if todo(p):
                og("Le blog · " + a["cat"], html.escape(a["title"]), a["title"], COLORS.get(a["color"], COBALT), p)
        br.close()


if __name__ == "__main__":
    main()
