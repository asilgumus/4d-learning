# 4D Learning

FRC 6429 4th Dimension'ın açık eğitim kütüphanesi (Türkçe). Statik site, derleme bağımlılığı yok.

- İçerik: `content/*.json` (modüller, deneyler, müfredat, set/MR/NeuroBridge verileri, sunumlar)
- Üret: `python3 build.py` → `site/`
- Yayın: Vercel (`vercel.json`, çıktı klasörü `site`)

## Dosya ekleme (boş yuvalar)
- Üretim modeli (hidrolik kol, elevatör): kitapçık PDF'leri `docs/uretim/kitapcik/`, SolidWorks ZIP'leri `docs/uretim/cizim/`, sayfa görselleri `img/uretim/`; metinler `content/sets.json`. Giriş sunumu slaytları `assets/slides/uretim-tr|en/` (PDF'ten üretildi).
- LEGO MR talimatı: `site/assets/docs/lego-mr/yapim-talimati.pdf`, yolu `builds.json > lego-mr > booklet`.
- Deney / ders videoları: YouTube ID'sini `experiments.json` (`youtube`) veya `courses.json` (`yt`) içine yaz.
- Siber güvenlik slaytları `site/assets/slides/cybersecurity/` (PDF'ten üretildi).

Sonra `python3 build.py`.
