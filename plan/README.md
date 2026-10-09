# Kütlə Planı · Bolonya

Fərdi qidalanma və məşq planı: kişi, 58,3 kq, 1,65 m, Bolonyada yaşayır. Məqsəd təmiz əzələ kütləsidir.

## Fayllar

| Fayl | Nə üçün |
|---|---|
| `index.html` | Veb tətbiq: gündəlik kalori izləmə, analiz, menyu, məşq proqramı (GIF-lər `../videos/`-dan gəlir) |
| `qidalanma-plani.xlsx` | Eyni plan Excel-də: gündəlik, avtomatik norma, həftəlik analiz |
| `src/` | Generator: `data.py` (məhsullar, menyu, məşq), `template.html`, `build.py` |

## Əsas rəqəmlər

| | |
|---|---|
| BMR (Mifflin–St Jeor) | 1 514 kkal |
| Məşqsiz gündəlik xərc (×1,4) | 2 120 kkal |
| İstirahət günü norması (+300) | **2 420 kkal** |
| Zal günü norması (+250) | **2 670 kkal** |
| Tennis, 60 dəq tək / cüt | +408 / +292 kkal |
| Protein (2 q/kq) | ≥ 117 q |
| Yağ / karbohidrat | 67–74 q / 337–384 q |
| Hədəf | həftədə +0,2–0,3 kq |

Gündə 5 yemək (08:00 · 11:00 · 13:30 · 17:00 · 20:30). Məşq saatı dəyişəndə yemək saatları da dəyişir, `index.html` → Menyu bölməsinə bax.

Zal: full-body A/B, həftədə 3 dəfə (B.e. · Çərş. · Cümə). İlk məşq 9 oktyabr 2026, Cümə: A.

## İstifadə

1. `index.html`-i brauzerdə aç (və ya claude.ai-dakı artifact versiyasını). Hər yeməyi çək, “Bu gün” bölməsində məhsulu və qramı yaz.
2. Zal günü “Zal günü”nü, tennis oynayanda “Tennis”i aç və dəqiqəni yaz: norma avtomatik dəyişir.
3. Səhər çəkisini həftədə ən azı 4 dəfə yaz. “Analiz” 2 həftədən sonra normanı ±150 kkal dəyişməyi təklif edəcək.

## Yenidən qurmaq

```bash
python3 plan/src/build.py
```

Qida dəyərləri CREA, USDA və İtaliya etiketlərinə əsaslanan orta rəqəmlərdir. Qiymətlər təxminidir. Bu plan tibbi məsləhət deyil.
