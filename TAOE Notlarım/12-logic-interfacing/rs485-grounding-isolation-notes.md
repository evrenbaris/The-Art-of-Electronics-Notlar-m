# RS-485, Grounding ve İzolasyon — Çalışma Notu

## 1. RS-485 neyi çözer?

RS-485 diferansiyel haberleşme sağlar. Bu, gürültü bağışıklığını artırır; fakat sonsuz bağışıklık anlamına gelmez. Alıcı hâlâ common-mode sınırları içinde kalmalıdır.

## 2. Temel bağlantı soruları

- A/B hattı twisted pair mi?
- Hat sonunda 120 Ω terminasyon var mı?
- Bus idle durumunda failsafe bias var mı?
- Shield tek uçtan mı, çift uçtan mı, kapasitif mi bağlanacak?
- İzole transceiver gerekiyorsa izolasyon bariyerinin iki tarafında güç de izole mi?
- Common reference için üçüncü iletken gerekiyor mu?

## 3. İzolasyon kararı

İzolasyon şu durumlarda güçlenir:

- Alt sistemler farklı ground potansiyelinde çalışıyorsa
- Uzun harness ve yüksek common-mode gürültü varsa
- Arıza izolasyonu sistem gereksinimiyse
- Ground loop riski yüksekse

Ama izolasyon bedava değildir:

- İzole güç gerekir.
- Bariyer kapasitansı common-mode akımı geçirir.
- CMTI ve creepage/clearance kontrol edilir.
- Test ve hata teşhisi karmaşıklaşır.

## 4. Minimum checklist

- [ ] Termination sadece uçlarda.
- [ ] Stub uzunluğu kısa.
- [ ] Bias dirençleri toplam yükü bozmayacak değerde.
- [ ] TVS common-mode range'i bozmayacak şekilde seçildi.
- [ ] Shield akımı sinyal return yerine geçmiyor.
- [ ] İzolasyon varsa iki tarafın referansları yanlışlıkla kısa devre edilmedi.
