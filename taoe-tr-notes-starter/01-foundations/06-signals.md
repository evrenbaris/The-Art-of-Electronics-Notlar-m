# 06 - Signal Kavramı

## 1. Bu konu ne anlatıyor?

Elektronikte sinyal, zamanla değişen gerilim veya akım bilgisidir. Analog ve dijital sistemlerin çoğu sinyallerin işlenmesi üzerine kuruludur.

## 2. Sezgisel açıklama

DC durumda gerilim sabittir. Sinyalde ise gerilim veya akım zamanla değişir.

Örnek sinyaller:

- Sinüs
- Kare dalga
- Darbe
- Ramp
- Gürültü
- Logic level

## 3. Temel kavramlar

```text
Frekans: f
Periyot: T = 1/f
Açısal frekans: ω = 2πf
```

Sinüs:

```text
V(t) = A × sin(2πft)
```

## 4. Devre tasarımcısı gözüyle yorum

Bir devre DC'de doğru çalışabilir ama AC/sinyal altında bozulabilir.

Bakılması gerekenler:

- Genlik
- Frekans
- Rise time
- Duty cycle
- Noise
- Ground reference
- Ölçüm probunun etkisi

## 5. Aviyonik / gömülü / güç elektroniği bağlantısı

- RS-485 diferansiyel sinyaller
- Discrete pulse komutları
- PWM motor/aktuator sürüşü
- ADC örnekleme sinyalleri
- Clock hatları
- EMI kaynaklı gürültüler
- Güç hattı ripple/noise

## 6. LTspice simülasyonu

Öneri:

- Sinüs kaynağı
- Pulse kaynağı
- Kare dalga
- RC filtre ile dalga şeklinin değişimi

## 7. Sık yapılan hatalar

- Kare dalganın yalnızca “0-1” olmadığını, yüksek frekans bileşenleri taşıdığını unutmak
- Rise time hızlıysa iletim hattı etkilerini ihmal etmek
- Osiloskop ground klipsiyle kısa devre oluşturmak
- RMS, peak ve peak-to-peak değerleri karıştırmak

## 8. Mini problemler

1. 1 kHz sinyalin periyodu nedir?
2. 10 MHz clock sinyalinde periyot kaç ns'dir?
3. 5 Vpp sinüsün peak değeri kaç V'tur?
4. 3.3 V logic sinyalinde ideal LOW ve HIGH seviyeleri nedir?

## 9. Türkçe-İngilizce kavramlar

| English | Türkçe |
|---|---|
| Signal | Sinyal |
| Frequency | Frekans |
| Period | Periyot |
| Amplitude | Genlik |
| RMS | Etkin değer |
| Rise time | Yükselme süresi |
| Duty cycle | Görev oranı |
| Noise | Gürültü |
