# Katkı Kuralları

Katkıların amacı kitabı kopyalamak değil, elektronik devre tasarım bilgisini Türkçe ve uygulanabilir hale getirmektir.

## Not yazarken

Her dosyada şu akışı koru:

1. Konu ne işe yarar?
2. Sezgisel açıklama
3. Temel bağıntılar
4. Devre tasarımcısı gözüyle yorum
5. Aviyonik/gömülü/güç elektroniği bağlantısı
6. Simülasyon/lab önerisi
7. Sık hata listesi
8. Mini problemler
9. İngilizce-Türkçe terimler

## Commit mesajları

Örnek:

```bash
git commit -m "Add RC time constant notes"
git commit -m "Add LTspice netlist for diode rectifier"
git commit -m "Improve RS-485 termination checklist"
```

## Kalite kontrol

- Formüllerde birim kontrolü yap.
- Her devre için varsayımları yaz.
- “Nominal çalışıyor” demeden önce worst-case düşün.
- Kullanılan komponentin datasheet parametrelerini not et.
- Güç, ısı ve tolerans kontrollerini unutma.
