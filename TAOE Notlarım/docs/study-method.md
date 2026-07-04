# Çalışma Metodu

## 1. Pasif okuma yapma

Her konudan sonra şu üç soruyu cevapla:

1. Bu devre hangi fiziksel etkiyi kullanıyor?
2. Hangi varsayım bozulursa devre çalışmaz?
3. Gerçek komponent idealden hangi yönde sapar?

## 2. Her formülü bir devreyle bağla

Örneğin `τ = RC` sadece matematik değildir. Reset delay, low-pass filter, debounce, ADC input settling ve inrush davranışında karşına çıkar.

## 3. Her konuda bir aviyonik örnek yaz

Örnekler:

- 28 V giriş filtresi
- RS-485 terminasyon ve failsafe bias
- ADC ile güç hattı ölçümü
- MOSFET high-side load switch
- Op-amp ile akım algılama
- Ground loop ve shield termination

## 4. Haftalık çıktı

Her hafta en az:

- 3 markdown notu
- 1 LTspice simülasyonu
- 1 mini problem çözümü
- 1 tasarım kontrol listesi güncellemesi
