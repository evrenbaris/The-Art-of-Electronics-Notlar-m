# 04 — Operasyonel Yükselteçler / Operational Amplifiers

## Bölüm amacı

Bu klasör, **Operational Amplifiers** konularını Türkçe ve tasarım odaklı şekilde çalışmak için hazırlanmıştır. İçerik birebir çeviri değil; devre sezgisi, uygulama, hata modu ve aviyonik/gömülü bağlantı odaklı özgün nottur.

## Konu dosyaları

- [İdeal Op-Amp Kuralları](notes/01-ideal-op-amp-kurallari.md)
- [Inverting ve Non-Inverting](notes/02-inverting-ve-non-inverting.md)
- [Buffer ve Difference Amplifier](notes/03-buffer-ve-difference-amplifier.md)
- [Op-Amp Akım Kaynakları](notes/04-op-amp-akim-kaynaklari.md)
- [Single-Supply Op-Amp](notes/05-single-supply-op-amp.md)
- [Op-Amp Gerçek Davranışı](notes/06-op-amp-gercek-davranisi.md)
- [Kararlılık ve Kompanzasyon](notes/07-kararlilik-ve-kompanzasyon.md)
- [Aktif Doğrultucu ve Peak Detector](notes/08-aktif-dogrultucu-ve-peak-detector.md)
- [Op-Amp Seçim Rehberi](notes/09-op-amp-secim-rehberi.md)

## Bu bölümde kazanılacak refleks

- Devrenin yalnız nominal çalışmasını değil, sınır koşullarını düşünmek.
- Formülü birim ve fiziksel anlamıyla yorumlamak.
- Komponent datasheet parametrelerini devre davranışına bağlamak.
- Simülasyonu gerçek testin ön hazırlığı olarak kullanmak.

## İlk kurulacak devreler / analizler

- İdeal Op-Amp Kuralları: Negatif geri besleme altında girişler eşitlenir ve giriş akımı ihmal edilir; bu bir sonuçtur, varsayım değil.
- Inverting ve Non-Inverting: Kazanç direnç oranıyla belirlenir; giriş empedansı ve faz ihtiyaca göre seçilir.
- Buffer ve Difference Amplifier: Buffer yüklemeyi azaltır; difference amplifier iki sinyal farkını alır ama direnç eşleşmesi ister.
- Op-Amp Akım Kaynakları: Op-amp geri besleme ile direnç üzerindeki gerilimi sabit tutarak hassas akım üretir.
- Single-Supply Op-Amp: Tek beslemede common-mode ve output swing sınırları tasarımın merkezidir.

## Aviyonik ve donanım tasarım bağlantıları

- 3.3V/5V analog ön uç
- ADC sürme
- BOM trade-off
- LED test current
- RTD/bridge excitation
- analog conditioning
- availability
- diferansiyel ölçüm
- ground offset azaltma
- hata bütçesi
- kapasitif yük sürme
- kontrol döngüsü

## Bölüm bitirme kriteri

- [ ] Her konu için kendi cümlelerinle 5 dakikalık sözlü anlatım yapıldı.
- [ ] En az bir simülasyon çalıştırıldı.
- [ ] En az üç mini problem çözüldü.
- [ ] Konunun aviyonik/donanım uygulaması yazıldı.
- [ ] Sık hatalar listesine kendi gözlemin eklendi.
