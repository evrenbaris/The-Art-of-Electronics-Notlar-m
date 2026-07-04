# 13 — Dijital Analog ile Buluşur / Digital Meets Analog

## Bölüm amacı

Bu klasör, **Digital Meets Analog** konularını Türkçe ve tasarım odaklı şekilde çalışmak için hazırlanmıştır. İçerik birebir çeviri değil; devre sezgisi, uygulama, hata modu ve aviyonik/gömülü bağlantı odaklı özgün nottur.

## Konu dosyaları

- [DAC Temelleri](notes/01-dac-temelleri.md)
- [R-2R ve Current Steering DAC](notes/02-r-2r-ve-current-steering-dac.md)
- [PWM ile DAC](notes/03-pwm-ile-dac.md)
- [ADC Temelleri](notes/04-adc-temelleri.md)
- [Örnekleme ve Aliasing](notes/05-ornekleme-ve-aliasing.md)
- [SAR ADC](notes/06-sar-adc.md)
- [Delta-Sigma ADC](notes/07-delta-sigma-adc.md)
- [ADC Sürme Devresi](notes/08-adc-surme-devresi.md)
- [PLL Temelleri](notes/09-pll-temelleri.md)
- [PRBS ve Dijital Gürültü](notes/10-prbs-ve-dijital-gurultu.md)

## Bu bölümde kazanılacak refleks

- Devrenin yalnız nominal çalışmasını değil, sınır koşullarını düşünmek.
- Formülü birim ve fiziksel anlamıyla yorumlamak.
- Komponent datasheet parametrelerini devre davranışına bağlamak.
- Simülasyonu gerçek testin ön hazırlığı olarak kullanmak.

## İlk kurulacak devreler / analizler

- DAC Temelleri: Dijital kod analog seviyeye çevrilirken çözünürlük, doğruluk ve çıkış yapısı önemlidir.
- R-2R ve Current Steering DAC: Farklı DAC mimarileri hız, doğruluk ve glitch açısından farklıdır.
- PWM ile DAC: PWM düşük maliyetlidir ama ripple ve gecikme için filtre gerekir.
- ADC Temelleri: ADC analog sinyali örnekler; çözünürlük, referans ve giriş sürme kritik olur.
- Örnekleme ve Aliasing: Nyquist üstündeki bileşenler yanlış frekans olarak görünür; anti-alias filtre gerekir.

## Aviyonik ve donanım tasarım bağlantıları

- ADC front-end
- BIST pattern
- IMU/sensör veri toplama
- MCU analog output
- MUX sonrası buffer
- PMU ADC
- RF synthesizer
- akım/gerilim izleme
- clock recovery
- data acquisition board
- haberleşme link testi
- hassas yavaş ölçüm

## Bölüm bitirme kriteri

- [ ] Her konu için kendi cümlelerinle 5 dakikalık sözlü anlatım yapıldı.
- [ ] En az bir simülasyon çalıştırıldı.
- [ ] En az üç mini problem çözüldü.
- [ ] Konunun aviyonik/donanım uygulaması yazıldı.
- [ ] Sık hatalar listesine kendi gözlemin eklendi.
