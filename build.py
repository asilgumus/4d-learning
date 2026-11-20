#!/usr/bin/env python3
"""Statik siteyi content/*.json dosyalarından üretir:  python3 build.py"""
import json, html, os, pathlib, re
from urllib.parse import quote
R = pathlib.Path(__file__).parent
C = R / "content"; S = R / "site"
J = lambda p: json.load(open(C / p, encoding="utf-8"))
e = html.escape
MODS, EXPS, COURSES, BUILDS = J("modules.json"), J("experiments.json"), J("courses.json"), J("builds.json")
ARD, SETS, LEGOG = J("arduino.json"), J("sets.json"), J("lego-mr-guide.json")
LV = {"ilkokul": "İlkokul", "ortaokul": "Ortaokul", "lise": "Lise", "noro": "Nöroçeşitli çocuklar", "mr": "MR'a girecek çocuklar"}
PICK = [("all", "herkes için içerik arıyorum"), ("ilkokul", "ilkokul öğretmeniyim"), ("ortaokul", "ortaokul öğretmeniyim"), ("lise", "lise öğretmeniyim"),
        ("noro", "nöroçeşitli çocuklarla çalışıyorum"), ("mr", "MR'a girecek bir çocuğun yakınıyım")]

def page(title, body, depth=0, desc="", extra_head="", cls=""):
    p = "../" * depth
    d = desc or "FRC 6429 4th Dimension takımının, okulların ve kurumların ücretsiz kullanabileceği açık eğitim içerikleri."
    return f'''<!doctype html><html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title><meta name="description" content="{e(d)}"><meta name="theme-color" content="#e31b2f">
<link rel="icon" href="{p}assets/img/4d-logo.png"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}assets/app.css">{extra_head}</head><body class="{cls}">
<a class="skip" href="#main">İçeriğe geç</a>
<header class="top"><div class="wrap"><a class="brand" href="{p}index.html"><img src="{p}assets/img/4d-logo.png" alt=""><span><b>4D Learning</b><small>FRC 6429 4th Dimension</small></span></a>
<nav class="main" aria-label="Ana menü"><a href="{p}index.html#kutuphane">Kütüphane</a><a href="https://frc6429.com" rel="noopener">Takım</a></nav></div></header>
<main id="main">{body}</main>
<footer><div class="wrap"><div><b>4D Learning</b><p>FRC 6429 4th Dimension, İzmir. İçerikler okullar, STK'lar ve takımlar için ücretsizdir. Kaynak göstererek kullanın, uyarlayın, paylaşın. adg</p></div>
<div><p><a href="mailto:frc4thdimension@gmail.com">frc4thdimension@gmail.com</a></p><p><a href="https://frc6429.com">frc6429.com</a> · <a href="https://www.instagram.com/frc4thdimension/">Instagram</a> · <a href="https://github.com/asilgumus">GitHub</a></p></div></div></footer>
<script src="{p}assets/app.js"></script></body></html>'''

TINT = [("#eef1f6", "#0b2a43")]
def tint(m): t = TINT[(m["no"] - 1) % len(TINT)]; return f'--t:{t[0]};--tf:{t[1]}'
def chips(m): return "".join(f'<span class="chip lv">{LV[l]}</span>' for l in m["levels"])

def index():
    def srch(m): return " ".join([m["title"], m["tagline"], m["summary"], m["kind"], " ".join(LV[l] for l in m["levels"]), " ".join(m["contents"])])
    rows = "".join(f'''<a class="row" href="m/{m["id"]}.html" data-levels="{" ".join(m["levels"])}" data-search="{e(srch(m))}" style="{tint(m)}">
<span class="no">{m["no"]}</span><div><h2>{e(m["title"])}</h2><p>{e(m["tagline"])}</p><div class="meta">{chips(m)}<span class="chip">{e(m["kind"])}</span><span class="chip">{e(m["minutes"])}</span></div></div><span class="go">Aç</span></a>''' for m in MODS)
    FL = [("all", "Tümü"), ("ilkokul", "İlkokul"), ("ortaokul", "Ortaokul"), ("lise", "Lise"), ("noro", "Nöroçeşitli çocuklar"), ("mr", "MR'a girecek çocuklar")]
    btns = "".join(f'<button type="button" data-who="{k}" aria-pressed="{str(k=="all").lower()}">{e(v)}</button>' for k, v in FL)
    body = f'''<section class="hero"><img class="hero-img" src="assets/img/hero.jpg" alt="4D bayrağı, bir FIRST Robotics yarışma salonunun üzerinde" width="1672" height="941" fetchpriority="high"><div class="wrap hero-in"><div class="hero-copy"><h1>Okulların ve kurumların doğrudan kullanabileceği eğitim içerikleri.</h1>
<p class="lede">FRC 6429 4th Dimension takımı tarafından hazırlanan sunumlar, yapım kitapçıkları, deney videoları ve açık kaynak çizimler. İndir, sınıfında veya kurumunda kullan.</p>
<div class="btns"><a class="btn p" href="#kutuphane">Kütüphaneye git</a></div></div></div></section>
<div class="wrap"><section id="kutuphane" class="lib" aria-label="Kütüphane"><div class="lib-card"><div class="lib-head"><h2>Kütüphane</h2><p class="count"><span id="count">7</span> modül</p></div>
<div class="fbar"><label class="search"><span class="sr">Kütüphanede ara</span><input id="q" type="search" placeholder="Modül, konu veya içerik ara" autocomplete="off"></label>
<div class="filter" role="group" aria-label="Kimin için"><span>Kimin için</span>{btns}</div></div></div>
<div class="shelf">{rows}</div><div class="empty" id="empty" hidden><p>Eşleşen modül yok. Aramayı veya filtreyi değiştir.</p><button class="btn" id="reset" type="button">Filtreleri temizle</button></div></section></div>
<section class="band team"><div class="wrap"><div class="team-grid"><div class="team-copy"><h2>Robot yapan bir takımdan, herkese açık eğitim.</h2><p>4th Dimension, İzmir'den bir FIRST Robotics takımı. Robotik çalışmalarının yanında okullara, çocuklara ve ailelere yönelik eğitim projeleri yürütüyoruz. Buradaki içerikler bu çalışmalardan çıkıyor ve ücretsiz.</p><div class="btns"><a class="btn" href="https://frc6429.com">Takımı tanı</a><a class="btn" href="mailto:frc4thdimension@gmail.com">Bize yaz</a></div></div>
<div class="team-photos"><img src="assets/img/takim.jpg" alt="4th Dimension takım üyeleri" loading="lazy"><img src="assets/img/etkinlik-1.jpg" alt="Takım üyeleri bir etkinlikte" loading="lazy"><img src="assets/img/etkinlik-2.jpg" alt="Çocuklara yönelik bir etkinlik" loading="lazy"></div></div></div></section>'''
    return page("4D Learning: açık eğitim kütüphanesi", body, cls="landing")

def deck_html(slides, imgs=None, label="Sunum"):
    out = []
    if imgs:
        for i, src in enumerate(imgs):
            out.append(f'<div class="slide"><img src="../{src}" alt="{label} {i+1}. slayt" {"" if i==0 else "loading=lazy"}></div>')
    else:
        for s in slides:
            t = s["t"]; h = e(s.get("h", ""))
            if t == "cover": x = f'<div class="sl cover"><h3>{h}</h3><p>{e(s["sub"])}</p></div>'
            elif t == "statement": x = f'<div class="sl stmt"><h3>{h}</h3><p>{e(s["text"])}</p></div>'
            elif t == "activity": x = f'<div class="sl act"><h3>{h}</h3><p>{e(s["text"])}</p></div>'
            elif t == "compare":
                col = lambda c: f'<div><h4>{e(c["title"])}</h4><ul>{"".join(f"<li>{e(i)}</li>" for i in c["items"])}</ul></div>'
                x = f'<div class="sl"><h3>{h}</h3><div class="cmp">{col(s["left"])}{col(s["right"])}</div></div>'
            else: x = f'<div class="sl"><h3>{h}</h3><ul>{"".join(f"<li>{e(i)}</li>" for i in s["items"])}</ul></div>'
            out.append(f'<div class="slide">{x}</div>')
    return f'''<div class="deck" aria-label="{label}"><div class="stage">{"".join(out)}</div><div class="bar"><i></i></div>
<div class="dctl"><button data-prev aria-label="Önceki slayt">Geri</button><span class="cnt" aria-live="polite"></span><button data-next aria-label="Sonraki slayt">İleri</button><span class="sp"></span><button data-full>Tam ekran</button></div></div>
<p style="color:var(--muted);font-size:14px;margin:8px 0 0">Ok tuşları veya kaydırma ile ilerle.</p>'''

def sec(title, sub, inner): return f'<section class="msec"><h2>{e(title)}</h2>' + (f'<p class="sub">{e(sub)}</p>' if sub else "") + inner + '</section>'
def slot(what, path): return f'<div class="todo"><b>{e(what)}</b> yüklenecek. Dosyayı <code>site/{path}</code> konumuna koyup <code>content/builds.json</code> içindeki yolu yaz, sonra <code>python3 build.py</code> çalıştır.</div>'
def has(path): return bool(path) and (S / path).exists()
def panels(items): return '<div class="grid2">' + "".join(f'<div class="panel"><h3>{e(h)}</h3><p>{e(p)}</p></div>' for h, p in items) + '</div>'

def module(m):
    i = m["id"]; b = ""
    if i == "siber-guvenlik":
        imgs = sorted(str(p.relative_to(S)) for p in (S / "assets/slides/cybersecurity").glob("*.jpg"))
        b += sec("Sunum", "17 slayt, Türkçe. Tam ekranda göster ya da PDF olarak indir.", deck_html(None, imgs, "Siber güvenlik sunumu") + '<div class="btns"><a class="btn p" href="../assets/docs/siber-guvenlik-sunum-tr.pdf" download>PDF indir</a></div>')
        b += sec("Tartışma soruları", "Sunumdan sonra sınıfla konuşmak için.", panels([("Parola", "Senin parolan hangi bilgilerden oluşuyor? Biri tahmin edebilir mi?"), ("Link", "Bilmediğin birinden link gelirse ilk ne yaparsın? Kime gösterirsin?"), ("Wi-Fi", "Kafedeki açık Wi-Fi ile banka uygulamasına girmek neden riskli?"), ("Zorbalık", "Çevrimiçi biri sana kötü davranırsa kime anlatırsın, hangi kanıtları saklarsın?")]))
        b += sec("Sunucu notları", "", panels([("Süre", "Sunum 15 dk, tartışma 15 dk, parola oyunu 10 dk."), ("Parola oyunu", "Her çocuk kendi parola kuralını (gerçek parolasını değil) kağıda yazar; sınıf güçlü mü zayıf mı olduğunu oylar."), ("Dikkat", "Çocuklardan gerçek parola veya kişisel bilgi istemeyin.")]))
    elif i == "teknoloji-bagimliligi":
        d = J("decks/teknoloji-bagimliligi.json")
        b += sec("Sunum", "14 slayt. Tartışma temelli: slaytlar arasında durup sınıfa soru sor.", deck_html(d["slides"], label="Teknoloji bağımlılığı sunumu"))
        b += sec("Aile etkinliği", "Anlaşmayı yazdır, evde birlikte doldurun.", '<div class="btns"><a class="btn p" href="../anlasma.html">Dijital denge anlaşması</a></div>')
    elif i == "uretim-ve-montaj":
        b += sec("Bu sayfada ne var?", "Üç parça var, bu sırayla ilerle.", panels([("1. Giriş sunumu", "Konuya giriş: bir ürün fabrikaya gelmeden önce neler olur, üretim ve montaj nasıl işler, robotlar ne yapar, sürdürülebilirlik. Türkçe ve İngilizce."), ("2. Yapım kitapçığı", "Her modelin inşa aşamaları: hangi parça önce takılır, nereye oturur. Adım adım resimli, Türkçe ve İngilizce."), ("3. Teknik çizim", "Modeli kendin üretmek için SolidWorks (CAD) dosyaları: her parça ayrı dosya, tüm parçaların birleşimi de montaj dosyası olarak var.")]))
        imgs = lambda d: sorted((str(q.relative_to(S)) for q in (S / f"assets/slides/{d}").glob("*.jpg")), key=lambda s: int(re.findall(r"(\d+)\.jpg", s)[0]))
        b += sec("1. Giriş sunumu", "Türkçe sunum; tam ekranda göster ya da PDF indir.", deck_html(None, imgs("uretim-tr"), "Endüstriyel üretim ve montaj sunumu") + '<div class="btns"><a class="btn p" href="../assets/docs/uretim/sunum/endustriyel-uretim-ve-montaj-tr.pdf" download>PDF indir (Türkçe)</a><a class="btn" href="../assets/docs/uretim/sunum/industrial-manufacturing-and-assembly-en.pdf" download>PDF (English)</a></div><details class="les" style="margin-top:18px"><summary><span>English version of the presentation</span><span>9 slides</span></summary><div style="padding-top:12px">' + deck_html(None, imgs("uretim-en"), "Industrial production and assembly presentation").replace("Ok tuşları veya kaydırma ile ilerle.", "Use arrow keys or swipe.") + '</div></details>')
        cards = ""
        for x in SETS:
            cards += f'''<div class="panel" style="margin-bottom:20px"><div style="display:grid;grid-template-columns:minmax(0,200px) 1fr;gap:24px;align-items:start"><img src="../assets/img/uretim/{x["img_tr"]}/p-01.jpg" alt="{e(x["title"])} kitapçığı kapağı" style="width:100%;border:1px solid var(--line);border-radius:8px" loading="lazy"><div><h3>{e(x["title"])}</h3><p>{e(x["intro"])}</p>
<div class="btns" style="margin-top:14px"><a class="btn p" href="../set/{x["id"]}.html">Kitapçığı ve çizimleri aç</a></div>
<p style="font-size:14px;color:var(--muted);margin:14px 0 0">Doğrudan indir: <a href="../assets/docs/uretim/{x["booklet_tr"]}" download>kitapçık (TR)</a> · <a href="../assets/docs/uretim/{x["booklet_en"]}" download>booklet (EN)</a> · <a href="../assets/docs/uretim/{x["cad"]}" download>SolidWorks çizimleri (ZIP)</a></p></div></div></div>'''
        b += sec("2. Yapım kitapçıkları ve 3. teknik çizimler", BUILDS[i]["drawings_license"], cards)
    elif i == "lego-mr":
        d = BUILDS[i]
        b += sec("Yapım kılavuzu", LEGOG["note"], '<div class="grid2">' + "".join(f'<div class="panel"><h3>{e(x["h"])}</h3><p>{e(x["p"])}</p></div>' for x in LEGOG["phases"]) + '</div><h3 style="margin:26px 0 10px">Bitince kontrol et</h3><div class="panel"><ul style="margin:0;padding-left:20px;color:var(--muted)">' + "".join(f"<li>{e(t)}</li>" for t in LEGOG["tests"]) + '</ul></div><div style="height:16px"></div>' + vtag("assets/video/lego-mr.mp4", "LEGO MR yapım kılavuzu") + (f'<div class="btns"><a class="btn p" href="../{d["booklet"]}" download>Adım adım talimatı indir (PDF)</a></div>' if has(d["booklet"]) else slot("Fotoğraflı adım adım talimat (PDF)", "assets/docs/lego-mr/yapim-talimati.pdf")))
        b += sec("Çocuğa MR'ı nasıl anlatırız?", "Çocuk ne bekleyeceğini bilirse kaygısı azalır. Modeli kurarken bu dört cümleyi kullanın.", panels([(x["h"], x["p"]) for x in d["prep"]]))
        b += sec("Aileye not", "", '<div class="panel"><ul style="margin:0;padding-left:20px;color:var(--muted)">' + "".join(f"<li>{e(x)}</li>" for x in d["family"]) + '</ul></div>')
    elif i == "neurobridge":
        d = BUILDS[i]
        b += sec("Oyunu oyna", "Tarayıcıda çalışır, kurulum gerekmez.", f'<div class="frame"><iframe src="{d["live"]}" title="NeuroBridge oyunu" loading="lazy" allow="fullscreen"></iframe></div><div class="btns"><a class="btn p" href="{d["live"]}" rel="noopener">Tam ekran aç</a><a class="btn" href="{d["repo"]}" rel="noopener">Kaynak kod (GitHub)</a></div>')
        b += sec("Eğitmen ve aile rehberi", "", panels([(x["h"], x["p"]) for x in d["guide"]]))
    elif i == "sense-of-science":
        b += sec("Deneyler", "Her deney için yazdırılabilir kitapçık ve sesli anlatım videosu.", '<div class="grid2">' + "".join(f'<a class="ex" href="../deney/{x["id"]}.html"><div><b>{e(x["title"])}</b><span>{x["minutes"]} dk · {len(x["materials"])} malzeme</span></div></a>' for x in EXPS) + '</div>')
        b += sec("Genel güvenlik", "", panels([("Yetişkin gözetimi", "Tüm deneyler bir yetişkinle yapılır."), ("Gözlük ve önlük", "Gözleri ve kıyafeti koruyun, sıvıları içmeyin."), ("Temizlik", "Bitince çalışma alanını silin, elleri yıkayın.")]))
    elif i == "cad-elektronik-yazilim":
        courses = COURSES[:1] + [{"id":"elektronik","title":"Elektronik: Arduino ile devre","tools":"Arduino Uno, breadboard, LED, direnç, sensörler","goal":"Basit LED'den küçük robota 19 deneyle fiziksel programlama.","ard":True,"lessons":[]}] + COURSES[1:]
        tb = "".join(f'<button role="tab" data-tab="{c["id"]}" aria-selected="{str(k==0).lower()}">{e(c["title"].split(":")[0])}</button>' for k, c in enumerate(courses))
        ps = ""
        for k, c in enumerate(courses):
            if c.get("ard"):
                ls = '<div class="grid2">' + "".join(f'<a class="ex" href="../elektronik/{a["id"]:02d}.html"><span class="em" style="font-weight:600;font-weight:800;color:var(--red)">{a["id"]:02d}</span><div><b>{e(a["title"])}</b><span>{e(a["level"])} · {e(a["time"])}</span></div></a>' for a in ARD) + '</div>'
            else:
                ls = "".join(f'<details class="les"><summary><span>{n+1}. {e(l["t"])}</span><span >{"Video" if (l["yt"] or (S / f'assets/video/ders/{c["id"]}-{n+1:02d}.mp4').exists()) else "Yazılı ders"}</span></summary><p>{e(l["d"])}</p><ol style="color:var(--muted)">{"".join(f"<li>{e(x)}</li>" for x in l["steps"])}</ol><p><b style="color:var(--ink)">Görev:</b> {e(l["task"])}</p>' + (f'<div class="video" style="margin-top:12px"><iframe src="https://www.youtube-nocookie.com/embed/{l["yt"]}" title="{e(l["t"])}" loading="lazy" allowfullscreen></iframe></div>' if l["yt"] else vtag(f'assets/video/ders/{c["id"]}-{n+1:02d}.mp4', l["t"]).replace('<figure style="margin:0">','<figure style="margin:12px 0 0">')) + '</details>' for n, l in enumerate(c["lessons"]))
            ps += f'<div data-panel="{c["id"]}" {"" if k==0 else "hidden"}><div class="panel" style="margin-bottom:16px"><h3>{e(c["title"])}</h3><p>{e(c["goal"])} Gerekenler: {e(c["tools"])}.</p></div>{ls}</div>'
        b += sec("Müfredatlar", "Üç yolu da sırayla ya da istediğin dersten başlayarak izle. Her dersin altında sesli anlatım videosu var.", f'<div class="tabs" role="tablist" data-tabs>{tb}</div>{ps}')
    head = f'''<div class="mband" style="{tint(m)}"><div class="wrap"><div class="mhead"><a class="crumb" href="../index.html">← Kütüphane</a><h1>{e(m["title"])}</h1><p>{e(m["summary"])}</p><div class="meta">{chips(m)}<span class="chip">{e(m["minutes"])}</span></div></div></div></div><div class="wrap">{b}</div><div style="height:48px"></div>'''
    return page(f'{m["title"]} · 4D Learning', head, 1, m["tagline"])

def vtag(rel, title):
    p = S / rel
    if not p.exists(): return ""
    return f'<figure style="margin:0"><video class="video" controls preload="none" poster="../{rel[:-4]}.jpg" title="{e(title)}"><source src="../{rel}" type="video/mp4"></video><figcaption style="color:var(--muted);font-size:14px;margin-top:6px">Sesli anlatım videosu (Türkçe, sentetik ses). Çekim videosu eklenince yerini alır.</figcaption></figure>'

def booklet(x):
    vid = f'<div class="video"><iframe src="https://www.youtube-nocookie.com/embed/{x["youtube"]}" title="{e(x["title"])}" loading="lazy" allowfullscreen></iframe></div>' if x["youtube"] else (vtag(f'assets/video/deney/{x["id"]}.mp4', x["title"]) or '<div class="vslot">Deney videosu hazırlanıyor</div>')
    li = lambda a: "".join(f"<li>{e(i)}</li>" for i in a)
    body = f'''<div class="toolbar"><a class="crumb" href="../m/sense-of-science.html">← Sense of Science</a><button class="btn p" id="print">Yazdır / PDF</button></div>
<article class="book"><h1>{e(x["title"])}</h1><p style="color:var(--muted)">Süre: {x["minutes"]} dakika · FRC 6429 Sense of Science</p>
<h2>Malzemeler</h2><ul>{li(x["materials"])}</ul><h2>Yapılış</h2><ol>{li(x["steps"])}</ol><h2>Neden oldu?</h2><p class="why">{e(x["why"])}</p>
<h2>Düşün ve dene</h2><ul>{li(x["questions"])}</ul><h2>Güvenlik</h2><p class="safe">{e(x["safety"])} Deneyi bir yetişkinle birlikte yap.</p>
<h2>Gözlemlerim</h2><div class="write"></div><div class="write"></div><div class="write"></div><div style="margin:30px 0 0" class="no-print">{vid}</div></article><div style="height:48px"></div>'''
    return page(f'{x["title"]} · deney kitapçığı', f'<div class="wrap">{body}</div>', 1)

def agreement():
    L = lambda t: f'<p style="margin:18px 0 0"><b>{t}</b></p><div class="write"></div><div class="write"></div>'
    body = f'''<div class="wrap"><div class="toolbar"><a class="crumb" href="m/teknoloji-bagimliligi.html">← Teknoloji Bağımlılığı</a><button class="btn p" id="print">Yazdır / PDF</button></div>
<article class="book"><h1>Dijital denge anlaşması</h1><p style="color:var(--muted)">Ailece birlikte doldurun. Herkes imzalar.</p>
{L("Ekransız saatlerimiz (ör. yemek, ders, yatmadan 1 saat önce)")}{L("Ekransız mekânlarımız (ör. yemek masası, yatak odası)")}{L("Haftalık ekransız aktivitemiz")}{L("Herkesin uyacağı bir kural")}{L("Kuralı bozarsak ne yaparız?")}
<p style="margin-top:30px"><b>İmzalar:</b></p><div class="write"></div><div class="write"></div></article><div style="height:48px"></div></div>'''
    return page("Dijital denge anlaşması · 4D Learning", body)

def setpage(x):
    li = lambda a: "".join(f"<li>{e(i)}</li>" for i in a)
    steps = "".join(f"<li>{e(s)}</li>" for s in x["steps"])
    pg = lambda d: "".join(f'<img src="../assets/img/uretim/{d}/p-{n:02d}.jpg" alt="{e(x["title"])} kitapçığı, sayfa {n}" loading="lazy" style="width:100%;border:1px solid var(--line);border-radius:8px;margin:0 0 14px;background:#fff">' for n in range(1, x["pages"] + 1))
    stls = sorted((q for q in (S / f"assets/models/{x['id']}").glob("*.stl")), key=lambda q: (not re.match(r"(montaj|assembly)", q.stem.lower()), q.stem.lower())) if (S / f"assets/models/{x['id']}").exists() else []
    if stls:
        fj = e(json.dumps([{"name": q.stem, "url": f"../assets/models/{x['id']}/{quote(q.name)}"} for q in stls], ensure_ascii=False))
        opts = "".join(f'<option value="{n}">{e(q.stem)}</option>' for n, q in enumerate(stls))
        viewer = f'''<div class="viewer" data-files="{fj}"><div class="v-bar"><label>Parça <select aria-label="Parça seç">{opts}</select></label><button class="btn v-reset" type="button">Görünümü sıfırla</button><span class="v-dim"></span></div><div class="v-canvas" role="img" aria-label="{e(x["title"])} 3B önizleme"><div class="v-status">Yükleniyor…</div></div><div class="v-hint">Sürükle: döndür · Tekerlek veya iki parmak: yakınlaştır · Sağ tuş: kaydır</div></div>'''
    else:
        viewer = f'<div class="todo"><b>3B önizleme</b> için STL dosyaları yüklenecek. SolidWorks\'te <i>Dosya, Farklı kaydet, STL</i> ile dışa aktarıp <code>site/assets/models/{x["id"]}/</code> klasörüne koy (montaj dosyası <code>Montaj.stl</code> adıyla), sonra <code>python3 build.py</code> çalıştır.</div>'
    stlz = f"assets/docs/uretim/cizim/{x['id']}-stl.zip"
    stlbtn = f'<a class="btn" href="../{stlz}" download>STL dosyaları (ZIP)</a>' if (S / stlz).exists() else ""
    body = f'''<div class="wrap"><div class="toolbar"><a class="crumb" href="../m/uretim-ve-montaj.html">← Endüstriyel Üretim ve Montaj</a><button class="btn p" id="print">Yazdır / PDF</button></div>
<article class="book"><h1>{e(x["title"])}</h1><p style="color:var(--muted)">{e(x["kind"])} · {e(x["level"])}</p><p>{e(x["intro"])}</p>
<h2>3B önizleme</h2>{viewer}
<h2>Adımlar bir bakışta</h2><ol>{steps}</ol>
<h2>Yapım kitapçığı</h2><p>Resimli adımlar aşağıda. Yazdırmak için PDF'i indir.</p><div class="btns" style="margin:0 0 16px"><a class="btn p" href="../assets/docs/uretim/{x["booklet_tr"]}" download>Kitapçık PDF (Türkçe)</a><a class="btn" href="../assets/docs/uretim/{x["booklet_en"]}" download>Booklet PDF (English)</a></div>
{pg(x["img_tr"])}
<details class="les"><summary><span>English booklet pages</span><span>{x["pages"]} pages</span></summary><div style="padding-top:12px">{pg(x["img_en"])}</div></details>
<h2>Teknik çizimler (SolidWorks)</h2><p>Bu modelin her parçası ayrı <code>.SLDPRT</code> dosyası, hepsinin birleşimi <code>.SLDASM</code> montaj dosyasıdır. Parçaları açmak için SolidWorks gerekir; yalnızca bakmak istersen ücretsiz eDrawings görüntüleyici yeterli. Lazer kesim ya da 3B baskı için SolidWorks'ten STEP, DXF veya STL olarak dışa aktar.</p>
<div class="btns" style="margin:0 0 12px"><a class="btn p" href="../assets/docs/uretim/{x["cad"]}" download>{e(x["cad_name"])} (ZIP)</a>{stlbtn}</div>
<p><b>Pakette olanlar:</b></p><ul>{li(x["parts"])}</ul>
<p style="color:var(--muted);font-size:14px">Adet, parça adındaki sayıdır (ör. spacer x12 = 12 adet). Kaynak göstererek kullanın: FRC 6429 4th Dimension.</p></article><div style="height:48px"></div></div>'''
    imp = '''<script type="importmap">{"imports":{"three":"https://cdn.jsdelivr.net/npm/three@0.160.1/build/three.module.js","three/addons/":"https://cdn.jsdelivr.net/npm/three@0.160.1/examples/jsm/"}}</script>'''
    return page(f'{x["title"]} · yapım kitapçığı', body + ('<script type="module" src="../assets/viewer.js"></script>' if stls else ""), 1, extra_head=imp if stls else "")

def lesson(a, prev, nxt):
    li = lambda t: "".join(f"<li>{e(i)}</li>" for i in t)
    nav = (f'<a href="{prev:02d}.html">← Önceki</a>' if prev else "<span></span>") + (f'<a href="{nxt:02d}.html">Sonraki →</a>' if nxt else "<span></span>")
    body = f'''<div class="wrap"><div class="toolbar"><a class="crumb" href="../m/cad-elektronik-yazilim.html">← CAD, Elektronik, Yazılım</a><button class="btn p" id="print">Yazdır / PDF</button></div>
<article class="book"><p style="color:var(--muted);font-weight:500;margin:0;font-size:14px">Arduino deneyi {a["id"]:02d}</p><h1>{e(a["title"])}</h1><p style="color:var(--muted)">{e(a["level"])} · {e(a["time"])} · {e(a["concept"])}</p><p>{e(a["summary"])}</p>
{vtag(f"assets/video/elektronik/{a['id']:02d}.mp4", a['title']).replace("Sesli anlatım videosu (Türkçe, sentetik ses)","Sesli anlatım videosu (İngilizce, sentetik ses)")}<h2>Malzemeler</h2><ul>{li(a["materials"])}</ul><h2>Bağlantı</h2><ol>{li(a["wiring"])}</ol><h2>Kod</h2><pre style="background:var(--ink);color:#eef;padding:16px;border-radius:10px;overflow:auto;font-size:14px;line-height:1.5"><code>{e(a["code"])}</code></pre>
<h2>Ne olmalı?</h2><p class="why">{e(a["result"])}</p><h2>Meydan okuma</h2><p>{e(a["challenge"])}</p>
<h2>Güvenlik ve sorun giderme</h2><ul><li>Bağlantıyı değiştirmeden önce gücü kes.</li><li>Her LED ile direnç kullan.</li><li>Kart ve port seçimini Arduino IDE'de kontrol et.</li><li>Her kablonun koddaki pin numarasıyla eşleştiğini doğrula.</li></ul>
<p style="color:var(--muted);font-size:14px">Not: Ders metinleri İngilizcedir. Orijinal Türkçe çalışma kâğıdı PDF olarak indirilebilir.</p>
<div class="btns"><a class="btn p" href="../assets/docs/arduino/experiment-{a["id"]:02d}.pdf" download>Türkçe çalışma kâğıdı (PDF)</a></div>
<nav style="display:flex;justify-content:space-between;margin-top:28px;font-weight:700">{nav}</nav></article><div style="height:48px"></div></div>'''
    return page(f'{a["title"]} · Arduino deneyi', body, 1)

def w(path, txt):
    p = S / path; p.parent.mkdir(parents=True, exist_ok=True); p.write_text(txt, encoding="utf-8")
w("index.html", index()); w("anlasma.html", agreement())
for m in MODS: w(f'm/{m["id"]}.html', module(m))
for x in EXPS: w(f'deney/{x["id"]}.html', booklet(x))
for x in SETS: w(f'set/{x["id"]}.html', setpage(x))
ids = [a["id"] for a in ARD]
for k, a in enumerate(ARD): w(f'elektronik/{a["id"]:02d}.html', lesson(a, ids[k-1] if k else None, ids[k+1] if k+1 < len(ids) else None))
w("robots.txt", "User-agent: *\nAllow: /\n")
print("ok:", len(list(S.rglob("*.html"))), "sayfa")
