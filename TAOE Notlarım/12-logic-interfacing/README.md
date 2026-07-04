# 12 — Logic Arayüzleme / Logic Interfacing

## Bölüm amacı

Bu klasör, **Logic Interfacing** konularını Türkçe ve tasarım odaklı şekilde çalışmak için hazırlanmıştır. İçerik birebir çeviri değil; devre sezgisi, uygulama, hata modu ve aviyonik/gömülü bağlantı odaklı özgün nottur.

## Konu dosyaları

- [Logic Family Arayüzleme](notes/01-logic-family-arayuzleme.md)
- [Giriş Koruma](notes/02-giris-koruma.md)
- [Comparator Kullanımı](notes/03-comparator-kullanimi.md)
- [Harici Yük Sürme](notes/04-harici-yuk-surme.md)
- [Optokuplör ve İzolasyon](notes/05-optokuplor-ve-izolasyon.md)
- [Fiber Optik Linkler](notes/06-fiber-optik-linkler.md)
- [Uzun Kablolar](notes/07-uzun-kablolar.md)
- [RS-232 / RS-485](notes/08-rs-232-rs-485.md)
- [Kablo Sürme Kontrol Listesi](notes/09-kablo-surme-kontrol-listesi.md)

## Bu bölümde kazanılacak refleks

- Devrenin yalnız nominal çalışmasını değil, sınır koşullarını düşünmek.
- Formülü birim ve fiziksel anlamıyla yorumlamak.
- Komponent datasheet parametrelerini devre davranışına bağlamak.
- Simülasyonu gerçek testin ön hazırlığı olarak kullanmak.

## İlk kurulacak devreler / analizler

- Logic Family Arayüzleme: Farklı logic aileleri gerilim, eşik ve akım uyumluluğu açısından kontrol edilir.
- Giriş Koruma: Harici hatlar ESD, transient, ters bağlantı ve overvoltage için korunur.
- Comparator Kullanımı: Comparator analog girişten dijital karar üretir; hysteresis ve output tipi önemlidir.
- Harici Yük Sürme: Logic pin doğrudan yük sürmek için değil, sürücü devreyi kontrol etmek için kullanılır.
- Optokuplör ve İzolasyon: İzolasyon ground loop ve güvenlik için kullanılır; hız ve CTR sınırlıdır.

## Aviyonik ve donanım tasarım bağlantıları

- 3.3V MCU
- 5V tolerant input
- EMC test hazırlığı
- EMI yoğun ortam
- KTS/IMU linkleri
- Sistem seviyesinde ICD
- alt sistem haberleşme
- aviyonik connector input
- discrete giriş
- fault isolation
- ground reference
- harness tasarım

## Bölüm bitirme kriteri

- [ ] Her konu için kendi cümlelerinle 5 dakikalık sözlü anlatım yapıldı.
- [ ] En az bir simülasyon çalıştırıldı.
- [ ] En az üç mini problem çözüldü.
- [ ] Konunun aviyonik/donanım uygulaması yazıldı.
- [ ] Sık hatalar listesine kendi gözlemin eklendi.
