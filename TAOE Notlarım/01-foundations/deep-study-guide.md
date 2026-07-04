# Chapter 1 Derin Çalışma Rehberi — Foundations

Bu dosya Chapter 1 için ana çalışma omurgasıdır. Notlar özgün anlatımdır; kitabın çevirisi değildir.

## 1. Elektroniğin temel dili

Elektronik devrelerde üç soru sürekli sorulur:

1. Bu noktadaki gerilim nedir?
2. Bu elemandan geçen akım nedir?
3. Bu elemanda harcanan veya depolanan güç/enerji nedir?

Gerilim her zaman iki nokta arasındadır. Akım her zaman bir yol üzerinden akar. Güç ise enerji dönüşümünü gösterir. Bu üçlü doğru kurulmadan hiçbir devre güvenilir yorumlanamaz.

## 2. Direnç yalnız akım sınırlamaz

Direnç pratikte şu rollere girer:

- Gerilim bölücü
- Pull-up / pull-down
- Terminasyon
- Bias ağı
- Akım ölçüm shunt'ı
- RC zaman sabiti elemanı
- Damping elemanı
- Güç harcayan yük

Tasarım refleksi: Bir direnç gördüğünde sadece değerine bakma; üzerinden geçen akımı, üzerinde düşen gerilimi ve harcadığı gücü kontrol et.

## 3. Voltage divider'ın gerçek sınırı

İdeal gerilim bölücü yalnız çıkış yüklenmiyorsa doğru sonuç verir. Çıkışa bir yük bağlanınca alt direnç ile paralel olur ve oran değişir.

Tasarım kuralı:

```text
Rload en az 10x, tercihen 100x daha büyük olmalı
```

Bu kural özellikle ADC ile batarya/güç hattı ölçerken önemlidir. ADC sample capacitor kısa süreli akım çekebilir; bu yüzden sadece DC bölücü hesabı yetmez.

## 4. Thevenin sezgisi

Thevenin eşdeğeri şunu söyler: Bir devrenin çıkışını, ideal kaynak ve seri iç direnç gibi görebilirsin.

Bu sezgi sana şunu kazandırır:

- Kaynak ne kadar “stiff”?
- Yük bağlanınca çıkış ne kadar düşer?
- Ölçü aleti devreyi etkiler mi?
- Sensör çıkışı buffer ister mi?

## 5. Kapasitör: akıma göre gerilim değiştirir

Kapasitör için ana fikir:

```text
Akım varsa kapasitör gerilimi zamanla değişir.
Gerilim ani değişemez; bunun için sonsuz akım gerekir.
```

Bu yüzden kapasitörler:

- Besleme bypass yapar.
- Reset delay üretir.
- Low-pass/high-pass filtre oluşturur.
- Enerji depolar.
- İnput coupling ile DC seviyeyi bloklar.

## 6. Endüktör: gerilime göre akım değiştirir

Endüktör için ana fikir:

```text
Gerilim varsa endüktör akımı zamanla değişir.
Akım ani değişemez; bunun için sonsuz gerilim gerekir.
```

Bu yüzden endüktörler:

- DC/DC converter içinde enerji depolar.
- Common-mode choke olarak EMI bastırır.
- Flyback gerilimi üretir.
- Kablo ve layout paraziti olarak istemeden ortaya çıkar.

## 7. Diyot: akım yolu tasarlama elemanı

Diyot sadece “tek yönde akım geçirir” diye düşünülmemeli. Asıl tasarım sorusu şudur:

```text
Normalde ve arızada akım nereye akacak?
```

Diyot kullanım yerleri:

- Ters polarite koruma
- Flyback clamp
- Rectifier
- OR-ing
- TVS transient koruma
- Logic clamp

## 8. Empedans ve frekans sezgisi

DC'de direnç gibi görünen devre, frekansta bambaşka davranabilir. Kapasitör yüksek frekansta düşük empedans, endüktör yüksek frekansta yüksek empedans gösterir.

Pratik sonuç:

- Bypass capacitor yüksek frekans gürültüsünü toprağa taşır.
- Uzun kablo yüksek hızlı kenarda transmission line olur.
- Ground sembolü her frekansta ideal sıfır empedans değildir.

## 9. Chapter 1'i bitirme testi

Aşağıdakileri kağıda çizip anlat:

1. 28 V → ADC ölçümü için voltage divider.
2. 5 V logic input için pull-up ve switch.
3. 100 nF bypass capacitor'ın akım döngüsü.
4. Röle bobini için flyback diode.
5. RC low-pass ile PWM'den analog gerilim üretme.
6. RS-485 hattında 120 Ω terminasyonun neden gerektiği.

## 10. Kendine sorulacak profesyonel sorular

- Bu devrede akımın dönüş yolu neresi?
- Bu eleman kaç watt harcıyor?
- Bu node yüksek empedans mı, gürültüye açık mı?
- Bu bağlantı hızlı kenarda transmission line olur mu?
- Bu komponent arızalanırsa sistem güvenli kalır mı?
