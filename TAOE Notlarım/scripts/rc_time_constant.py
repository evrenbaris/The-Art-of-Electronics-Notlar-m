import math

R = 10_000      # ohm
C = 100e-9      # farad
tau = R * C

print(f"tau = {tau:.6f} s")
for n in [1, 2, 3, 4, 5]:
    charge = 1 - math.exp(-n)
    discharge = math.exp(-n)
    print(f"{n} tau: charge={charge*100:.2f}% discharge={discharge*100:.2f}%")
