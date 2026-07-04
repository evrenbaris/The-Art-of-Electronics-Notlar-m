Vin = 28
Vout = 5
Iout = 0.15
theta_ja = 60
Ta = 70

P = (Vin - Vout) * Iout
Tj = Ta + P * theta_ja

print(f"Power loss = {P:.2f} W")
print(f"Junction temperature = {Tj:.1f} °C")
