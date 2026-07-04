# 05 — Hassas Devreler / Precision Circuits

## Bölüm amacı

Bu klasör, **Precision Circuits** konularını Türkçe ve tasarım odaklı şekilde çalışmak için hazırlanmıştır. İçerik birebir çeviri değil; devre sezgisi, uygulama, hata modu ve aviyonik/gömülü bağlantı odaklı özgün nottur.

## Konu dosyaları

- [Hata Bütçesi](notes/01-hata-butcesi.md)
- [Direnç Toleransı ve Drift](notes/02-direnc-toleransi-ve-drift.md)
- [Offset ve Bias Current](notes/03-offset-ve-bias-current.md)
- [CMRR ve PSRR](notes/04-cmrr-ve-psrr.md)
- [Settling, Slew Rate ve Dinamik Hata](notes/05-settling-slew-rate-ve-dinamik-hata.md)
- [Instrumentation Amplifier](notes/06-instrumentation-amplifier.md)
- [Fully Differential Amplifier](notes/07-fully-differential-amplifier.md)
- [Kalibrasyon ve Test](notes/08-kalibrasyon-ve-test.md)

## Bu bölümde kazanılacak refleks

- Devrenin yalnız nominal çalışmasını değil, sınır koşullarını düşünmek.
- Formülü birim ve fiziksel anlamıyla yorumlamak.
- Komponent datasheet parametrelerini devre davranışına bağlamak.
- Simülasyonu gerçek testin ön hazırlığı olarak kullanmak.

## İlk kurulacak devreler / analizler

- Hata Bütçesi: Hassas tasarımda her hata kaynağını ppm, yüzde veya volt cinsinden bütçeye yaz.
- Direnç Toleransı ve Drift: Kazanç doğruluğu çoğu zaman op-amp değil direnç oranı ile sınırlanır.
- Offset ve Bias Current: Küçük sinyallerde giriş offseti ve bias akımı doğrudan ölçüm hatasına dönüşür.
- CMRR ve PSRR: Ortak mod ve besleme değişimleri ölçüme sızabilir; dB değerini gerçek hataya çevir.
- Settling, Slew Rate ve Dinamik Hata: ADC öncesi devre yalnız doğru değere değil, zamanında doğru değere ulaşmalıdır.

## Aviyonik ve donanım tasarım bağlantıları

- ADC ölçüm doğruluğu
- ATP prosedürü
- EMI dayanımı
- SAR ADC sürme
- bridge sensor
- current sense
- current shunt high-side
- güç rail gürültüsü
- kalibrasyon gereksinimi
- kalibrasyon verisi saklama
- mV ölçüm
- multiplexed DAQ

## Bölüm bitirme kriteri

- [ ] Her konu için kendi cümlelerinle 5 dakikalık sözlü anlatım yapıldı.
- [ ] En az bir simülasyon çalıştırıldı.
- [ ] En az üç mini problem çözüldü.
- [ ] Konunun aviyonik/donanım uygulaması yazıldı.
- [ ] Sık hatalar listesine kendi gözlemin eklendi.
