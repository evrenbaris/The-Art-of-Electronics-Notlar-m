# 02 — BJT Transistörler / Bipolar Transistors

## Bölüm amacı

Bu klasör, **Bipolar Transistors** konularını Türkçe ve tasarım odaklı şekilde çalışmak için hazırlanmıştır. İçerik birebir çeviri değil; devre sezgisi, uygulama, hata modu ve aviyonik/gömülü bağlantı odaklı özgün nottur.

## Konu dosyaları

- [BJT modelleri](notes/01-bjt-modelleri.md)
- [Transistör Anahtar](notes/02-transistor-anahtar.md)
- [Emitter Follower](notes/03-emitter-follower.md)
- [BJT Akım Kaynağı](notes/04-bjt-akim-kaynagi.md)
- [Common-Emitter Amplifier](notes/05-common-emitter-amplifier.md)
- [Diferansiyel Çift](notes/06-diferansiyel-cift.md)
- [BJT Devrelerinde Geri Besleme](notes/07-bjt-devrelerinde-geri-besleme.md)
- [BJT Tasarım Hataları](notes/08-bjt-tasarim-hatalari.md)

## Bu bölümde kazanılacak refleks

- Devrenin yalnız nominal çalışmasını değil, sınır koşullarını düşünmek.
- Formülü birim ve fiziksel anlamıyla yorumlamak.
- Komponent datasheet parametrelerini devre davranışına bağlamak.
- Simülasyonu gerçek testin ön hazırlığı olarak kullanmak.

## İlk kurulacak devreler / analizler

- BJT modelleri: BJT akım kontrollü gibi başlar, transconductance davranışıyla gerçekçi anlaşılır.
- Transistör Anahtar: Doyuma sürülen BJT düşük/orta akım anahtarlamada basit ve sağlamdır.
- Emitter Follower: Gerilim kazancı yaklaşık 1, akım kazancı yüksek; tampon olarak kullanılır.
- BJT Akım Kaynağı: Akımı direnç ve referans gerilimle belirleyip yükten bağımsızlaştırır.
- Common-Emitter Amplifier: Gerilim kazancı sağlar ama bias, headroom ve sıcaklık kararlılığı ister.

## Aviyonik ve donanım tasarım bağlantıları

- LED sabit akım
- LED/optokuplör sürme
- analog preamp
- analog sinyal yükseltme
- basit regülatör
- bias akımı
- current mirror
- diferansiyel sensör
- discrete output
- instrumentation zinciri
- kararlı analog yükselteç
- komparator öncesi kazanç

## Bölüm bitirme kriteri

- [ ] Her konu için kendi cümlelerinle 5 dakikalık sözlü anlatım yapıldı.
- [ ] En az bir simülasyon çalıştırıldı.
- [ ] En az üç mini problem çözüldü.
- [ ] Konunun aviyonik/donanım uygulaması yazıldı.
- [ ] Sık hatalar listesine kendi gözlemin eklendi.
