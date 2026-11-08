#!/usr/bin/env python3
"""Açık kaynak üretim setlerinin çizimlerini üretir (bağımlılık: numpy).
Set 1: 3B yazıcı için dişli zinciri (STL). Set 2: lazer kesim geçmeli telefon standı (SVG + DXF).
Lisans: CC BY-SA 4.0 - 4th Dimension FRC 6429"""
import math, struct, pathlib
import numpy as np
OUT = pathlib.Path(__file__).resolve().parent.parent / "site/assets/docs/uretim"

# ---------- Set 1: dişliler ----------
M, PA, T_G, BORE = 2.0, math.radians(20), 6.0, 6.3   # modül, basınç açısı, kalınlık, delik (0.3 tolerans)
def inv(rb, r):  # involüt: r yarıçapındaki nokta için kutupsal açı
    a = math.sqrt(max((r / rb) ** 2 - 1, 0)); return a - math.atan(a)
def gear_outline(z, n=8):
    rp = M * z / 2; rb = rp * math.cos(PA); ra = rp + M; rr = rp - 1.25 * M; r0 = max(rb, rr)
    pts = []
    for k in range(z):
        c = 2 * math.pi * k / z; rs = np.linspace(r0, ra, n); hp = math.pi / (2 * z) - 0.15 / (2 * rp)   # 0.15 mm boşluk (backlash)
        right = [(c - hp + (inv(rb, rp) - inv(rb, r)), r) for r in rs]
        left = [(c + hp - (inv(rb, rp) - inv(rb, r)), r) for r in rs[::-1]]
        nxt = c + 2 * math.pi / z - hp + (inv(rb, rp) - inv(rb, r0))
        root = [(left[-1][0] + (nxt - left[-1][0]) * t, r0) for t in (0.33, 0.66)]
        pts += right + left + root
    th = np.maximum.accumulate(np.array([p[0] for p in pts]) + np.arange(len(pts)) * 1e-9)
    return [(r * math.cos(t), r * math.sin(t), t) for (_, r), t in zip(pts, th)]
def tri_ring(outer, rb_hole, h):
    tris = []; n = len(outer)
    O0 = [(x, y, 0) for x, y, _ in outer]; O1 = [(x, y, h) for x, y, _ in outer]
    I0 = [(rb_hole * math.cos(t), rb_hole * math.sin(t), 0) for _, _, t in outer]; I1 = [(a, b, h) for a, b, _ in I0]
    for i in range(n):
        j = (i + 1) % n
        tris += [(O0[i], O0[j], I0[j]), (O0[i], I0[j], I0[i])]            # alt (normal -z): sırayı çevir
        tris += [(O1[i], I1[j], O1[j]), (O1[i], I1[i], I1[j])]            # üst
        tris += [(O0[i], O1[j], O0[j]), (O0[i], O1[i], O1[j])]            # dış duvar
        tris += [(I0[i], I0[j], I1[j]), (I0[i], I1[j], I1[i])]            # delik duvarı
    return [(a, c, b) for a, b, c in tris]   # dış normal dışarı baksın
def write_stl(path, tris, name):
    with open(path, "wb") as f:
        f.write(name.encode()[:80].ljust(80, b" ")); f.write(struct.pack("<I", len(tris)))
        for a, b, c in tris:
            u = np.subtract(b, a); v = np.subtract(c, a); nrm = np.cross(u, v); l = np.linalg.norm(nrm) or 1
            f.write(struct.pack("<12fH", *(nrm / l), *a, *b, *c, 0))
def box(x0, y0, z0, x1, y1, z1):
    v = [(x0,y0,z0),(x1,y0,z0),(x1,y1,z0),(x0,y1,z0),(x0,y0,z1),(x1,y0,z1),(x1,y1,z1),(x0,y1,z1)]
    q = [(0,3,2,1),(4,5,6,7),(0,1,5,4),(1,2,6,5),(2,3,7,6),(3,0,4,7)]
    return [t for a,b,c,d in q for t in ((v[a],v[b],v[c]),(v[a],v[c],v[d]))]
def cyl(cx, cy, r, h, n=48, z0=0):
    t = []
    for i in range(n):
        a0, a1 = 2*math.pi*i/n, 2*math.pi*(i+1)/n
        p0 = (cx+r*math.cos(a0), cy+r*math.sin(a0)); p1 = (cx+r*math.cos(a1), cy+r*math.sin(a1))
        t += [((*p0, z0), (*p1, z0), (cx, cy, z0)), ((*p0, z0+h), (cx, cy, z0+h), (*p1, z0+h)),
              ((*p0, z0), (*p1, z0+h), (*p1, z0)), ((*p0, z0), (*p0, z0+h), (*p1, z0+h))]
    return t
def plate_with_holes(w, d, h, holes, hr, n=32):
    # ızgara tabanlı: basitlik için plaka = kutu; delikler yerine pimler ayrı basılır ve plakaya "pim yuvası" çıkıntısı olarak eklenir
    t = box(0, 0, 0, w, d, h)
    for (x, y) in holes: t += cyl(x, y, 2.8, 12, n, h)  # 5.6 mm sabit pim doğrudan plakaya basılı
    return t
def set1():
    d = OUT / "set-1"; d.mkdir(parents=True, exist_ok=True)
    teeth = [12, 24, 36]; svgs = []
    for z in teeth:
        o = gear_outline(z); write_stl(d / f"disli-{z}T.stl", tri_ring(o, BORE / 2, T_G), f"disli {z}T m={M}")
    xs = [20, 20 + (12 + 24) * M / 2, 20 + (12 + 24) * M / 2 + (24 + 36) * M / 2]
    write_stl(d / "taban-plaka.stl", plate_with_holes(150, 80, 5, [(x, 40) for x in xs], 2.8), "taban plaka + pimler")
    # önizleme SVG
    s = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="-5 -5 160 90" width="640">', '<rect x="0" y="0" width="150" height="80" rx="4" fill="#eee" stroke="#999"/>']
    for z, x in zip(teeth, xs):
        ph = math.pi / z if z == 24 else 0   # önizlemede orta dişli yarım adım döner: dişler boşluğa girer
        o = [(px*math.cos(ph)-py*math.sin(ph), px*math.sin(ph)+py*math.cos(ph), 0) for px, py, _ in gear_outline(z)]; pts = " ".join(f"{x+px:.2f},{40+py:.2f}" for px, py, _ in o)
        s.append(f'<polygon points="{pts}" fill="#e31b2f" fill-opacity=".75" stroke="#7a0c18" stroke-width=".3"/><circle cx="{x}" cy="40" r="{BORE/2}" fill="#fff"/>')
    s.append("</svg>"); (d / "onizleme.svg").write_text("".join(s))
    (d / "uretici-bilgisi.txt").write_text(f"Modül {M} mm, basınç açısı 20°, kalınlık {T_G} mm, delik {BORE} mm.\nDişliler: 12T, 24T, 36T. Eksen mesafeleri: {xs[1]-xs[0]:.0f} mm ve {xs[2]-xs[1]:.0f} mm.\nPimler taban plakaya basılıdır (Ø5.6). Dişli deliği 6.3 mm: yazıcınıza göre 'BORE' değerini değiştirip tools/make_sets.py çalıştırın.\n")
    return xs

# ---------- Set 2: lazer kesim dayanak ----------
T = 3.0; K = 0.1; TABH = 7; BARL = 60; BARH = 15      # kalınlık, yuva payı, tırnak yüksekliği, çubuk boyu/yüksekliği
SLOTS = [(45, 3), (78, 3), (30, 42)]                    # çubuk yuvalarının sol-alt köşeleri (plaka koordinatı)
def plate(ox):
    outer = [(ox+x, y) for x, y in [(0,0),(90,0),(90,12),(60,80),(18,80),(0,40)]]
    holes = [[(ox+x, y), (ox+x+T+K, y), (ox+x+T+K, y+TABH+K), (ox+x, y+TABH+K)] for x, y in SLOTS]
    return outer, holes
def bar(ox, oy):  # gövde BARL x BARH, uçlarda T uzunluğunda TABH yüksekliğinde tırnak
    m = (BARH - TABH) / 2
    return [(ox, oy+m), (ox+T, oy+m), (ox+T, oy), (ox+T+BARL, oy), (ox+T+BARL, oy+m), (ox+2*T+BARL, oy+m),
            (ox+2*T+BARL, oy+m+TABH), (ox+T+BARL, oy+m+TABH), (ox+T+BARL, oy+BARH), (ox+T, oy+BARH), (ox+T, oy+m+TABH), (ox, oy+m+TABH)]
def svg_dxf():
    d = OUT / "set-2"; d.mkdir(parents=True, exist_ok=True)
    p1, p2 = plate(0), plate(100)
    shapes = [("plaka-A", *p1), ("plaka-B", *p2)] + [(f"cubuk-{i+1}", bar(0, 92+i*20), []) for i in range(3)]
    W_, H_ = 200, 155
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-5 -5 {W_+10} {H_+10}" width="{W_*4}" style="background:#fff"><g fill="none" stroke="#e31b2f" stroke-width=".3">']
    dxf = ["0\nSECTION\n2\nENTITIES"]
    for name, o, holes in shapes:
        for poly in [o] + holes:
            svg.append('<polygon points="%s"/>' % " ".join(f"{x:.2f},{H_-y:.2f}" for x, y in poly))
            dxf.append("0\nLWPOLYLINE\n8\nCUT\n90\n%d\n70\n1\n" % len(poly) + "".join(f"10\n{x:.3f}\n20\n{y:.3f}\n" for x, y in poly).rstrip("\n"))
        x0 = min(x for x, _ in o); y0 = min(y for _, y in o)
        svg.append(f'<text x="{x0+2:.1f}" y="{H_-y0-3:.1f}" font-size="4" fill="#555" stroke="none">{name}</text>')
    svg.append("</g></svg>"); dxf.append("0\nENDSEC\n0\nEOF")
    (d / "dayanak.svg").write_text("\n".join(svg)); (d / "dayanak.dxf").write_text("\n".join(dxf))
    (d / "uretici-bilgisi.txt").write_text(f"Malzeme kalınlığı T={T} mm (MDF/kontrplak/akrilik). Yuva payı {K} mm. Birim: mm.\nParçalar: 2 yan plaka, 3 çubuk. Kırmızı çizgi = kesim.\nÇubuklar plakalar arasında {BARL} mm açıklık bırakır. Lazerin kerf'ine göre K değerini değiştirip tools/make_sets.py çalıştırın.\n")
set1(); svg_dxf(); print("üretildi:", sorted(str(p.relative_to(OUT)) for p in OUT.rglob("*") if p.is_file()))
