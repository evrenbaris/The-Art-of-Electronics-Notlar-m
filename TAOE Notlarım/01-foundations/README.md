# 01 — Temeller / Foundations

## Bölüm amacı

Bu klasör, **Foundations** konularını Türkçe ve tasarım odaklı şekilde çalışmak için hazırlanmıştır. İçerik birebir çeviri değil; devre sezgisi, uygulama, hata modu ve aviyonik/gömülü bağlantı odaklı özgün nottur.

## Konu dosyaları

- [Gerilim, Akım ve Direnç](notes/01-gerilim-akim-ve-direnc.md)
- [Ohm Kanunu ve Güç](notes/02-ohm-kanunu-ve-guc.md)
- [Seri ve Paralel Dirençler](notes/03-seri-ve-paralel-direncler.md)
- [Gerilim Bölücü](notes/04-gerilim-bolucu.md)
- [Thevenin ve Norton Eşdeğerleri](notes/05-thevenin-ve-norton-esdegerleri.md)
- [Sinyaller, Genlik ve dB](notes/06-sinyaller-genlik-ve-db.md)
- [Kapasitörler ve RC Devreler](notes/07-kapasitorler-ve-rc-devreler.md)
- [Türevleyici ve İntegratör](notes/08-turevleyici-ve-integrator.md)
- [Endüktörler ve Transformatörler](notes/09-enduktorler-ve-transformatorler.md)
- [Diyotlar ve Doğrultma](notes/10-diyotlar-ve-dogrultma.md)
- [Empedans ve Reaktans](notes/11-empedans-ve-reaktans.md)
- [Pasif Komponent Seçimi](notes/12-pasif-komponent-secimi.md)

## Bu bölümde kazanılacak refleks

- Devrenin yalnız nominal çalışmasını değil, sınır koşullarını düşünmek.
- Formülü birim ve fiziksel anlamıyla yorumlamak.
- Komponent datasheet parametrelerini devre davranışına bağlamak.
- Simülasyonu gerçek testin ön hazırlığı olarak kullanmak.

## İlk kurulacak devreler / analizler

- Gerilim, Akım ve Direnç: Devre dilinin temelini kur: gerilim iki nokta arasında, akım elemanın içinden, direnç ise ilişkiyi belirleyen elemandır.
- Ohm Kanunu ve Güç: Devrede bir elemanın elektriksel zorlanmasını yalnız gerilimle değil, akım ve güçle birlikte değerlendir.
- Seri ve Paralel Dirençler: Eşdeğer direnç hesabını sezgisel yap; büyük-küçük direnç yaklaşımını kullan.
- Gerilim Bölücü: Bölücü çıkışı ancak yük akımı ihmal edilebiliyorsa beklenen değeri verir.
- Thevenin ve Norton Eşdeğerleri: Karmaşık kaynak-direnç ağını tek kaynak + tek direnç gibi düşünerek yükleme etkisini gör.

## Aviyonik ve donanım tasarım bağlantıları

- 28 V hatlarda akım/güç hesabı
- ADC giriş ölçekleme
- DC/DC dönüştürücüler
- EMI kuplaj yolu
- PWM filtreleme
- RF/EMI seviye yorumlama
- SNR bütçesi
- TVS seçimi
- TVS ve seri direnç güç hesabı
- aviyonik derating
- batarya/güç hattı izleme
- bias ağı

## Bölüm bitirme kriteri

- [ ] Her konu için kendi cümlelerinle 5 dakikalık sözlü anlatım yapıldı.
- [ ] En az bir simülasyon çalıştırıldı.
- [ ] En az üç mini problem çözüldü.
- [ ] Konunun aviyonik/donanım uygulaması yazıldı.
- [ ] Sık hatalar listesine kendi gözlemin eklendi.
