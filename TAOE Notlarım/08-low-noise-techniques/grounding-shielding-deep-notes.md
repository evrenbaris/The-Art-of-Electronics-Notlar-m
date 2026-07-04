# Grounding ve Shielding — Derin Not

## 1. Ground sembolü gerçek bir fiziksel nokta değildir

Şematikte aynı GND sembolünü koymak, layoutta ve kabloda her noktanın aynı potansiyelde olduğu anlamına gelmez. Her iletkenin direnç, endüktans ve kapasitansı vardır.

## 2. Ana soru: Akım nereden dönüyor?

Her sinyal için bir ileri yol ve dönüş yolu vardır. Dönüş yolu belirsizse EMI, crosstalk ve ölçüm hatası başlar.

## 3. Ground loop

Ground loop, iki nokta arasında birden fazla dönüş yolu oluştuğunda ve bu döngüden istenmeyen akım aktığında oluşur. Özellikle düşük seviye analog ölçümlerde ve uzun kablolarda önemlidir.

## 4. Shield bağlantısı

Shield bağlantı kararı frekans, güvenlik, EMC ve sistem mimarisine bağlıdır.

Yaklaşımlar:

- Tek uçtan shield: düşük frekans ground loop riskini azaltır.
- Çift uçtan shield: yüksek frekans ekranlama için daha iyi olabilir.
- Kapasitif bağlantı: DC loop'u kesip HF dönüş yolu sağlayabilir.
- 360° connector termination: yüksek frekans EMC için etkilidir.

## 5. Aviyonik tasarım refleksi

Grounding mimarisi “sonradan layoutta halledilir” konusu değildir. Sistem gereksinimlerinde, ICD'de, harness tasarımında, şase bağlantısında ve test planında yer almalıdır.
