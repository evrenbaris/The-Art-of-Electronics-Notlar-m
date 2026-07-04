# 15 — Mikrodenetleyiciler / Microcontrollers

## Bölüm amacı

Bu klasör, **Microcontrollers** konularını Türkçe ve tasarım odaklı şekilde çalışmak için hazırlanmıştır. İçerik birebir çeviri değil; devre sezgisi, uygulama, hata modu ve aviyonik/gömülü bağlantı odaklı özgün nottur.

## Konu dosyaları

- [MCU Seçimi](notes/01-mcu-secimi.md)
- [GPIO ve Timer](notes/02-gpio-ve-timer.md)
- [MCU ADC/DAC Periferikleri](notes/03-mcu-adc-dac-periferikleri.md)
- [UART/SPI/I2C/CAN](notes/04-uart-spi-i2c-can.md)
- [Gerçek Zamanlı Firmware](notes/05-gercek-zamanli-firmware.md)
- [Bring-up ve Debug](notes/06-bring-up-ve-debug.md)
- [MCU Donanım Kontrol Listesi](notes/07-mcu-donanim-kontrol-listesi.md)

## Bu bölümde kazanılacak refleks

- Devrenin yalnız nominal çalışmasını değil, sınır koşullarını düşünmek.
- Formülü birim ve fiziksel anlamıyla yorumlamak.
- Komponent datasheet parametrelerini devre davranışına bağlamak.
- Simülasyonu gerçek testin ön hazırlığı olarak kullanmak.

## İlk kurulacak devreler / analizler

- MCU Seçimi: MCU seçimi çekirdekten çok periferik, güvenilirlik, toolchain ve yaşam döngüsü kararıdır.
- GPIO ve Timer: Gerçek zamanlı kontrol timer/capture/compare/PWM bloklarıyla yapılır.
- MCU ADC/DAC Periferikleri: MCU iç ADC kullanışlıdır ama referans, sampling ve giriş empedansı limitlidir.
- UART/SPI/I2C/CAN: Haberleşme periferikleri protokolü kolaylaştırır; hata durumları firmware tasarımına girer.
- Gerçek Zamanlı Firmware: Loop, interrupt ve RTOS tasarımı deterministik zaman gereksinimlerine göre seçilir.

## Aviyonik ve donanım tasarım bağlantıları

- 2 ms polling
- ATP hazırlığı
- PBIT/CIT
- PMU controller
- RS-485 half-duplex
- aviyonik kontrol kartı
- discrete timing
- fault isolation
- health monitoring
- low-cost sensing
- sensor bus
- servo command

## Bölüm bitirme kriteri

- [ ] Her konu için kendi cümlelerinle 5 dakikalık sözlü anlatım yapıldı.
- [ ] En az bir simülasyon çalıştırıldı.
- [ ] En az üç mini problem çözüldü.
- [ ] Konunun aviyonik/donanım uygulaması yazıldı.
- [ ] Sık hatalar listesine kendi gözlemin eklendi.
