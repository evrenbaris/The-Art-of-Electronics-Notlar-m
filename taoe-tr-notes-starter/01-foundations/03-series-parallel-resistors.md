# 03 - Seri ve Paralel Dirençler

## 1. Bu konu ne anlatıyor?

Dirençlerin seri ve paralel bağlandığında eşdeğer dirençlerinin nasıl hesaplanacağını anlatır.

## 2. Sezgisel açıklama

Seri dirençte akım aynıdır, gerilim bölünür.  
Paralel dirençte gerilim aynıdır, akım bölünür.

## 3. Temel formüller

Seri:

```text
R_eq = R1 + R2 + R3 + ...
```

Paralel:

```text
1/R_eq = 1/R1 + 1/R2 + 1/R3 + ...
```

İki direnç için:

```text
R_eq = (R1 × R2) / (R1 + R2)
```

## 4. Devre tasarımcısı gözüyle yorum

Seri direnç değer artırmak için, paralel direnç değer düşürmek için kullanılır.

Pratik sezgi:

- Büyük direnç + küçük direnç seri ise toplam yaklaşık büyük dirençtir.
- Büyük direnç || küçük direnç paralel ise toplam yaklaşık küçük dirençtir.
- Eşit iki direnç paralel ise değer yarıya iner.

## 5. Aviyonik / gömülü / güç elektroniği bağlantısı

- ADC giriş gerilim bölücülerinde seri dirençler
- Terminasyon ağlarında paralel eşdeğerler
- Pull-up/pull-down ağları
- Bias dirençleri
- TVS kaçak akımıyla paralel etkiler

## 6. LTspice simülasyonu

Öneri:

```text
R1 = 10 kΩ
R2 = 10 kΩ
```

Seri ve paralel iki devre kur.

Beklenen:

```text
Seri: 20 kΩ
Paralel: 5 kΩ
```

## 7. Sık yapılan hatalar

- Paralel direnç sonucunun en küçük dirençten daha küçük olduğunu unutmak
- Seri dirençte güç paylaşımını hesaplamamak
- Eşdeğer direnç hesabını yük bağlıyken tekrar yapmamak

## 8. Mini problemler

1. 5 kΩ ve 10 kΩ seri kaç kΩ eder?
2. 5 kΩ ve 10 kΩ paralel kaç kΩ eder?
3. 120 Ω terminasyon üzerine 120 Ω paralel gelirse eşdeğer kaç Ω olur?
4. 10 kΩ || 1 MΩ yaklaşık kaç kΩ olur?

## 9. Türkçe-İngilizce kavramlar

| English | Türkçe |
|---|---|
| Series | Seri |
| Parallel | Paralel |
| Equivalent resistance | Eşdeğer direnç |
| Conductance | İletkenlik |
