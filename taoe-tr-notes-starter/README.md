# The Art of Electronics Türkçe Çalışma Notları

Bu repo, **Paul Horowitz & Winfield Hill - The Art of Electronics, 3rd Edition** kitabını çalışırken oluşturulan **özgün Türkçe çalışma notları**, devre sezgileri, simülasyonlar, örnek çözümler ve elektronik tasarım yorumlarından oluşur.

> Bu repo kitabın birebir çevirisi değildir. Kitaptaki metin, şekil, tablo ve PDF içerikleri bu repoda paylaşılmaz.  
> Amaç: Kitaptan öğrenilen konuları Türkçe, özgün ve uygulanabilir bir elektronik tasarım rehberine dönüştürmektir.

---

## Hedef

Bu çalışmanın amacı üç aşamalıdır:

1. Kitabı sistematik şekilde anlamak.
2. Her konuyu Türkçe ve mühendislik sezgisiyle yeniden anlatmak.
3. LTspice/KiCad/sayısal örneklerle uygulanabilir bir donanım tasarım kütüphanesi oluşturmak.

---

## Çalışma Prensibi

Her konu dosyası şu şablonla yazılır:

```markdown
# Konu Başlığı

## 1. Bu konu ne anlatıyor?

## 2. Sezgisel açıklama

## 3. Temel formüller

## 4. Devre tasarımcısı gözüyle yorum

## 5. Aviyonik / gömülü / güç elektroniği bağlantısı

## 6. LTspice simülasyonu

## 7. Sık yapılan hatalar

## 8. Mini problemler

## 9. Türkçe-İngilizce kavramlar
```

---

## Repo Yapısı

```text
.
├── README.md
├── LEGAL_NOTICE.md
├── CONTRIBUTING.md
├── docs/
│   ├── roadmap.md
│   └── study-method.md
├── 01-foundations/
├── 02-bipolar-transistors/
├── 03-field-effect-transistors/
├── 04-operational-amplifiers/
├── 05-precision-circuits/
├── 06-filters/
├── 07-oscillators-and-timers/
├── 08-low-noise-techniques/
├── 09-power-regulation-conversion/
├── 10-digital-logic/
├── 11-programmable-logic-devices/
├── 12-logic-interfacing/
├── 13-digital-meets-analog/
├── 14-computers-controllers-data-links/
├── 15-microcontrollers/
├── appendices/
├── glossary/
├── ltspice/
├── kicad/
└── images/
```

---

## Öncelikli Çalışma Sırası

### Faz 1 — Temel analog sezgi

- Chapter 1 — Foundations
- Chapter 2 — Bipolar Transistors
- Chapter 3 — Field-Effect Transistors
- Chapter 4 — Operational Amplifiers

### Faz 2 — Gerçek donanım tasarımı

- Chapter 5 — Precision Circuits
- Chapter 8 — Low-Noise Techniques
- Chapter 9 — Voltage Regulation and Power Conversion
- Chapter 12 — Logic Interfacing

### Faz 3 — Aviyonik / gömülü sistem bağlantısı

- Chapter 10 — Digital Logic
- Chapter 13 — Digital Meets Analog
- Chapter 14 — Computers, Controllers, and Data Links
- Chapter 15 — Microcontrollers

### Faz 4 — Derinleşme

- Chapter 6 — Filters
- Chapter 7 — Oscillators and Timers
- Chapter 11 — Programmable Logic Devices

---

## Haftalık Çalışma Döngüsü

| Gün | İş |
|---|---|
| Pazartesi | Kitap bölümünü oku |
| Salı | Kavramları kendi cümlelerinle çıkar |
| Çarşamba | Türkçe notu yaz |
| Perşembe | LTspice/KiCad uygulaması yap |
| Cuma | Aviyonik/donanım tasarım bağlantısını yaz |
| Hafta sonu | GitHub düzenleme, commit, tekrar |

---

## Örnek Commit Mesajları

```bash
git add .
git commit -m "Add voltage current resistance notes"
git commit -m "Add LTspice example for voltage divider"
git commit -m "Add Thevenin equivalent explanation"
git push
```

---

## Telif Notu

Bu repo, ilgili kitabın yerini tutmaz. Kitabı edinmeniz ve konuları orijinal kaynaktan çalışmanız önerilir. Buradaki içerik, kişisel öğrenme sürecinde oluşturulmuş özgün Türkçe mühendislik notlarıdır.
