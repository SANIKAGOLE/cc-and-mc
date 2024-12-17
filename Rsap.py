import math

p = 3
q = 7

n = p * q
phi = (p-1) * (q-1)

e = 2
while e < phi:
    if math.gcd(e, phi) == 1:
        break
    else:
        e += 1

k = 2
d = ((k * phi) + 1) / e

print(f'Public key: ({e}, {n})')
print(f'Private key: ({d}, {n})')
