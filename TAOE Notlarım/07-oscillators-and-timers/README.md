# 07 — Osilatörler ve Zamanlayıcılar / Oscillators and Timers

## Bölüm amacı

Bu klasör, **Oscillators and Timers** konularını Türkçe ve tasarım odaklı şekilde çalışmak için hazırlanmıştır. İçerik birebir çeviri değil; devre sezgisi, uygulama, hata modu ve aviyonik/gömülü bağlantı odaklı özgün nottur.

## Konu dosyaları

- [Osilasyon Koşulu](notes/01-osilasyon-kosulu.md)
- [Relaxation Oscillator](notes/02-relaxation-oscillator.md)
- [555 ve Monostable](notes/03-555-ve-monostable.md)
- [Sinüs Osilatörleri](notes/04-sinus-osilatorleri.md)
- [Kristal Osilatörler](notes/05-kristal-osilatorler.md)
- [PLL ve DDS](notes/06-pll-ve-dds.md)

## Bu bölümde kazanılacak refleks

- Devrenin yalnız nominal çalışmasını değil, sınır koşullarını düşünmek.
- Formülü birim ve fiziksel anlamıyla yorumlamak.
- Komponent datasheet parametrelerini devre davranışına bağlamak.
- Simülasyonu gerçek testin ön hazırlığı olarak kullanmak.

## İlk kurulacak devreler / analizler

- Osilasyon Koşulu: Osilatör, döngü kazancı ve fazı uygun olduğunda kendi kendine sinyal üretir.
- Relaxation Oscillator: Kapasitör şarj/deşarj ve eşik karşılaştırma ile kare/üçgen dalga üretir.
- 555 ve Monostable: Klasik 555 pratik olsa da hassasiyet, besleme gürültüsü ve sıcaklık sınırları dikkate alınır.
- Sinüs Osilatörleri: Düşük distorsiyonlu sinüs için genlik kontrolü ve seçici ağ gerekir.
- Kristal Osilatörler: Kristal düşük jitter ve iyi frekans kararlılığı sağlar; yük kapasitansı önemlidir.

## Aviyonik ve donanım tasarım bağlantıları

- GNSS/RF referans
- LO üretimi
- MCU clock
- RF alt sistem test
- analog test source
- basit zamanlama
- clock üretimi
- datalink/radar saatleri
- low-cost timer
- test fixture
- test sinyali
- watchdog pulse

## Bölüm bitirme kriteri

- [ ] Her konu için kendi cümlelerinle 5 dakikalık sözlü anlatım yapıldı.
- [ ] En az bir simülasyon çalıştırıldı.
- [ ] En az üç mini problem çözüldü.
- [ ] Konunun aviyonik/donanım uygulaması yazıldı.
- [ ] Sık hatalar listesine kendi gözlemin eklendi.
