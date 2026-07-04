# 02 - Ohm Kanunu ve Güç

## 1. Bu konu ne anlatıyor?

Ohm Kanunu, direnç üzerindeki gerilim ile dirençten akan akım arasındaki ilişkiyi verir. Güç hesabı ise devrede enerjinin nerede harcandığını gösterir.

## 2. Sezgisel açıklama

Bir direnç üzerine gerilim uygularsan, dirençten akım akar. Direnç değeri büyüdükçe aynı gerilimde daha az akım akar.

Güç hesabı tasarımda çok kritiktir çünkü komponentin yanıp yanmayacağını belirler.

## 3. Temel formüller

```text
V = I × R
P = V × I
P = I² × R
P = V² / R
```

## 4. Devre tasarımcısı gözüyle yorum

Bir direnç seçerken yalnızca ohm değerine bakılmaz. Güç değeri de kontrol edilir.

Örneğin 28 V hatta 1 kΩ direnç:

```text
I = 28 / 1000 = 28 mA
P = 28 × 28 mA = 0.784 W
```

Bu durumda 1/4 W direnç yanabilir. En az 1 W, tercihen margin ile daha yüksek güçte direnç gerekir.

## 5. Aviyonik / gömülü / güç elektroniği bağlantısı

- 28 V nominal, 34 V transient, load dump gibi durumlarda direnç gücü tekrar hesaplanmalıdır.
- Discrete hatlarda pull-up/pull-down güçleri ihmal edilmemelidir.
- Akım algılama dirençlerinde hem güç hem tolerans önemlidir.
- Güç hattındaki bleeder dirençleri termal olarak kontrol edilmelidir.

## 6. LTspice simülasyonu

Önerilen simülasyon:

```text
V1 = 28 V
R1 = 1 kΩ
```

Ölç:

- R1 akımı
- R1 üzerindeki güç
- 1/4 W ile karşılaştır

## 7. Sık yapılan hatalar

- Direncin yalnızca ohm değerine bakmak
- Transient durumda gücü tekrar hesaplamamak
- 0603/0402 küçük paket dirençlerde güç limitini ihmal etmek
- Sürekli güç ile pulse güç dayanımını karıştırmak

## 8. Mini problemler

1. 34 V üzerinde 4.7 kΩ direnç kaç mW harcar?
2. 28 V üzerinde 10 kΩ direnç kaç mA çeker?
3. 0.1 Ω shunt üzerinden 3 A geçerse kaç W harcar?
4. 1 A nominal akım ölçümü için 50 mV düşüm istenirse shunt kaç Ω olur?

## 9. Türkçe-İngilizce kavramlar

| English | Türkçe |
|---|---|
| Ohm's law | Ohm Kanunu |
| Power dissipation | Güç harcaması |
| Rating | Anma değeri |
| Derating | Güvenlik payıyla düşürme |
| Shunt resistor | Akım algılama direnci |
