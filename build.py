#!/usr/bin/env python3
"""Statik siteyi content/*.json dosyalarından üretir:  python3 build.py"""
import json, html, os, pathlib
R = pathlib.Path(__file__).parent
C = R / "content"; S = R / "site"
J = lambda p: json.load(open(C / p, encoding="utf-8"))
e = html.escape
MODS, EXPS, COURSES, BUILDS = J("modules.json"), J("experiments.json"), J("courses.json"), J("builds.json")
LV = {"ilkokul": "İlkokul", "ortaokul": "Ortaokul", "lise": "Lise", "noro": "Nöroçeşitli çocuklar", "mr": "MR'a girecek çocuklar"}
PICK = [("all", "herkes için içerik arıyorum"), ("ilkokul", "ilkokul öğretmeniyim"), ("ortaokul", "ortaokul öğretmeniyim"), ("lise", "lise öğretmeniyim"),
        ("noro", "nöroçeşitli çocuklarla çalışıyorum"), ("mr", "MR'a girecek bir çocuğun yakınıyım")]

def page(title, body, depth=0, desc="", extra_head=""):
    p = "../" * depth
    d = desc or "FRC 6429 4th Dimension takımının, okulların ve kurumların ücretsiz kullanabileceği açık eğitim içerikleri."
    return f'''<!doctype html><html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title><meta name="description" content="{e(d)}"><meta name="theme-color" content="#e31b2f">
<link rel="icon" href="{p}assets/img/4d-logo.png"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800&family=Manrope:wght@400;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}assets/app.css">{extra_head}</head><body>
<a class="skip" href="#main">İçeriğe geç</a>
<header class="top"><div class="wrap"><a class="brand" href="{p}index.html"><img src="{p}assets/img/4d-logo.png" alt=""><span><b>4D Learning</b><small>FRC 6429 4th Dimension</small></span></a>
<nav class="main" aria-label="Ana menü"><a href="{p}index.html#kutuphane">Kütüphane</a><a href="{p}index.html#nasil">Nasıl kullanılır</a><a href="https://frc6429.com" rel="noopener">Takım</a></nav></div></header>
<main id="main">{body}</main>
<footer><div class="wrap"><div><b style="font-family:var(--display);font-size:1.3rem;color:#fff">4D Learning</b><p>FRC 6429 4th Dimension, İzmir. İçerikler okullar, STK'lar ve takımlar için ücretsizdir. Kaynak göstererek kullanın, uyarlayın, paylaşın.</p></div>
<div><p><a href="mailto:frc4thdimension@gmail.com">frc4thdimension@gmail.com</a></p><p><a href="https://frc6429.com">frc6429.com</a> · <a href="https://www.instagram.com/frc4thdimension/">Instagram</a> · <a href="https://github.com/asilgumus">GitHub</a></p></div></div></footer>
<script src="{p}assets/app.js"></script></body></html>'''

def chips(m): return "".join(f'<span class="chip lv">{LV[l]}</span>' for l in m["levels"])

def index():
    rows = "".join(f'''<a class="row" href="m/{m["id"]}.html" data-levels="{" ".join(m["levels"])}" style="--a:{m["accent"]}">
<span class="no">{m["no"]}</span><div><h2>{e(m["title"])}</h2><p>{e(m["tagline"])}</p><div class="meta">{chips(m)}<span class="chip">{e(m["kind"])}</span><span class="chip">{e(m["minutes"])}</span></div></div><span class="go">Aç</span></a>''' for m in MODS)
    opts = "".join(f'<option value="{k}">{e(v)}</option>' for k, v in PICK)
    body = f'''<div class="wrap"><section class="hero"><h1>Ben <span class="pick"><label class="sr" for="who" style="position:absolute;left:-999px">Kim olduğunu seç</label><select id="who">{opts}</select></span></h1>
<p class="lede">Hazır sunumlar, yapım kitapçıkları, deney videoları ve açık kaynak çizimler. Dosyayı indir, sınıfında ya da kurumunda hemen kullan.</p>
<div class="stats"><span><b>7</b>eğitim modülü</span><span><b>{len(EXPS)}</b>deney kitapçığı</span><span><b>{sum(len(c["lessons"]) for c in COURSES)}</b>video ders</span></div></section>
<section id="kutuphane" aria-label="Kütüphane"><div class="shelf">{rows}</div><p class="empty" id="empty" hidden>Bu grup için henüz içerik yok. Önerin varsa bize yaz.</p><p style="color:var(--muted);font-size:14px;margin-top:12px"><span id="count">7</span> modül listeleniyor</p></section></div>
<section class="band" id="nasil"><div class="wrap"><h2>Dört adımda sınıfına getir.</h2><ul class="steps">
<li><b>Seç</b><span>Yaş grubuna uygun modülü bul.</span></li><li><b>İndir</b><span>Sunumu, kitapçığı veya çizimi indir ya da tarayıcıda göster.</span></li><li><b>Uyarla</b><span>Kendi dilin, malzemelerin ve sürene göre değiştir.</span></li><li><b>Uygula</b><span>Çocuklarla yap, geri bildirimini bize yaz.</span></li></ul></div></section>'''
    return page("4D Learning: açık eğitim kütüphanesi", body)

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
        d = J("decks/uretim-ve-montaj.json")
        b += sec("Giriş sunumu", "10 slayt: üretim yolculuğu, tolerans, montaj, güvenlik ve bir montaj hattı oyunu.", deck_html(d["slides"], label="Üretim sunumu"))
        sets = ""
        for s in BUILDS[i]["sets"]:
            bk = f'<div class="btns"><a class="btn p" href="../{s["booklet"]}" download>Kitapçığı indir</a></div>' if has(s["booklet"]) else slot(s["title"] + " kitapçığı", f'assets/docs/uretim/{s["id"]}-kitapcik.pdf')
            dr = "".join(f'<a class="btn" href="../{x}" download>{e(os.path.basename(x))}</a> ' for x in s["drawings"] if has(x)) or slot(s["title"] + " çizimleri (STEP/STL/DXF)", f'assets/docs/uretim/{s["id"]}/')
            sets += f'<div class="panel" style="margin-bottom:20px"><h3>{e(s["title"])}</h3><p>{e(s["desc"])}</p><h4 style="margin:18px 0 8px;font-family:var(--display)">Yapım kitapçığı</h4>{bk}<h4 style="margin:18px 0 8px;font-family:var(--display)">Açık kaynak çizimler</h4>{dr}</div>'
        b += sec("İki set", BUILDS[i]["drawings_license"], sets)
    elif i == "lego-mr":
        d = BUILDS[i]
        b += sec("Yapım talimatı", "LEGO MR setinin SPIKE Prime parçalarıyla yeniden inşa edilmiş hali.", (f'<div class="btns"><a class="btn p" href="../{d["booklet"]}" download>Talimatı indir</a></div>' if has(d["booklet"]) else slot("Yapım talimatı (PDF)", "assets/docs/lego-mr/yapim-talimati.pdf")))
        b += sec("Çocuğa MR'ı nasıl anlatırız?", "Çocuk ne bekleyeceğini bilirse kaygısı azalır. Modeli kurarken bu dört cümleyi kullanın.", panels([(x["h"], x["p"]) for x in d["prep"]]))
        b += sec("Aileye not", "", '<div class="panel"><ul style="margin:0;padding-left:20px;color:var(--muted)">' + "".join(f"<li>{e(x)}</li>" for x in d["family"]) + '</ul></div>')
    elif i == "neurobridge":
        d = BUILDS[i]
        b += sec("Oyunu oyna", "Tarayıcıda çalışır, kurulum gerekmez.", f'<div class="frame"><iframe src="{d["live"]}" title="NeuroBridge oyunu" loading="lazy" allow="fullscreen"></iframe></div><div class="btns"><a class="btn p" href="{d["live"]}" rel="noopener">Tam ekran aç</a><a class="btn" href="{d["repo"]}" rel="noopener">Kaynak kod (GitHub)</a></div>')
        b += sec("Eğitmen ve aile rehberi", "", panels([(x["h"], x["p"]) for x in d["guide"]]))
    elif i == "sense-of-science":
        b += sec("Deneyler", "Her kitapçık yazdırılabilir; videosu eklendiğinde aynı sayfada oynar.", '<div class="grid2">' + "".join(f'<a class="ex" href="../deney/{x["id"]}.html"><span class="em" aria-hidden="true">{x["emoji"]}</span><div><b>{e(x["title"])}</b><span>{x["minutes"]} dk · {len(x["materials"])} malzeme</span></div></a>' for x in EXPS) + '</div>')
        b += sec("Genel güvenlik", "", panels([("Yetişkin gözetimi", "Tüm deneyler bir yetişkinle yapılır."), ("Gözlük ve önlük", "Gözleri ve kıyafeti koruyun, sıvıları içmeyin."), ("Temizlik", "Bitince çalışma alanını silin, elleri yıkayın.")]))
    elif i == "cad-elektronik-yazilim":
        tb = "".join(f'<button role="tab" data-tab="{c["id"]}" aria-selected="{str(k==0).lower()}">{e(c["title"].split(":")[0])}</button>' for k, c in enumerate(COURSES))
        ps = ""
        for k, c in enumerate(COURSES):
            ls = "".join(f'<details class="les"><summary><span>{n+1}. {e(l["t"])}</span><span style="color:var(--muted);font-weight:600">{"Video" if l["yt"] else "Yakında"}</span></summary><p>{e(l["d"])}</p>' + (f'<div class="video" style="margin-top:12px"><iframe src="https://www.youtube-nocookie.com/embed/{l["yt"]}" title="{e(l["t"])}" loading="lazy" allowfullscreen></iframe></div>' if l["yt"] else '<div class="vslot" style="margin-top:12px">Video hazırlanıyor</div>') + '</details>' for n, l in enumerate(c["lessons"]))
            ps += f'<div data-panel="{c["id"]}" {"" if k==0 else "hidden"}><div class="panel" style="margin-bottom:16px"><h3>{e(c["title"])}</h3><p>{e(c["goal"])} Gerekenler: {e(c["tools"])}.</p></div>{ls}</div>'
        b += sec("Müfredatlar", "Üç yolu da sırayla ya da istediğin dersten başlayarak izleyebilirsin.", f'<div class="tabs" role="tablist" data-tabs>{tb}</div>{ps}')
    head = f'''<div class="wrap"><div class="mhead" style="--a:{m["accent"]}"><a class="crumb" href="../index.html">← Kütüphane</a><h1>{e(m["title"])}</h1><p>{e(m["summary"])}</p><div class="meta">{chips(m)}<span class="chip">{e(m["minutes"])}</span></div></div>{b}</div><div style="height:48px"></div>'''
    return page(f'{m["title"]} · 4D Learning', head, 1, m["tagline"])

def booklet(x):
    vid = f'<div class="video"><iframe src="https://www.youtube-nocookie.com/embed/{x["youtube"]}" title="{e(x["title"])}" loading="lazy" allowfullscreen></iframe></div>' if x["youtube"] else '<div class="vslot">Deney videosu hazırlanıyor</div>'
    li = lambda a: "".join(f"<li>{e(i)}</li>" for i in a)
    body = f'''<div class="toolbar"><a class="crumb" href="../m/sense-of-science.html">← Sense of Science</a><button class="btn p" id="print">Yazdır / PDF</button></div>
<article class="book"><div style="font-size:3rem" aria-hidden="true">{x["emoji"]}</div><h1>{e(x["title"])}</h1><p style="color:var(--muted)">Süre: {x["minutes"]} dakika · FRC 6429 Sense of Science</p>
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

def w(path, txt):
    p = S / path; p.parent.mkdir(parents=True, exist_ok=True); p.write_text(txt, encoding="utf-8")
w("index.html", index()); w("anlasma.html", agreement())
for m in MODS: w(f'm/{m["id"]}.html', module(m))
for x in EXPS: w(f'deney/{x["id"]}.html', booklet(x))
w("robots.txt", "User-agent: *\nAllow: /\n")
print("ok:", len(list(S.rglob("*.html"))), "sayfa")
