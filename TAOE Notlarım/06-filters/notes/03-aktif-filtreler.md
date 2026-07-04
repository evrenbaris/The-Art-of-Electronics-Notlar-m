# Aktif Filtreler

## 1. Amaç

Op-amp ile kazanç ve filtreleme birlikte yapılır; GBW ve op-amp limiti unutulmaz.

Bu notun hedefi, konuyu ezber bilgi olarak değil, şematik okuma ve donanım tasarımı kararına dönüşecek şekilde anlamaktır.

## 2. Sezgisel açıklama

Bir devre elemanını veya bloğu değerlendirirken önce şu soruyu sor: **Bu blok hangi fiziksel büyüklüğü kontrol ediyor ve hangi büyüklükten etkileniyor?**

Bu konu için pratik sezgi:

- Giriş ve çıkış büyüklüklerini açıkça ayır.
- Akımın hangi yoldan döndüğünü belirle.
- Enerjinin nerede depolandığını veya harcandığını bul.
- Gerçek komponentin ideal modelden hangi yönde sapacağını yaz.

## 3. Temel bağıntılar

- `Sallen-Key`
- `MFB`

Formülü kullanırken birim kontrolü yap. Sonuç yalnız sayı değil; akım, gerilim, güç, frekans, sıcaklık veya hata yüzdesi olarak tasarım kararı üretmelidir.

## 4. Devre tasarımcısı gözüyle yorum

Bu konuyu gerçek tasarımda kullanırken aşağıdaki parametreleri kontrol et:

- Nominal değer
- Minimum/maksimum sınırlar
- Tolerans ve sıcaklık katsayısı
- Güç/ısı zorlanması
- Giriş/çıkış empedansı
- Frekans cevabı veya zaman cevabı
- Arıza modu: açık devre, kısa devre, sızıntı, yanlış bağlantı

## 5. Aviyonik / gömülü / güç elektroniği bağlantısı

- analog ön filtre
- anti-alias

Aviyonik bağlamda bu konu genelde yalnız elektronik performans değil; güvenilirlik, test edilebilirlik, EMC/EMI ve hata izolasyonu ile birlikte değerlendirilir.

## 6. Simülasyon / lab önerisi

1. Önce ideal komponentlerle nominal devreyi kur.
2. Sonra toleranslı değerleri dene.
3. Sıcaklık veya yük değişimi ekle.
4. Çıkışın beklenen limit içinde kalıp kalmadığını tabloya yaz.
5. Simülasyon sonucunu gerçek testte hangi probla ölçeceğini belirt.

Önerilen ölçümler:

- Giriş gerilimi/akımı
- Çıkış gerilimi/akımı
- Güç kaybı
- Zaman cevabı veya frekans cevabı
- Hata yüzdesi

## 7. Sık yapılan hatalar

- [ ] Nominal değere bakıp tolerans/sıcaklık etkisini unutmak.
- [ ] Devrenin yüklenme etkisini hesaba katmamak.
- [ ] Simülasyondaki ideal elemanı gerçek komponent sanmak.
- [ ] Güç ve ısı hesabını en sona bırakmak.
- [ ] Return current yolunu şematikte ve layoutta düşünmemek.

## 8. Mini problemler

1. Bu konuyu kullanan basit bir devre çiz ve giriş/çıkış değişkenlerini etiketle.
2. Nominal değeri hesapla; sonra ±1%, ±5% veya sıcaklık etkisiyle tekrar hesapla.
3. Bir komponentin açık devre veya kısa devre arıza modunda sistem ne yapar?
4. Bu devreyi aviyonik bir alt sistemde kullanacaksan ICD'ye hangi parametreleri yazarsın?

## 9. Kısa kontrol soruları

- Bu devre hangi durumda kararsız veya hatalı olur?
- Ölçüm cihazı bağlandığında sonucu değiştirir mi?
- Layout parazitikleri sonucu etkiler mi?
- Bu blok için test noktası gerekir mi?

## 10. Terimler

| English | Türkçe | Not |
|---|---|---|
| Aktif | Aktif | Konu içinde tanımlanacak |
| Filtreler | Filtreler | Konu içinde tanımlanacak |
