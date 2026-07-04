# 05 - Thevenin Eşdeğeri

## 1. Bu konu ne anlatıyor?

Thevenin eşdeğeri, karmaşık bir lineer devreyi tek bir ideal gerilim kaynağı ve seri direnç ile temsil etmeyi sağlar.

## 2. Sezgisel açıklama

Bir devrenin çıkışından bakıldığında, o devre çoğu zaman şöyle düşünülebilir:

```text
İdeal gerilim kaynağı + seri iç direnç
```

Bu model özellikle yük bağlandığında çıkış geriliminin neden düştüğünü anlamak için çok kullanışlıdır.

## 3. Temel formüller

```text
Vth = Açık devre çıkış gerilimi
Rth = Vth / Isc
```

Gerilim bölücü için:

```text
Vth = Vin × R2 / (R1 + R2)
Rth = R1 || R2
```

## 4. Devre tasarımcısı gözüyle yorum

Thevenin eşdeğeri, “bu çıkış ne kadar sağlam/stiff?” sorusunu yanıtlar.

Rth küçükse:

- Kaynak güçlüdür.
- Yük bağlanınca gerilim az değişir.

Rth büyükse:

- Kaynak zayıftır.
- Yük bağlanınca gerilim ciddi düşebilir.

## 5. Aviyonik / gömülü / güç elektroniği bağlantısı

- ADC ölçüm noktası kaynak empedansı
- Sensör çıkışının yüklenmesi
- Op-amp girişine sürülen sinyalin zayıflaması
- Referans gerilim kaynaklarının yük altında davranışı
- Kablo/hat iç direnci
- Güç dağıtımında kaynak empedansı

## 6. LTspice simülasyonu

Öneri:

1. 10 kΩ - 10 kΩ gerilim bölücü kur.
2. Vin = 30 V ver.
3. Açık devre Vout ölç.
4. Çıkışa 10 kΩ yük bağla.
5. Vout'un düştüğünü gör.
6. Aynı sonucu Thevenin modeli ile doğrula.

## 7. Sık yapılan hatalar

- Gerilim bölücüyü ideal gerilim kaynağı sanmak
- Yük etkisini ihmal etmek
- Ölçü aletinin giriş empedansını hesaba katmamak
- Kaynak empedansı ile hat empedansını karıştırmak

## 8. Mini problemler

1. 30 V, R1 = R2 = 10 kΩ bölücü için Vth ve Rth nedir?
2. Bu çıkışa 10 kΩ yük bağlanırsa Vout kaç olur?
3. Rth'nin küçük olması neden iyidir?
4. Ölçü aleti 10 MΩ ise 10 kΩ kaynak empedansında ölçüm hatası önemli midir?

## 9. Türkçe-İngilizce kavramlar

| English | Türkçe |
|---|---|
| Thevenin equivalent | Thevenin eşdeğeri |
| Open-circuit voltage | Açık devre gerilimi |
| Short-circuit current | Kısa devre akımı |
| Source resistance | Kaynak direnci |
| Loading | Yükleme |
