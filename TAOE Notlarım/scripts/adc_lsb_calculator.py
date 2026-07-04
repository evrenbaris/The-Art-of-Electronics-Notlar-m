import math

vref = 3.3
bits = 12
lsb = vref / (2 ** bits)
q_rms = lsb / math.sqrt(12)

print(f"ADC: {bits} bit, Vref={vref} V")
print(f"LSB = {lsb*1000:.3f} mV")
print(f"Quantization RMS = {q_rms*1000:.3f} mV")
