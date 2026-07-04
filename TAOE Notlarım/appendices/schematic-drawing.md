# Şematik Çizim Kuralları

## Genel prensip

Şematik yalnız bağlantı listesi değildir; devrenin çalışma fikrini anlatan mühendislik dokümanıdır.

## Kurallar

- Sinyal akışı soldan sağa, güç yukarıdan aşağıya okunabilir olmalı.
- Her IC pininin besleme ve ground bağlantısı net görünmeli.
- Connector pinleri fonksiyon ve yön bilgisiyle etiketlenmeli.
- Analog, dijital, güç ve şase referansları bilinçli isimlendirilmeli.
- Test noktaları kritik sinyaller için eklenmeli.
- Kullanılmayan girişler floating bırakılmamalı.

## Kötü kokular

- Her yerde aynı GND sembolü ama dönüş akımı belirsiz.
- Uzun net isimleri yerine anlamsız kısa isimler.
- Koruma elemanları connector'dan uzakta.
- Decoupling kapasitörleri şematikte yok veya değeri belirsiz.
