# TAOE Türkçe Notlar — Elektronik Devre Tasarımı Çalışma Reposu

Bu repo, **The Art of Electronics** kitabını sistematik şekilde çalışırken oluşturulan **özgün Türkçe mühendislik notları**, devre sezgileri, kontrol listeleri, LTspice örnekleri, mini problemler ve aviyonik/donanım tasarım bağlantılarından oluşur.

> Bu repo kitabın birebir çevirisi değildir. Kitaptaki metinler, sayfa görüntüleri, tablolar, şekiller ve PDF içerikleri bu repoya eklenmemelidir. Buradaki içerik, konuları kendi cümlelerimizle anlamak ve uygulanabilir elektronik tasarım rehberine dönüştürmek için hazırlanmıştır.

## Neden bu repo?

Amaç yalnızca kitabı okumak değil; devre tasarımcısı gibi düşünmeyi öğrenmek:

- Şematikte akımın nereden aktığını ve nereden döndüğünü görmek.
- Komponenti yalnız nominal değeriyle değil, tolerans, güç, sıcaklık, parazitik ve arıza modu ile değerlendirmek.
- Analog, dijital, güç ve haberleşme bloklarını aynı sistem içinde yorumlayabilmek.
- Aviyonik donanım tasarımında gerekli olan grounding, shielding, power tree, interface ve test bakışını güçlendirmek.

## Nasıl çalışılır?

Her konu için sabit döngü:

1. İlgili kitap bölümünü oku.
2. Bu repodaki özgün Türkçe notu oku.
3. Formülleri ezberlemek yerine devre davranışını sözlü anlat.
4. LTspice örneğini çalıştır veya kendin tekrar kur.
5. Mini problemleri çöz.
6. Konuyu kendi aviyonik/donanım örneğinle bağla.
7. Anladığını kendi cümlelerinle güncelle ve commit at.

## Klasörler

```text
.
├── 01-foundations/                  # Temel devre kavramları
├── 02-bipolar-transistors/           # BJT devreleri
├── 03-field-effect-transistors/      # JFET/MOSFET
├── 04-operational-amplifiers/        # Op-amp devreleri
├── 05-precision-circuits/            # Hata bütçesi ve hassas ölçüm
├── 06-filters/                       # Pasif/aktif/dijital filtreler
├── 07-oscillators-and-timers/        # Osilatör ve zamanlayıcılar
├── 08-low-noise-techniques/          # Gürültü, shielding, grounding
├── 09-power-regulation-conversion/   # Regülatörler ve güç dönüşümü
├── 10-digital-logic/                 # Dijital mantık
├── 11-programmable-logic-devices/    # PLD/FPGA temelleri
├── 12-logic-interfacing/             # Logic arayüzleme ve kablo sürme
├── 13-digital-meets-analog/          # ADC/DAC/PLL
├── 14-computers-controllers-data-links/ # Veri yolları ve bilgisayar mimarisi
├── 15-microcontrollers/              # Mikrodenetleyiciler
├── appendices/                       # Ek notlar
├── docs/                             # Yol haritası, yöntem, kontrol listeleri
├── glossary/                         # Sözlük, semboller, formüller
├── ltspice/                          # SPICE netlist örnekleri
├── kicad/                            # KiCad çalışma alanı
├── scripts/                          # Hesap ve çizim yardımcıları
└── templates/                        # Not/lab/simülasyon şablonları
```

## Öncelikli sıra

Aviyonik donanım/sistem mühendisliği odağı için önerilen sıra:

1. **01 → 04:** Temel analog sezgi.
2. **09 → 12 → 08 → 05:** Güç, arayüz, grounding/gürültü, hassasiyet.
3. **10 → 13 → 14 → 15:** Dijital, ADC/DAC, veri yolları, MCU.
4. **06 → 07 → 11:** Filtre, clock/timing, FPGA/PLD derinleşmesi.

## Günlük minimum çalışma

- 30 dakika okuma.
- 20 dakika not çıkarma.
- 20 dakika devre/simülasyon.
- 10 dakika “tasarımcı gözüyle risk nedir?” sorusu.

## Telif ve etik

Bu repo bir çeviri projesi değil, özgün öğrenme notları projesidir. Kitabın telifli içeriğini repoya koyma. Kendi çizdiğin devreleri, kendi açıklamalarını, kendi simülasyonlarını ve kendi problemlerini ekle.
