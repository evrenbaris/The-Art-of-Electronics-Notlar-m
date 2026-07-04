# 06 — Filtreler / Filters

## Bölüm amacı

Bu klasör, **Filters** konularını Türkçe ve tasarım odaklı şekilde çalışmak için hazırlanmıştır. İçerik birebir çeviri değil; devre sezgisi, uygulama, hata modu ve aviyonik/gömülü bağlantı odaklı özgün nottur.

## Konu dosyaları

- [Filtre Temelleri](notes/01-filtre-temelleri.md)
- [Pasif RC/LC Filtreler](notes/02-pasif-rc-lc-filtreler.md)
- [Aktif Filtreler](notes/03-aktif-filtreler.md)
- [Butterworth, Bessel, Chebyshev](notes/04-butterworth-bessel-chebyshev.md)
- [Notch ve All-Pass](notes/05-notch-ve-all-pass.md)
- [Dijital Filtreleme](notes/06-dijital-filtreleme.md)

## Bu bölümde kazanılacak refleks

- Devrenin yalnız nominal çalışmasını değil, sınır koşullarını düşünmek.
- Formülü birim ve fiziksel anlamıyla yorumlamak.
- Komponent datasheet parametrelerini devre davranışına bağlamak.
- Simülasyonu gerçek testin ön hazırlığı olarak kullanmak.

## İlk kurulacak devreler / analizler

- Filtre Temelleri: Filtre, frekans alanında sinyal seçiciliği sağlar; zaman alanında gecikme ve overshoot getirir.
- Pasif RC/LC Filtreler: RC basit ve kayıplı; LC daha seçici ama parazitik ve rezonans hassasiyetlidir.
- Aktif Filtreler: Op-amp ile kazanç ve filtreleme birlikte yapılır; GBW ve op-amp limiti unutulmaz.
- Butterworth, Bessel, Chebyshev: Düz genlik, iyi zaman cevabı veya keskin geçiş arasında tercih yapılır.
- Notch ve All-Pass: Belirli bir bozucuyu bastırmak veya fazı ayarlamak için özel filtreler kullanılır.

## Aviyonik ve donanım tasarım bağlantıları

- EMI filtresi
- IMU/GNSS veri işleme
- PLL faz düzeltme
- RF hatları
- analog ön filtre
- anti-alias
- güç giriş filtresi
- haberleşme alıcı ön ucu
- kontrol sinyali
- motor harmonik bastırma
- sensör bant sınırlama
- telemetri filtreleme

## Bölüm bitirme kriteri

- [ ] Her konu için kendi cümlelerinle 5 dakikalık sözlü anlatım yapıldı.
- [ ] En az bir simülasyon çalıştırıldı.
- [ ] En az üç mini problem çözüldü.
- [ ] Konunun aviyonik/donanım uygulaması yazıldı.
- [ ] Sık hatalar listesine kendi gözlemin eklendi.
