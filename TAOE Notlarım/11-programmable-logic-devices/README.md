# 11 — Programlanabilir Mantık / Programmable Logic Devices

## Bölüm amacı

Bu klasör, **Programmable Logic Devices** konularını Türkçe ve tasarım odaklı şekilde çalışmak için hazırlanmıştır. İçerik birebir çeviri değil; devre sezgisi, uygulama, hata modu ve aviyonik/gömülü bağlantı odaklı özgün nottur.

## Konu dosyaları

- [PAL/PLA Mantığı](notes/01-pal-pla-mantigi.md)
- [FPGA Temelleri](notes/02-fpga-temelleri.md)
- [HDL ile Donanım Düşünme](notes/03-hdl-ile-donanim-dusunme.md)
- [LFSR ve PRBS](notes/04-lfsr-ve-prbs.md)
- [FPGA Tasarım Tavsiyesi](notes/05-fpga-tasarim-tavsiyesi.md)

## Bu bölümde kazanılacak refleks

- Devrenin yalnız nominal çalışmasını değil, sınır koşullarını düşünmek.
- Formülü birim ve fiziksel anlamıyla yorumlamak.
- Komponent datasheet parametrelerini devre davranışına bağlamak.
- Simülasyonu gerçek testin ön hazırlığı olarak kullanmak.

## İlk kurulacak devreler / analizler

- PAL/PLA Mantığı: Basit programlanabilir mantık sabit glue logic için kullanılabilir.
- FPGA Temelleri: LUT, flip-flop, routing ve block RAM ile paralel donanım davranışı kurulur.
- HDL ile Donanım Düşünme: Verilog/VHDL kodu yazılım değil, sentezlenen donanım tarifidir.
- LFSR ve PRBS: Test, scrambler ve pseudo-random sequence üretimi için küçük donanım bloklarıdır.
- FPGA Tasarım Tavsiyesi: Clocking, reset, CDC ve timing closure FPGA tasarımının ana riskleridir.

## Aviyonik ve donanım tasarım bağlantıları

- BIST
- DO-254 farkındalığı
- aviyonik güvenilirlik
- decode logic
- deterministik mantık
- interface glue
- link test pattern
- protocol bridge
- safety state machine
- yüksek hızlı I/O

## Bölüm bitirme kriteri

- [ ] Her konu için kendi cümlelerinle 5 dakikalık sözlü anlatım yapıldı.
- [ ] En az bir simülasyon çalıştırıldı.
- [ ] En az üç mini problem çözüldü.
- [ ] Konunun aviyonik/donanım uygulaması yazıldı.
- [ ] Sık hatalar listesine kendi gözlemin eklendi.
