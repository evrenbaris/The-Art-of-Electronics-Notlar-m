# 04 - Voltage Divider / Gerilim Bölücü

## 1. Bu konu ne anlatıyor?

Gerilim bölücü, giriş geriliminin belirli bir oranını çıkışa veren en temel devre parçalarından biridir.

## 2. Sezgisel açıklama

İki direnç seri bağlanır. Çıkış alt direnç üzerinden alınır. Gerilim, direnç oranlarına göre bölünür.

## 3. Temel formül

```text
Vout = Vin × R2 / (R1 + R2)
```

## 4. Devre tasarımcısı gözüyle yorum

Gerilim bölücü yalnızca “voltaj düşürme” değildir. Aynı zamanda:

- ADC giriş ölçekleme
- Referans gerilim üretme
- Bias noktası oluşturma
- Sensör okuma
- Logic threshold oluşturma

için kullanılır.

Ama kritik nokta şudur:

> Gerilim bölücü çıkışına yük bağlandığında oran değişir.

Bu yüzden yük etkisi mutlaka hesaplanmalıdır.

## 5. Aviyonik / gömülü / güç elektroniği bağlantısı

- 28 V hattı ADC ile ölçülecekse gerilim bölücü kullanılır.
- 34 V transient varsa ADC giriş koruması ayrıca düşünülür.
- Bölücü akımı çok düşük seçilirse gürültüye hassasiyet artar.
- Bölücü akımı çok yüksek seçilirse güç tüketimi artar.
- Alt direnç üzerine paralel ADC giriş empedansı gelirse ölçüm hatası oluşur.

## 6. LTspice simülasyonu

Örnek:

```text
Vin = 28 V
R1 = 100 kΩ
R2 = 20 kΩ
```

Beklenen:

```text
Vout = 28 × 20 / 120 = 4.67 V
```

Sonra çıkışa 100 kΩ yük bağla ve Vout değişimini gözlemle.

## 7. Sık yapılan hatalar

- ADC giriş empedansını sonsuz sanmak
- Koruma diyotlarının kaçağını ihmal etmek
- Direnç toleransını hesaba katmamak
- Güç tüketimini gözden kaçırmak
- Yük bağlıyken gerilim bölücüyü tekrar hesaplamamak

## 8. Mini problemler

1. 28 V'u 3.3 V ADC aralığına indirmek için oran ne olmalıdır?
2. R1 = 100 kΩ, R2 = 10 kΩ ise 28 V girişte Vout kaçtır?
3. R2'ye paralel 10 kΩ yük gelirse Vout nasıl değişir?
4. Gerilim bölücüde dirençleri 10 kat artırmanın avantajı ve dezavantajı nedir?

## 9. Türkçe-İngilizce kavramlar

| English | Türkçe |
|---|---|
| Voltage divider | Gerilim bölücü |
| Load effect | Yük etkisi |
| Input impedance | Giriş empedansı |
| Divider current | Bölücü akımı |
