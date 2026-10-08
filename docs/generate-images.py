#!/usr/bin/env python3
"""
Membuat semua gambar README Livia Panel (SVG, tema Roblox) dalam dua bahasa.

Pakai:
    python3 docs/generate-images.py

Hasil ada di docs/images/:
    banner.id.svg   banner.en.svg
    preview.id.svg  preview.en.svg
    features.id.svg features.en.svg
    workflow.id.svg workflow.en.svg
    controls.id.svg controls.en.svg
    fly.id.svg      fly.en.svg
    safety.id.svg   safety.en.svg
    social-preview.svg (+ social-preview.png bila cairosvg terpasang)

Warna panel diambil dari tabel `T` di LiviaPanel.lua, jadi gambar tetap
sama dengan tampilan aslinya. Ubah teks lewat kamus STR di bawah.
"""
import os
import random
from xml.sax.saxutils import escape

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
os.makedirs(OUT, exist_ok=True)

UI = "'Segoe UI','Helvetica Neue',Arial,sans-serif"
MONO = "Consolas,'SFMono-Regular',Menlo,'DejaVu Sans Mono',monospace"

# Warna panel (sama dengan tabel T di LiviaPanel.lua)
C = dict(
    bg="#101118", panel="#181a25", card="#202332", inp="#2c3044",
    stroke="#3a3f5a", accent="#7c5cff", text="#f0f2fa", off="#464b64",
    on="#2ecc85", red="#f05460",
)
# Warna blok bergaya Roblox
ORANGE, BLUE, YELLOW, GREEN = "#ff9f1c", "#1f9bff", "#f7d44c", "#4fae4a"
SLATE, SHADOW = "#5b6b8c", "#07080f"

# ----------------------------------------------------------------- teks
STR = {
    "id": {
        "tag": "ROBLOX EXECUTOR  ·  KHUSUS LAYAR HP",
        "tagline": "Satu panel mungil untuk Roblox executor.",
        "alt_banner": "Livia Panel: panel Speed, Jump, Fly, Ghost, dan ESP untuk Roblox executor",
        "cap_default": "Bawaan (semua OFF)",
        "cap_active": "Fitur menyala",
        "cap_min": "Diminimize",
        "cap_min_sub": "Ketuk bulatan L untuk membuka lagi",
        "alt_preview": "Tiga tampilan panel: bawaan, fitur menyala, dan diminimize",
        "features": [
            ("SPEED", "angka + ON/OFF", ["Atur kecepatan lari.", "Kembali ke 16 saat OFF."], "BAWAAN 50"),
            ("JUMP", "angka + ON/OFF", ["Atur tinggi lompat.", "Kembali ke 50 saat OFF."], "BAWAAN 100"),
            ("FLY", "angka + ON/OFF", ["Terbang bebas, angka", "menentukan kecepatan.", "Kamera atur naik/turun."], "BAWAAN 60"),
            ("GHOST", "ON/OFF", ["Tembus tembok (noclip)", "dengan mematikan", "collision karakter."], "TANPA ANGKA"),
            ("ESP PLAYER", "ON/OFF", ["Pemain lain tampak", "tembus pandang dengan", "sorotan merah."], "TANPA ANGKA"),
        ],
        "alt_features": "Lima fitur Livia Panel: Speed, Jump, Fly, Ghost, dan ESP Player",
        "steps": [
            ("SALIN", ["Salin isi LiviaPanel.lua", "atau pakai loadstring."]),
            ("JALANKAN", ["Tempel di executor, lalu", "jalankan di dalam game."]),
            ("NYALAKAN", ["Isi angka bila perlu,", "lalu ketuk tombol ON."]),
            ("ATUR", ["Geser panel, minimize (-),", "atau tutup dengan X."]),
        ],
        "alt_workflow": "Alur pakai Livia Panel: salin, jalankan, nyalakan, atur",
        "controls": [
            ("TAP", "Sentuh singkat", ["Tombol bereaksi saat kamu", "mengetuk tanpa bergeser."]),
            ("DRAG", "Geser", ["Geser lebih dari 10 px", "memindahkan panel. Tombol", "tidak aktif saat digeser."]),
            ("MINIMIZE", "Minimize (-)", ["Panel jadi bulatan L.", "Ketuk bulatan itu untuk", "membuka lagi."]),
            ("CLOSE", "Tutup (X)", ["Mematikan semua fitur,", "lalu menutup panel."]),
        ],
        "alt_controls": "Kontrol panel: ketuk, geser, minimize, dan tutup",
        "fly_up": ("NAIK", "Kamera ke atas + joystick maju"),
        "fly_down": ("TURUN", "Kamera ke bawah + joystick maju"),
        "fly_note": "Joystick dilepas = melayang di tempat.",
        "alt_fly": "Cara mengatur ketinggian saat Fly: arahkan kamera ke atas atau ke bawah sambil mendorong joystick",
        "safety": [
            ("Hanya sisi client", ["Script berjalan di sisi client", "kamu dan berhenti saat kamu", "keluar dari game."]),
            ("Anti-cheat", ["Sebagian game menarik balik", "speed atau jump. Pakai angka", "yang lebih kecil bila itu terjadi."]),
            ("Risiko akun", ["Bisa melanggar Terms of Use", "Roblox dan berisiko kena sanksi.", "Risiko ditanggung sendiri."]),
        ],
        "alt_safety": "Catatan keamanan: sisi client, anti-cheat, dan risiko akun",
    },
    "en": {
        "tag": "ROBLOX EXECUTOR  ·  MOBILE FIRST",
        "tagline": "One compact panel for Roblox executors.",
        "alt_banner": "Livia Panel: a Speed, Jump, Fly, Ghost, and ESP panel for Roblox executors",
        "cap_default": "Default (all OFF)",
        "cap_active": "Features on",
        "cap_min": "Minimized",
        "cap_min_sub": "Tap the L bubble to reopen",
        "alt_preview": "Three panel views: default, features on, and minimized",
        "features": [
            ("SPEED", "number + ON/OFF", ["Sets your run speed.", "Back to 16 when OFF."], "DEFAULT 50"),
            ("JUMP", "number + ON/OFF", ["Sets your jump height.", "Back to 50 when OFF."], "DEFAULT 100"),
            ("FLY", "number + ON/OFF", ["Free flight, the number", "sets the speed. Camera", "controls up and down."], "DEFAULT 60"),
            ("GHOST", "ON/OFF", ["Walk through walls", "(noclip) by turning off", "character collision."], "NO NUMBER"),
            ("ESP PLAYER", "ON/OFF", ["Other players show up", "through walls with a", "red highlight."], "NO NUMBER"),
        ],
        "alt_features": "Five Livia Panel features: Speed, Jump, Fly, Ghost, and ESP Player",
        "steps": [
            ("COPY", ["Copy the LiviaPanel.lua", "source or use loadstring."]),
            ("RUN", ["Paste it into your executor", "and run it inside a game."]),
            ("ENABLE", ["Set a number if needed,", "then tap the ON button."]),
            ("ADJUST", ["Drag the panel, minimize (-)", "or close it with X."]),
        ],
        "alt_workflow": "How to use Livia Panel: copy, run, enable, adjust",
        "controls": [
            ("TAP", "Quick tap", ["Buttons react when you tap", "without moving your finger."]),
            ("DRAG", "Drag", ["Moving more than 10 px", "drags the panel. Buttons", "stay inactive while dragging."]),
            ("MINIMIZE", "Minimize (-)", ["The panel becomes an L", "bubble. Tap the bubble to", "open it again."]),
            ("CLOSE", "Close (X)", ["Turns every feature off,", "then closes the panel."]),
        ],
        "alt_controls": "Panel controls: tap, drag, minimize, and close",
        "fly_up": ("CLIMB", "Camera up + joystick forward"),
        "fly_down": ("DESCEND", "Camera down + joystick forward"),
        "fly_note": "Joystick released = hover in place.",
        "alt_fly": "How to change altitude while flying: aim the camera up or down while pushing the joystick",
        "safety": [
            ("Client side only", ["The script runs on your client", "and stops when you leave", "the game."]),
            ("Anti-cheat", ["Some games pull speed or jump", "back. Use smaller numbers", "when that happens."]),
            ("Account risk", ["May violate the Roblox Terms", "of Use and risk a ban.", "Use at your own risk."]),
        ],
        "alt_safety": "Safety notes: client side, anti-cheat, and account risk",
    },
}


# ------------------------------------------------------------- helpers
def tx(x, y, s, size=16, fill=None, weight=700, anchor="start", font=UI, extra=""):
    fill = fill or C["text"]
    return (f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" {extra}>{escape(s)}</text>')


def rect(x, y, w, h, fill, rx=0, stroke=None, sw=1, extra=""):
    st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"{st} {extra}/>'


def block(x, y, w, h, fill, rx=10, off=6, stroke="#000", sa=0.35):
    """Kotak dengan bayangan keras (gaya blok Roblox)."""
    return (rect(x + off, y + off, w, h, SHADOW, rx, extra='opacity="0.55"')
            + rect(x, y, w, h, fill, rx, stroke, 2, extra=f'stroke-opacity="{sa}"'))


def chip(x, y, label, fill, color="#ffffff", size=14, pad=14, h=30):
    w = int(len(label) * size * 0.76 + pad * 2)
    return (block(x, y, w, h, fill, 7, 3)
            + tx(x + w / 2, y + h / 2 + size * 0.36, label, size, color, 800, "middle", extra='letter-spacing="1"')), w


DEFS = f"""
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#090c22"/><stop offset="0.55" stop-color="#1a1a5e"/>
  <stop offset="1" stop-color="#5a3fd0"/>
</linearGradient>
<pattern id="studs" width="32" height="32" patternUnits="userSpaceOnUse">
  <rect width="32" height="32" fill="#2c7a43"/>
  <rect x="8" y="8" width="16" height="16" rx="5" fill="#3a9657" stroke="#226036" stroke-width="2"/>
  <rect x="11" y="10" width="7" height="3" rx="1.5" fill="#6bc486" opacity="0.7"/>
</pattern>
"""


def scene(w, h, ground, seed=7, clouds=True):
    rnd = random.Random(seed)
    o = [rect(0, 0, w, h, "url(#sky)")]
    for _ in range(int(w / 22)):
        sx, sy = rnd.randrange(8, w - 8), rnd.randrange(8, max(20, ground - 90))
        sz = rnd.choice([3, 3, 4, 5])
        o.append(rect(sx, sy, sz, sz, "#ffffff", extra=f'opacity="{rnd.choice([0.25, 0.4, 0.6, 0.8])}"'))
    if clouds:
        for cx, cy, cw in [(w * 0.08, ground - 120, 120), (w * 0.52, ground - 96, 150), (w * 0.9, ground - 150, 110)]:
            o.append(rect(cx, cy, cw, 26, "#ffffff", 4, extra='opacity="0.10"'))
            o.append(rect(cx + 20, cy - 20, cw - 50, 24, "#ffffff", 4, extra='opacity="0.10"'))
    o.append(rect(0, ground - 6, w, 6, "#1b4d2b"))
    o.append(rect(0, ground, w, h - ground, "url(#studs)"))
    o.append(rect(0, ground, w, 5, "#000", extra='opacity="0.25"'))
    return "".join(o)


def avatar(x, y, s=1.0, rot=0, esp=False):
    """Karakter blok ala Roblox. (x, y) = titik tengah telapak kaki."""
    parts = [  # x, y, w, h, rx, warna
        (-14, -28, 14, 28, 3, GREEN), (0, -28, 14, 28, 3, GREEN),
        (-28, -56, 14, 28, 3, YELLOW), (14, -56, 14, 28, 3, YELLOW),
        (-14, -56, 28, 28, 3, BLUE),
        (-11, -80, 22, 22, 7, YELLOW),
    ]
    g = [f'<g transform="translate({x},{y}) rotate({rot}) scale({s})">']
    for px, py, pw, ph, prx, col in parts:
        if esp:
            g.append(rect(px, py, pw, ph, "#ff3232", prx, "#ffffff", 2.5, extra='fill-opacity="0.55"'))
        else:
            g.append(rect(px, py, pw, ph, col, prx, "#000", 1.5, extra='stroke-opacity="0.35"'))
    if not esp:
        g.append(rect(-6, -72, 3.4, 3.4, "#1b1b1b", 1))
        g.append(rect(3, -72, 3.4, 3.4, "#1b1b1b", 1))
        g.append('<path d="M-5 -64 Q0 -60 5 -64" fill="none" stroke="#1b1b1b" stroke-width="2" stroke-linecap="round"/>')
    g.append("</g>")
    return "".join(g)


ROWS = [("SPEED", "Speed", True), ("JUMP", "Jump", True), ("FLY", "Fly", True),
        ("GHOST", "Ghost", False), ("ESP PLAYER", "ESP", False)]


def panel(x, y, s=1.0, on=None, vals=None, uid="p", shadow=True):
    """Salinan panel asli: 300x342, header 46, baris 46 dengan jarak 8."""
    on = on or {}
    vals = vals or {"Speed": 50, "Jump": 100, "Fly": 60}
    o = [f'<g transform="translate({x},{y}) scale({s})">']
    if shadow:
        o.append(rect(8, 8, 300, 342, SHADOW, 14, extra='opacity="0.6"'))
    o.append(rect(0, 0, 300, 342, C["bg"], 14, C["stroke"], 1))
    o.append(f'<path d="M0 46 V14 A14 14 0 0 1 14 0 H286 A14 14 0 0 1 300 14 V46 Z" fill="{C["panel"]}"/>')
    o.append(rect(0, 44, 300, 2, C["accent"]))
    o.append(tx(14, 29, "LIVIA PANEL", 17, C["text"], 800, extra='letter-spacing="0.6"'))
    o.append(rect(216, 6, 34, 34, C["inp"], 8))
    o.append(tx(233, 29, "-", 18, C["text"], 800, "middle"))
    o.append(rect(256, 6, 34, 34, C["red"], 8))
    o.append(tx(273, 29, "X", 16, C["text"], 800, "middle"))
    for i, (label, key, has_val) in enumerate(ROWS):
        ry = 56 + i * 54
        o.append(rect(10, ry, 280, 46, C["card"], 10, C["stroke"], 1))
        o.append(tx(22, ry + 28, label, 14, C["text"], 800))
        if has_val:
            o.append(rect(140, ry + 7, 64, 32, C["inp"], 8))
            o.append(tx(172, ry + 28, str(vals[key]), 14, C["text"], 800, "middle"))
        is_on = bool(on.get(key))
        o.append(rect(210, ry + 7, 70, 32, C["on"] if is_on else C["off"], 8))
        o.append(tx(245, ry + 28, "ON" if is_on else "OFF", 14, C["text"], 800, "middle"))
    o.append("</g>")
    return "".join(o)


def orb(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})">'
            f'<circle cx="4" cy="5" r="26" fill="{SHADOW}" opacity="0.6"/>'
            f'<circle r="26" fill="{C["accent"]}" stroke="#000" stroke-opacity="0.3" stroke-width="2"/>'
            f'{tx(0, 9, "L", 24, C["text"], 800, "middle")}</g>')


def title3d(x, y, s, size, depth=7, main="#ffffff", side="#3b2a99"):
    o = []
    for i in range(depth, 0, -1):
        o.append(tx(x + i, y + i, s, size, side, 900, extra='letter-spacing="2"'))
    o.append(tx(x, y, s, size, main, 900, extra='letter-spacing="2"'))
    return "".join(o)


def svg(w, h, body, title, defs=DEFS):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'role="img" aria-label="{escape(title)}">\n<title>{escape(title)}</title>\n<defs>{defs}</defs>\n{body}\n</svg>\n')


def save(name, content):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(content)
    print("ok", name)


def icon(kind, x, y):
    """Ikon putih 64x64 di dalam blok berwarna."""
    g = [f'<g transform="translate({x},{y})" fill="#fff">']
    if kind == "SPEED":
        g.append('<path d="M37 6 L13 37 H28 L22 60 L51 25 H35 L43 6 Z"/>')
    elif kind == "JUMP":
        g.append('<path d="M12 34 L32 14 L52 34" fill="none" stroke="#fff" stroke-width="9" stroke-linecap="square"/>')
        g.append('<path d="M12 54 L32 34 L52 54" fill="none" stroke="#fff" stroke-width="9" stroke-linecap="square" opacity="0.55"/>')
    elif kind == "FLY":
        g.append('<path d="M6 30 L58 6 L42 58 L31 37 Z"/>')
        g.append('<path d="M31 37 L58 6" stroke="#7c5cff" stroke-width="3" fill="none"/>')
    elif kind == "GHOST":
        g.append('<path d="M10 58 V28 A22 22 0 0 1 54 28 V58 L45 49 L37 58 L27 49 L19 58 Z"/>')
        g.append('<rect x="21" y="24" width="7" height="10" rx="2" fill="#5b6b8c"/><rect x="36" y="24" width="7" height="10" rx="2" fill="#5b6b8c"/>')
    else:  # ESP
        g.append('<path d="M3 32 Q32 2 61 32 Q32 62 3 32 Z" fill="none" stroke="#fff" stroke-width="6" stroke-linejoin="round"/>')
        g.append('<circle cx="32" cy="32" r="9"/>')
    g.append("</g>")
    return "".join(g)


# --------------------------------------------------------------- gambar
def wall(x, y, w, h):
    o = [rect(x, y, w, h, "#7b7f93", 4, "#000", 2, extra='stroke-opacity="0.35"')]
    for r in range(int(h // 18)):
        o.append(rect(x, y + 18 * (r + 1) - 1, w, 2, "#000", extra='opacity="0.25"'))
        off = 0 if r % 2 == 0 else 20
        for cx in range(int(x) + off + 40, int(x + w), 40):
            o.append(rect(cx, y + 18 * r, 2, 18, "#000", extra='opacity="0.25"'))
    return "".join(o)


def banner(L):
    s = STR[L]
    W, H, G = 1280, 470, 400
    o = [scene(W, H, G, seed=3)]
    o.append(chip(60, 50, s["tag"], C["accent"], size=13)[0])
    o.append(title3d(60, 172, "LIVIA", 104))
    o.append(title3d(60, 282, "PANEL", 104))
    o.append(tx(64, 330, s["tagline"], 24, "#dfe3ff", 600))
    x = 60
    for label, col in [("SPEED", ORANGE), ("JUMP", BLUE), ("FLY", "#8b6cff"), ("GHOST", SLATE), ("ESP", C["red"])]:
        c, w = chip(x, 346, label, col, size=12, pad=11, h=26)
        o.append(c)
        x += w + 12
    for i, ly in enumerate([96, 112, 128]):
        o.append(rect(590 - i * 14, ly, 90 - i * 10, 5, "#ffffff", 2, extra='opacity="0.35"'))
    o.append(avatar(760, 150, 0.9, rot=68))
    o.append(panel(830, 30, 0.95, on={"Speed": 1, "Fly": 1, "ESP": 1}, uid="b"))
    # ESP tembus tembok
    o.append(avatar(1196, G + 2, 1.15))
    o.append(wall(1140, G - 74, 112, 74))
    o.append(avatar(1196, G + 2, 1.15, esp=True))
    o.append(orb(1196, 130, 0.9))
    o.append(tx(W - 24, H - 18, "v1.0  ·  Lua  ·  MIT", 14, "#ffffff", 700, "end", extra='opacity="0.8"'))
    save(f"banner.{L}.svg", svg(W, H, "".join(o), s["alt_banner"]))


def preview(L):
    s = STR[L]
    W, H, G = 1280, 600, 440
    o = [scene(W, H, G, seed=11)]
    sc = 1.05
    pw, ph = 300 * sc, 342 * sc
    o.append(panel(90, 60, sc, uid="a"))
    o.append(panel(90 + pw + 90, 60, sc,
                   on={"Speed": 1, "Jump": 1, "Fly": 1, "ESP": 1}, uid="b"))
    ox = 90 + 2 * (pw + 90) + 80
    o.append(orb(ox, 150, 1.3))
    o.append(avatar(ox + 40, G + 8, 1.2, esp=True))
    for cx, label in [(90 + pw / 2, s["cap_default"]), (90 + pw + 90 + pw / 2, s["cap_active"])]:
        o.append(tx(cx, G + 54, label, 20, "#ffffff", 800, "middle"))
    o.append(tx(ox, G + 54, s["cap_min"], 20, "#ffffff", 800, "middle"))
    o.append(tx(ox, G + 82, s["cap_min_sub"], 14, "#e6e8ff", 600, "middle"))
    save(f"preview.{L}.svg", svg(W, H, "".join(o), s["alt_preview"]))


def features(L):
    s = STR[L]
    W, H, G = 1280, 430, 372
    o = [scene(W, H, G, seed=5, clouds=False)]
    colors = [ORANGE, BLUE, "#8b6cff", SLATE, C["red"]]
    cw, gap = 230, 16
    x0 = (W - (5 * cw + 4 * gap)) / 2
    for i, (name, setting, lines, default) in enumerate(s["features"]):
        x, y = x0 + i * (cw + gap), 34
        o.append(block(x, y, cw, 304, C["card"], 14, 7))
        o.append(block(x + 20, y + 20, 68, 68, colors[i], 12, 4))
        o.append(icon(name.split()[0], x + 22, y + 22))
        o.append(tx(x + 20, y + 124, name, 22, C["text"], 900, extra='letter-spacing="0.5"'))
        o.append(tx(x + 20, y + 148, setting, 13, "#aab0d4", 600, font=MONO))
        for j, ln in enumerate(lines):
            o.append(tx(x + 20, y + 190 + j * 24, ln, 15, "#e3e6fb", 500))
        o.append(rect(x + 20, y + 258, cw - 40, 28, C["inp"], 7))
        o.append(tx(x + cw / 2, y + 277, default, 12, "#cfd4f5", 800, "middle", extra='letter-spacing="1.2"'))
    save(f"features.{L}.svg", svg(W, H, "".join(o), s["alt_features"]))


def workflow(L):
    s = STR[L]
    W, H, G = 1280, 300, 246
    o = [scene(W, H, G, seed=9, clouds=False)]
    colors = [ORANGE, BLUE, C["on"], "#8b6cff"]
    cw, gap = 276, 40
    x0 = (W - (4 * cw + 3 * gap)) / 2
    for i, (name, lines) in enumerate(s["steps"]):
        x, y = x0 + i * (cw + gap), 26
        o.append(block(x, y, cw, 188, C["card"], 14, 7))
        o.append(block(x + 18, y + 18, 56, 56, colors[i], 10, 4))
        o.append(tx(x + 46, y + 58, str(i + 1), 34, "#fff", 900, "middle"))
        o.append(tx(x + 90, y + 55, name, 22, C["text"], 900, extra='letter-spacing="0.5"'))
        for j, ln in enumerate(lines):
            o.append(tx(x + 20, y + 112 + j * 26, ln, 15.5, "#e3e6fb", 500))
        if i < 3:
            ax = x + cw + 6
            o.append(f'<path d="M{ax} {y+94} h{gap-20} m-10 -10 l10 10 l-10 10" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="square" opacity="0.85"/>')
    save(f"workflow.{L}.svg", svg(W, H, "".join(o), s["alt_workflow"]))


def controls(L):
    s = STR[L]
    W, H, G = 1280, 400, 342
    o = [scene(W, H, G, seed=13, clouds=False)]
    cw, gap = 296, 16
    x0 = (W - (4 * cw + 3 * gap)) / 2
    for i, (key, name, lines) in enumerate(s["controls"]):
        x, y = x0 + i * (cw + gap), 30
        o.append(block(x, y, cw, 282, C["card"], 14, 7))
        # area ilustrasi
        o.append(rect(x + 14, y + 14, cw - 28, 140, C["bg"], 10, C["stroke"], 1))
        cx, cy = x + cw / 2, y + 84
        if key == "TAP":
            for r, op in [(46, 0.18), (32, 0.32)]:
                o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{C["on"]}" stroke-width="3" opacity="{op*2}"/>')
            o.append(rect(cx - 40, cy - 17, 80, 34, C["on"], 8))
            o.append(tx(cx, cy + 6, "ON", 16, "#fff", 800, "middle"))
            o.append(f'<circle cx="{cx+34}" cy="{cy+24}" r="11" fill="#fff" opacity="0.9"/><circle cx="{cx+34}" cy="{cy+24}" r="4" fill="{C["accent"]}"/>')
        elif key == "DRAG":
            o.append(rect(cx - 98, cy - 34, 64, 56, "none", 8, "#8a90b8", 2, extra='stroke-dasharray="6 5"'))
            o.append(rect(cx + 28, cy - 18, 64, 56, C["panel"], 8, C["accent"], 2))
            o.append(rect(cx + 28, cy - 18, 64, 12, C["accent"], 6))
            o.append(f'<path d="M{cx-26} {cy-6} H{cx+16} m-9 -9 l9 9 l-9 9" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="square"/>')
            o.append(tx(cx - 5, cy - 22, "> 10 px", 12, "#fff", 800, "middle", font=MONO))
        elif key == "MINIMIZE":
            o.append(rect(cx - 100, cy - 18, 112, 36, C["panel"], 8, C["stroke"], 1))
            o.append(rect(cx - 52, cy - 12, 24, 24, C["accent"], 6))
            o.append(tx(cx - 40, cy + 6, "-", 17, "#fff", 800, "middle"))
            o.append(rect(cx - 24, cy - 12, 24, 24, C["red"], 6))
            o.append(tx(cx - 12, cy + 5, "X", 13, "#fff", 800, "middle"))
            o.append(f'<path d="M{cx+20} {cy} h24 m-9 -9 l9 9 l-9 9" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="square"/>')
            o.append(orb(cx + 78, cy, 0.9))
        else:
            o.append(rect(cx - 98, cy - 20, 40, 40, C["red"], 9))
            o.append(tx(cx - 78, cy + 8, "X", 22, "#fff", 800, "middle"))
            o.append(f'<path d="M{cx-48} {cy} h24 m-9 -9 l9 9 l-9 9" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="square"/>')
            for k, lbl in enumerate(["SPEED", "FLY", "ESP"]):
                yy = cy - 34 + k * 26
                o.append(rect(cx - 12, yy, 104, 22, C["card"], 6, C["stroke"], 1))
                o.append(tx(cx - 4, yy + 16, lbl, 11, C["text"], 800))
                o.append(rect(cx + 50, yy + 3, 36, 16, C["off"], 5))
                o.append(tx(cx + 68, yy + 15, "OFF", 10, "#fff", 800, "middle"))
        o.append(tx(x + 20, y + 190, name, 21, C["text"], 900))
        for j, ln in enumerate(lines):
            o.append(tx(x + 20, y + 220 + j * 24, ln, 14.5, "#e3e6fb", 500))
    save(f"controls.{L}.svg", svg(W, H, "".join(o), s["alt_controls"]))


def arrow(x1, y1, x2, y2, col="#ffffff"):
    import math
    ang = math.atan2(y2 - y1, x2 - x1)
    hx, hy = x2 - math.cos(ang) * 4, y2 - math.sin(ang) * 4
    pts = []
    for da, ln in [(0, 0), (2.6, 24), (-2.6, 24)]:
        pts.append((x2 + math.cos(ang + da) * ln if ln else x2, y2 + math.sin(ang + da) * ln if ln else y2))
    return (f'<path d="M{x1:.1f} {y1:.1f} L{hx:.1f} {hy:.1f}" stroke="{col}" stroke-width="5" '
            f'stroke-dasharray="3 12" stroke-linecap="round" opacity="0.75"/>'
            f'<polygon points="{" ".join(f"{px:.1f},{py:.1f}" for px, py in pts)}" fill="{col}"/>')


def camera_icon(x, y, tilt):
    """Kamera kecil dengan garis arah bidik (tilt: -1 atas, 1 bawah)."""
    return (rect(x, y, 40, 26, C["inp"], 6, "#000", 2, extra='stroke-opacity="0.35"')
            + f'<circle cx="{x+20}" cy="{y+13}" r="7" fill="{C["bg"]}" stroke="#fff" stroke-width="2.5"/>'
            + f'<path d="M{x+44} {y+13} l18 {tilt*14}" stroke="#fff" stroke-width="3" stroke-linecap="round"/>')


def joystick_icon(x, y):
    return (f'<circle cx="{x}" cy="{y}" r="20" fill="{C["inp"]}" stroke="#000" stroke-opacity="0.35" stroke-width="2"/>'
            f'<circle cx="{x}" cy="{y-8}" r="10" fill="{C["accent"]}"/>')


def fly(L):
    import math
    s = STR[L]
    W, H, G = 1280, 450, 372
    o = [scene(W, H, G, seed=17, clouds=True)]
    half = W / 2
    for k, key in enumerate(["fly_up", "fly_down"]):
        title, sub = s[key]
        x0 = 30 + k * half
        bw = half - 60
        o.append(block(x0, 24, bw, 70, C["card"], 12, 6))
        o.append(tx(x0 + 22, 68, title, 26, C["on"] if k == 0 else C["red"], 900, extra='letter-spacing="1"'))
        o.append(tx(x0 + 22 + len(title) * 21 + 18, 66, sub, 14, "#e3e6fb", 600))
        o.append(camera_icon(x0 + bw - 122, 46, -1 if k == 0 else 1))
        o.append(joystick_icon(x0 + bw - 36, 59))
        cx = x0 + bw / 2
        if k == 0:
            x1, y1, x2, y2 = cx - 160, G - 40, cx + 90, G - 210
        else:
            x1, y1, x2, y2 = cx - 160, 140, cx + 90, G - 50
        o.append(arrow(x1, y1, x2, y2))
        rot = math.degrees(math.atan2(x2 - x1, -(y2 - y1)))
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        fx, fy = mx - 40 * math.sin(math.radians(rot)), my + 40 * math.cos(math.radians(rot))
        o.append(avatar(fx, fy, 1.0, rot=rot))
    o.append(tx(W / 2, H - 20, s["fly_note"], 16, "#ffffff", 700, "middle"))
    save(f"fly.{L}.svg", svg(W, H, "".join(o), s["alt_fly"]))


def safety(L):
    s = STR[L]
    W, H, G = 1280, 270, 216
    o = [scene(W, H, G, seed=21, clouds=False)]
    cw, gap = 396, 20
    x0 = (W - (3 * cw + 2 * gap)) / 2
    cols = [BLUE, ORANGE, C["red"]]
    for i, (name, lines) in enumerate(s["safety"]):
        x, y = x0 + i * (cw + gap), 24
        o.append(block(x, y, cw, 164, C["card"], 14, 7))
        o.append(block(x + 18, y + 18, 56, 56, cols[i], 10, 4))
        if i == 0:   # layar / client
            o.append(rect(x + 28, y + 30, 36, 24, "none", 3, "#fff", 4))
            o.append(rect(x + 38, y + 58, 16, 4, "#fff", 1))
        elif i == 1:  # perisai
            o.append(f'<path d="M{x+46} {y+28} l16 6 v12 q0 14 -16 22 q-16 -8 -16 -22 v-12 Z" fill="#fff"/>')
        else:        # segitiga peringatan
            o.append(f'<path d="M{x+46} {y+28} L{x+66} {y+62} H{x+26} Z" fill="#fff"/>')
            o.append(rect(x + 44, y + 38, 4, 13, cols[i], 1))
            o.append(rect(x + 44, y + 54, 4, 4, cols[i], 1))
        o.append(tx(x + 90, y + 54, name, 22, C["text"], 900))
        for j, ln in enumerate(lines):
            o.append(tx(x + 20, y + 100 + j * 23, ln, 15, "#e3e6fb", 500))
    save(f"safety.{L}.svg", svg(W, H, "".join(o), s["alt_safety"]))


def social():
    W, H, G = 1280, 640, 552
    o = [scene(W, H, G, seed=29)]
    o.append(chip(80, 84, "ROBLOX EXECUTOR PANEL", C["accent"], size=15, h=34)[0])
    o.append(title3d(80, 262, "LIVIA", 150, depth=9))
    o.append(title3d(80, 400, "PANEL", 150, depth=9))
    x = 82
    for label, col in [("SPEED", ORANGE), ("JUMP", BLUE), ("FLY", "#8b6cff"), ("GHOST", SLATE), ("ESP", C["red"])]:
        c, w = chip(x, 452, label, col, size=15, pad=14, h=34)
        o.append(c)
        x += w + 14
    o.append(panel(840, 90, 1.12, on={"Speed": 1, "Fly": 1, "ESP": 1}))
    o.append(avatar(1226, G + 20, 1.3, esp=True))
    o.append(avatar(770, 190, 0.9, rot=64))
    save("social-preview.svg", svg(W, H, "".join(o), "Livia Panel: Roblox executor panel"))
    try:
        import cairosvg
        cairosvg.svg2png(url=os.path.join(OUT, "social-preview.svg"),
                         write_to=os.path.join(OUT, "social-preview.png"))
        print("ok social-preview.png")
    except Exception as e:  # cairosvg opsional
        print("lewati PNG:", e)


if __name__ == "__main__":
    for lang in ("id", "en"):
        banner(lang)
        preview(lang)
        features(lang)
        workflow(lang)
        controls(lang)
        fly(lang)
        safety(lang)
    social()
