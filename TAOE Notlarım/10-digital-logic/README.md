# 10 — Dijital Mantık / Digital Logic

## Bölüm amacı

Bu klasör, **Digital Logic** konularını Türkçe ve tasarım odaklı şekilde çalışmak için hazırlanmıştır. İçerik birebir çeviri değil; devre sezgisi, uygulama, hata modu ve aviyonik/gömülü bağlantı odaklı özgün nottur.

## Konu dosyaları

- [Logic Seviyeleri](notes/01-logic-seviyeleri.md)
- [Kombinasyonel Mantık](notes/02-kombinasyonel-mantik.md)
- [Sequential Logic](notes/03-sequential-logic.md)
- [Senkronizer ve Metastability](notes/04-senkronizer-ve-metastability.md)
- [Sayaçlar ve Timing](notes/05-sayaclar-ve-timing.md)
- [CMOS Güç Tüketimi](notes/06-cmos-guc-tuketimi.md)
- [Logic Patolojileri](notes/07-logic-patolojileri.md)

## Bu bölümde kazanılacak refleks

- Devrenin yalnız nominal çalışmasını değil, sınır koşullarını düşünmek.
- Formülü birim ve fiziksel anlamıyla yorumlamak.
- Komponent datasheet parametrelerini devre davranışına bağlamak.
- Simülasyonu gerçek testin ön hazırlığı olarak kullanmak.

## İlk kurulacak devreler / analizler

- Logic Seviyeleri: HIGH/LOW aralıkları aileye göre değişir; eşik, noise margin ve besleme uyumu önemlidir.
- Kombinasyonel Mantık: Çıkış yalnız mevcut girişlere bağlıdır; sadeleştirme donanım maliyetini düşürür.
- Sequential Logic: Flip-flop ve register ile zaman ve bellek devreye girer.
- Senkronizer ve Metastability: Asenkron sinyal clock domain içine alınırken metastability riski yönetilir.
- Sayaçlar ve Timing: Dijital zamanlama sayaç, clock ve reset ile hassas ve tekrarlanabilir yapılır.

## Aviyonik ve donanım tasarım bağlantıları

- 3.3V/5V uyumluluk
- EMI dayanım
- PBIT zamanlayıcı
- arming logic
- discrete giriş
- enable gating
- güvenli discrete okuma
- harici discrete
- interlock logic
- interrupt input
- low-power mode
- pulse generation

## Bölüm bitirme kriteri

- [ ] Her konu için kendi cümlelerinle 5 dakikalık sözlü anlatım yapıldı.
- [ ] En az bir simülasyon çalıştırıldı.
- [ ] En az üç mini problem çözüldü.
- [ ] Konunun aviyonik/donanım uygulaması yazıldı.
- [ ] Sık hatalar listesine kendi gözlemin eklendi.
