#!/usr/bin/env python3
"""Deney ve ders metinlerinden Türkçe sesli anlatım videoları üretir (PIL + espeak-ng + ffmpeg).
Gerçek çekim videolarının yerini tutmaz; çekim videosu eklenene kadar adım adım anlatım sağlar."""
import json, pathlib, subprocess, tempfile, wave, sys
from PIL import Image, ImageDraw, ImageFont
R = pathlib.Path(__file__).resolve().parent.parent; C = R / "content"; V = R / "site/assets/video"
FB = "/usr/share/fonts/google-noto/NotoSans-Bold.ttf"
FR = "/usr/share/fonts/google-noto/NotoSans-Regular.ttf"
W, H = 1280, 720; RED = (30, 91, 140); INK = (11, 42, 67); PAPER = (255, 255, 255); MUTED = (95, 113, 134)
logo = Image.open(R / "site/assets/img/4d-logo.png").convert("RGBA").resize((64, 62))
def wrap(d, text, font, maxw):
    lines, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= maxw: cur = t
        else: lines.append(cur); cur = w
    return lines + ([cur] if cur else [])
def frame(path, kicker, head, body_lines, accent=RED, dark=False):
    bg = INK if dark else PAPER; fg = (255, 255, 255) if dark else INK
    im = Image.new("RGB", (W, H), bg); d = ImageDraw.Draw(im)
    d.rectangle([0, 0, 14, H], fill=accent); im.paste(logo, (W - 110, 36), logo)
    d.text((80, 70), kicker, font=ImageFont.truetype(FR, 28), fill=accent)
    f1 = ImageFont.truetype(FB, 54); y = 130
    for l in wrap(d, head, f1, W - 240)[:3]: d.text((80, y), l, font=f1, fill=fg); y += 66
    y += 24; f2 = ImageFont.truetype(FR, 34)
    for b in body_lines:
        ls = wrap(d, b, f2, W - 220)
        for k, l in enumerate(ls): d.text((110 if k == 0 else 110, y), l, font=f2, fill=fg if not dark else (210, 214, 222)); y += 46
        d.rectangle([80, y - len(ls) * 46 + 16, 92, y - len(ls) * 46 + 28], fill=accent); y += 12
    d.text((80, H - 60), "4D Learning · FRC 6429 4th Dimension", font=ImageFont.truetype(FR, 22), fill=MUTED if not dark else (150, 155, 165))
    im.save(path, quality=90)
VOICE = ["tr"]
def tts(text, wav):
    subprocess.run(["espeak-ng", "-v", VOICE[0], "-s", "135", "-p", "45", "-w", str(wav), text], check=True)
    with wave.open(str(wav)) as w: return w.getnframes() / w.getframerate()
def make(out, title, scenes, kicker):
    out.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as td:
        td = pathlib.Path(td); segs = []
        for i, (head, lines, say, dark) in enumerate(scenes):
            png, wav, mp4 = td / f"{i}.png", td / f"{i}.wav", td / f"{i}.mp4"
            frame(png, kicker if i else "Sesli anlatım videosu", head, lines, dark=dark)
            dur = tts(say, wav) + 0.7
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-framerate", "10", "-i", str(png), "-i", str(wav), "-t", f"{dur:.2f}",
                            "-af", "apad", "-c:v", "libx264", "-preset", "veryfast", "-crf", "30", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "64k", "-ar", "22050", "-ac", "1", "-shortest", str(mp4)], check=True)
            segs.append(mp4)
            if i == 0: Image.open(png).convert("RGB").resize((640, 360)).save(out.with_suffix(".jpg"), quality=80)
        lst = td / "l.txt"; lst.write_text("".join(f"file '{s}'\n" for s in segs))
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", "-movflags", "+faststart", str(out)], check=True)
def exp_scenes(x):
    m = x["materials"]
    sc = [(x["title"], [f"Süre: {x['minutes']} dakika", "Bir yetişkinle birlikte yapalım."], f"{x['title']} deneyi. Süre {x['minutes']} dakika. Bir yetişkinle birlikte yapalım.", True),
          ("Malzemeler", m, "Önce malzemeleri hazırlayalım. " + ". ".join(m), False)]
    sc += [(f"{n}. adım", [s], f"{n}. adım. {s}", False) for n, s in enumerate(x["steps"], 1)]
    sc += [("Neden oldu?", [x["why"]], x["why"], False), ("Güvenlik", [x["safety"], "Deneyi bir yetişkinle yap."], x["safety"] + " Deneyi bir yetişkinle yap.", True)]
    return sc
def ard_scenes(a):
    code = [l for l in a["code"].split("\n") if l.strip()][:9]
    sc = [(f"Experiment {a['id']:02d}: {a['title']}", [a["summary"], f"{a['level']} · {a['time']}"], f"Experiment {a['id']}. {a['title']}. {a['summary']}", True),
          ("Materials", a["materials"], "Materials. " + ". ".join(a["materials"]), False),
          ("Wiring", a["wiring"], "Wiring. " + " ".join(a["wiring"]), False),
          ("Code", code, "Upload the code shown here. The full code is on the lesson page.", True),
          ("What should happen", [a["result"]], "What should happen. " + a["result"], False),
          ("Challenge", [a["challenge"]], "Challenge. " + a["challenge"], True)]
    return sc
def les_scenes(c, l):
    sc = [(l["t"], [l["d"], c["tools"]], f"{l['t']}. {l['d']}", True)]
    sc += [(f"{n}. adım", [s], f"{n}. adım. {s}", False) for n, s in enumerate(l["steps"], 1)]
    sc += [("Görev", [l["task"]], "Şimdi sıra sende. Görev: " + l["task"], True)]
    return sc
def set_scenes(x):
    sc = [(x["title"], [x["kind"], x["time"]], f"{x['title']}. {x['intro']}", True), ("Gerekenler", x["tools"], "Gerekenler. " + ". ".join(x["tools"]), False), ("Parçalar", x["parts"], "Parça listesi. " + ". ".join(x["parts"]), False)]
    sc += [(f"{n}. {h}", [t], f"{n}. adım. {h}. {t}", False) for n, (h, t) in enumerate(x["steps"], 1)]
    return sc
def lego_scenes(g):
    sc = [("LEGO MR yapım kılavuzu", ["SPIKE Prime ile MR cihazı"], "LEGO M R yapım kılavuzu. Spike Prime ile M R cihazı modeli, altı aşamada.", True)]
    sc += [(p["h"], [p["p"]], p["h"] + ". " + p["p"], False) for p in g["phases"]]
    sc += [("Bitince kontrol et", g["tests"], "Bitince kontrol et. " + ". ".join(g["tests"]), True)]
    return sc
if __name__ == "__main__":
    only = sys.argv[1:] 
    for x in json.load(open(C / "experiments.json")):
        o = V / "deney" / f"{x['id']}.mp4"
        if not o.exists() and (not only or x["id"] in only): make(o, x["title"], exp_scenes(x), "Sense of Science · " + x["title"]); print("deney", x["id"], flush=True)
    for x in json.load(open(C / "sets.json")):
        o = V / "set" / f"{x['id']}.mp4"
        if not o.exists() and (not only or x["id"] in only): make(o, x["title"], set_scenes(x), x["title"]); print("set", x["id"], flush=True)
    o = V / "lego-mr.mp4"
    if not o.exists() and (not only or "lego-mr" in only): make(o, "LEGO MR", lego_scenes(json.load(open(C / "lego-mr-guide.json"))), "LEGO MR"); print("lego", flush=True)
    VOICE[0] = "en-us"
    for a in json.load(open(C / "arduino.json")):
        o = V / "elektronik" / f"{a['id']:02d}.mp4"
        if not o.exists() and (not only or "elektronik" in only): make(o, a["title"], ard_scenes(a), "Arduino · " + a["title"]); print("ard", a["id"], flush=True)
    VOICE[0] = "tr"
    for c in json.load(open(C / "courses.json")):
        for n, l in enumerate(c["lessons"], 1):
            o = V / "ders" / f"{c['id']}-{n:02d}.mp4"
            if not o.exists() and (not only or c["id"] in only): make(o, l["t"], les_scenes(c, l), c["title"]); print("ders", c["id"], n, flush=True)
