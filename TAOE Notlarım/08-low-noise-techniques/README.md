# 08 — Düşük Gürültü Teknikleri / Low-Noise Techniques

## Bölüm amacı

Bu klasör, **Low-Noise Techniques** konularını Türkçe ve tasarım odaklı şekilde çalışmak için hazırlanmıştır. İçerik birebir çeviri değil; devre sezgisi, uygulama, hata modu ve aviyonik/gömülü bağlantı odaklı özgün nottur.

## Konu dosyaları

- [Gürültü Türleri](notes/01-gurultu-turleri.md)
- [SNR ve Noise Figure](notes/02-snr-ve-noise-figure.md)
- [BJT Gürültüsü](notes/03-bjt-gurultusu.md)
- [JFET/FET Gürültüsü](notes/04-jfet-fet-gurultusu.md)
- [Op-Amp Gürültü Hesabı](notes/05-op-amp-gurultu-hesabi.md)
- [Transimpedance Amplifier](notes/06-transimpedance-amplifier.md)
- [Shielding ve Grounding](notes/07-shielding-ve-grounding.md)
- [Gürültü Ölçümü](notes/08-gurultu-olcumu.md)

## Bu bölümde kazanılacak refleks

- Devrenin yalnız nominal çalışmasını değil, sınır koşullarını düşünmek.
- Formülü birim ve fiziksel anlamıyla yorumlamak.
- Komponent datasheet parametrelerini devre davranışına bağlamak.
- Simülasyonu gerçek testin ön hazırlığı olarak kullanmak.

## İlk kurulacak devreler / analizler

- Gürültü Türleri: Johnson, shot, flicker ve çevresel girişim farklı kaynaklara sahiptir.
- SNR ve Noise Figure: Sinyal zincirinde ilk katın gürültüsü genelde tüm sistemi belirler.
- BJT Gürültüsü: Kaynak empedansına göre BJT düşük voltage noise avantajı sağlayabilir.
- JFET/FET Gürültüsü: Yüksek kaynak empedansında düşük input current nedeniyle FET avantajlıdır.
- Op-Amp Gürültü Hesabı: Datasheet en/in değerlerini bant genişliği ve kaynak empedansıyla birlikte hesapla.

## Aviyonik ve donanım tasarım bağlantıları

- ADC ön kat
- IR sensor
- RF alıcı zinciri
- aviyonik kablolama
- fotodiyot
- hassas alıcı
- instrumentation amp
- mikrofon/sensör preamp
- optik algılama
- osiloskop prob seçimi
- sensör ön uç
- telemetri hassasiyeti

## Bölüm bitirme kriteri

- [ ] Her konu için kendi cümlelerinle 5 dakikalık sözlü anlatım yapıldı.
- [ ] En az bir simülasyon çalıştırıldı.
- [ ] En az üç mini problem çözüldü.
- [ ] Konunun aviyonik/donanım uygulaması yazıldı.
- [ ] Sık hatalar listesine kendi gözlemin eklendi.
