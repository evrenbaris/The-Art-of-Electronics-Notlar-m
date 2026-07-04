# 03 — FET ve MOSFET / Field-Effect Transistors

## Bölüm amacı

Bu klasör, **Field-Effect Transistors** konularını Türkçe ve tasarım odaklı şekilde çalışmak için hazırlanmıştır. İçerik birebir çeviri değil; devre sezgisi, uygulama, hata modu ve aviyonik/gömülü bağlantı odaklı özgün nottur.

## Konu dosyaları

- [FET Temelleri](notes/01-fet-temelleri.md)
- [JFET Akım Kaynağı](notes/02-jfet-akim-kaynagi.md)
- [FET Yükselteçler](notes/03-fet-yukseltecler.md)
- [FET Analog Anahtarlar](notes/04-fet-analog-anahtarlar.md)
- [Power MOSFET Anahtar](notes/05-power-mosfet-anahtar.md)
- [Gate Drive](notes/06-gate-drive.md)
- [Lineer MOSFET Kullanımı](notes/07-lineer-mosfet-kullanimi.md)
- [MOSFET Hataları](notes/08-mosfet-hatalari.md)

## Bu bölümde kazanılacak refleks

- Devrenin yalnız nominal çalışmasını değil, sınır koşullarını düşünmek.
- Formülü birim ve fiziksel anlamıyla yorumlamak.
- Komponent datasheet parametrelerini devre davranışına bağlamak.
- Simülasyonu gerçek testin ön hazırlığı olarak kullanmak.

## İlk kurulacak devreler / analizler

- FET Temelleri: FET gate gerilimiyle kanal iletkenliğini kontrol eder; giriş akımı çok küçüktür.
- JFET Akım Kaynağı: JFET basit ve düşük gürültülü akım sınırlama/bias elemanı olabilir.
- FET Yükselteçler: Yüksek giriş empedansı ve düşük input current gereken yerlerde FET ön kat mantıklıdır.
- FET Analog Anahtarlar: Ron, charge injection, leakage ve capacitance gerçek performansı belirler.
- Power MOSFET Anahtar: MOSFET anahtarlamada gate charge, Rds(on), SOA ve ısı birlikte düşünülür.

## Aviyonik ve donanım tasarım bağlantıları

- 28 V load switch
- ADC mux
- EMI kontrolü
- MOSFET driver seçimi
- analog anahtar
- e-fuse
- fotodiyot/JFET preamp
- güç kartı koruma
- hot-swap
- inrush control
- low-noise bias
- low-side/high-side sürme

## Bölüm bitirme kriteri

- [ ] Her konu için kendi cümlelerinle 5 dakikalık sözlü anlatım yapıldı.
- [ ] En az bir simülasyon çalıştırıldı.
- [ ] En az üç mini problem çözüldü.
- [ ] Konunun aviyonik/donanım uygulaması yazıldı.
- [ ] Sık hatalar listesine kendi gözlemin eklendi.
