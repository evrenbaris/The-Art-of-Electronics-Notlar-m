# Aviyonik Donanım Bağlantı Haritası

Bu repo genel elektronik devre tasarımını aviyonik sistem bakışıyla bağlamak için kullanılır.

## Güç mimarisi

İlgili bölümler:

- 01 Foundations: güç, direnç, kapasitör, endüktör
- 03 MOSFET: anahtarlama, soft-start, inrush
- 09 Power: regülasyon, DC/DC, koruma, power tree
- 08 Low Noise: güç gürültüsü, grounding, shielding

Sorular:

- 28 V hattın nominal, minimum, maksimum ve transient sınırları nedir?
- Hangi alt sistem izole güç ister?
- Inrush akımı kim sınırlar?
- Return akımı şaseden mi, dedicated return hattından mı döner?

## Haberleşme

İlgili bölümler:

- 10 Digital Logic
- 12 Logic Interfacing
- 14 Data Links
- 15 Microcontrollers

Sorular:

- Hat single-ended mı differential mı?
- Terminasyon nerede?
- Bias/failsafe var mı?
- İzolasyon gereksinimi hangi hata modundan geliyor?
- Common-mode aralığı yeterli mi?

## Analog ölçüm

İlgili bölümler:

- 04 Op-Amps
- 05 Precision
- 08 Low Noise
- 13 ADC/DAC

Sorular:

- Ölçülen büyüklük kaç V / kaç A / kaç Hz?
- Hata bütçesi nedir?
- ADC referansı nereden geliyor?
- Anti-alias filtre var mı?
- Op-amp output ADC sampling anında settle oluyor mu?
