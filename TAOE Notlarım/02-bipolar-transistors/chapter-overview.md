# BJT Transistörler — Bölüm Genel Özeti

Bu bölümün ana fikri: **BJT akım kontrollü gibi başlar, transconductance davranışıyla gerçekçi anlaşılır.**

## Çalışma akışı

1. Önce kavramı sözlü anlat.
2. Devreyi ideal elemanlarla çöz.
3. Gerçek komponent etkilerini ekle.
4. Simülasyonda nominal ve worst-case çalıştır.
5. Sonucu aviyonik/donanım bağlamına taşı.

## Kavram haritası

```mermaid
flowchart LR
    A[Konu] --> B[Sezgisel model]
    B --> C[Formül]
    C --> D[Devre örneği]
    D --> E[Simülasyon]
    E --> F[Tasarım checklist]
    F --> G[Aviyonik uygulama]
```

## Kendini test et

- Bu bölümdeki en önemli tasarım riski ne?
- Hangi parametre sıcaklıkla değişir?
- Hangi parametre toleransla değişir?
- Ölçüm yaparken devreyi yüklüyor musun?
- Layout bu davranışı değiştirir mi?
