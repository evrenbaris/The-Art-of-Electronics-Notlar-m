# 01 - Voltage, Current and Resistance

## 1. Bu konu ne anlatıyor?

Bu konu, elektronik devrelerdeki en temel üç büyüklüğü anlatır:

- Gerilim / voltaj
- Akım
- Direnç

Bu üç kavram anlaşılmadan devre analizi, güç hesabı, sinyal bütünlüğü, filtreleme, regülatör tasarımı veya haberleşme hattı yorumlamak mümkün değildir.

## 2. Sezgisel açıklama

Voltaj, iki nokta arasındaki potansiyel farktır.  
Akım, bir elemanın içinden geçen yük akışıdır.  
Direnç, voltaj ile akım arasındaki ilişkiyi belirler.

Kritik dil ayrımı:

- Voltaj bir elemanın **üzerinde** veya iki nokta **arasında** oluşur.
- Akım bir elemanın **içinden** akar.

Yanlış ifade:

```text
Direncin içinden voltaj geçer.
```

Doğru ifade:

```text
Direncin üzerinden voltaj düşer.
Direncin içinden akım akar.
```

## 3. Temel formüller

Ohm Kanunu:

```text
V = I × R
I = V / R
R = V / I
```

Güç:

```text
P = V × I
P = I² × R
P = V² / R
```

## 4. Devre tasarımcısı gözüyle yorum

Direnç yalnızca “akımı sınırlayan eleman” değildir. Gerçek tasarımda direnç:

- Akım sınırlar.
- Gerilim böler.
- Pull-up / pull-down görevi görür.
- Terminasyon sağlar.
- Akım ölçümü için shunt olarak kullanılır.
- Bias noktası oluşturur.
- RC filtrelerde zaman sabitini belirler.
- Güç harcayarak enerji sönümler.

## 5. Aviyonik / gömülü / güç elektroniği bağlantısı

Aviyonik donanımda bu konu şuralarda doğrudan karşına çıkar:

- 28 V güç hattında akım limitleme
- Discrete girişlerde pull-up/pull-down seçimi
- RS-485/CAN hatlarında terminasyon
- ADC girişlerinde gerilim bölücü
- High-side switch akım ölçümü
- TVS/ESD koruma elemanlarında güç hesabı
- Inrush current sınırlama
- Ground return akımı yorumlama

## 6. LTspice simülasyonu

Önerilen ilk simülasyon:

```text
12 V kaynak + 1 kΩ direnç
```

Beklenen sonuç:

```text
I = 12 V / 1 kΩ = 12 mA
P = 12 V × 12 mA = 144 mW
```

## 7. Sık yapılan hatalar

- Voltaj ve akım dilini karıştırmak
- Direnç gücünü kontrol etmemek
- 1/4 W dirençle yüksek güç harcatmak
- Pull-up direncini çok küçük seçip gereksiz akım harcamak
- Pull-up direncini çok büyük seçip hattı gürültüye açık bırakmak

## 8. Mini problemler

1. 28 V hatta 10 kΩ direnç bağlanırsa akım kaç mA olur?
2. 5 V hatta 330 Ω LED seri direnci varsa yaklaşık akım ne olur?
3. 1 W güç harcayan 100 Ω dirençten geçen akım kaçtır?
4. 1/4 W direnç üzerinde 10 V düşerse direnç minimum kaç Ω olmalıdır?

## 9. Türkçe-İngilizce kavramlar

| English | Türkçe |
|---|---|
| Voltage | Gerilim / Voltaj |
| Current | Akım |
| Resistance | Direnç |
| Power | Güç |
| Voltage drop | Gerilim düşümü |
| Ground | Toprak / Referans |
