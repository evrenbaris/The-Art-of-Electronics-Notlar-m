# Donanım Tasarım Gözden Geçirme Checklist

## Güç

- [ ] Giriş gerilim aralığı tanımlı mı?
- [ ] Transient ve ters polarite koruması var mı?
- [ ] Inrush akımı hesaplandı mı?
- [ ] Sigorta/e-fuse/akım limiti koordinasyonu yapıldı mı?
- [ ] Regülatör ısıl hesabı yapıldı mı?
- [ ] Her IC için local decoupling var mı?
- [ ] Power sequencing gereksinimi var mı?

## Analog

- [ ] Op-amp common-mode range uygun mu?
- [ ] Output swing yük altında yeterli mi?
- [ ] Offset ve bias current hata bütçesine girdi mi?
- [ ] ADC giriş settling hesabı yapıldı mı?
- [ ] Anti-alias filtre var mı?
- [ ] Referans gerilimi noise/drift açısından uygun mu?

## Dijital / Haberleşme

- [ ] Logic level uyumu kontrol edildi mi?
- [ ] Floating input kalmadı mı?
- [ ] Reset/boot pinleri doğru bağlandı mı?
- [ ] RS-485/CAN terminasyon doğru yerde mi?
- [ ] Uzun hatlarda ESD/TVS var mı?
- [ ] Ground reference/common-mode sınırı kontrol edildi mi?

## Layout / EMC

- [ ] Yüksek di/dt döngüleri küçük mü?
- [ ] Switching node alanı minimum mu?
- [ ] Analog ve power return yolları bilinçli mi?
- [ ] Shield termination stratejisi belli mi?
- [ ] Connector pin dizilimi return path açısından uygun mu?
