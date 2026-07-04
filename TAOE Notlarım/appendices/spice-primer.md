# SPICE Primer

## Temel analizler

```text
.op      çalışma noktası
.tran    zaman alanı
.ac      frekans alanı
.dc      DC sweep
.step    parametre sweep
```

## Örnek

```spice
V1 in 0 DC 5
R1 in out 10k
R2 out 0 10k
.op
.end
```

## Uyarılar

- Model yoksa simülasyon sonucu yanıltıcı olabilir.
- ESR/ESL/parazitik eklenmeyen devre fazla ideal görünür.
- Güç elektroniğinde timestep ve başlangıç koşulları önemlidir.
