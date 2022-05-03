import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

n = 10
Du, Dv, F, k = 0.16, 0.08, 0.035, 0.065  # Bacteria 1
# Du, Dv, F, k = 0.14, 0.06, 0.035, 0.065  # Bacteria 2
# Du, Dv, F, k = 0.16, 0.08, 0.060, 0.062  # Coral
# Du, Dv, F, k = 0.19, 0.05, 0.060, 0.062  # Fingerprint
# Du, Dv, F, k = 0.10, 0.10, 0.018, 0.050  # Spirals
# Du, Dv, F, k = 0.12, 0.08, 0.020, 0.050  # Spirals Dense
# Du, Dv, F, k = 0.10, 0.16, 0.020, 0.050  # Spirals Fast
# Du, Dv, F, k = 0.16, 0.08, 0.020, 0.055  # Unstable
# Du, Dv, F, k = 0.16, 0.08, 0.050, 0.065  # Worms 1
# Du, Dv, F, k = 0.16, 0.08, 0.054, 0.063  # Worms 2
# Du, Dv, F, k = 0.16, 0.08, 0.035, 0.060  # Zebrafish

Z = np.zeros((n+2, n+2), [('U', np.double), ('V', np.double)])

U, V = Z['U'], Z['V']
print(U)
'''
[1:-1, 1:-1]
Select 2nd row to the 2nd last row
Select 2nd column to the 2nd last column
'''
u, v = U[1:-1, 1:-1], V[1:-1, 1:-1]


'''
To Figure Out:
How does U get from 0s to having some 1s?
Seems like u[...] = 1.0 has something to do with it
'''
r = 20
u[...] = 1.0
print(U)
U[n//2-r:n//2+r, n//2-r:n//2+r] = 0.50
V[n//2-r:n//2+r, n//2-r:n//2+r] = 0.25
print(U)
u += 0.05*np.random.uniform(-1, +1, (n, n))
v += 0.05*np.random.uniform(-1, +1, (n, n))

print(4*U[1:-1, 1:-1])

def update(frame):
    global U, V, u, v, im

    # i = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    for i in range(10):
        Lu = (U[0:-2, 1:-1] +
              U[1:-1, 0:-2] - 4*U[1:-1, 1:-1] + U[1:-1, 2:] +
              U[2:, 1:-1])
        Lv = (V[0:-2, 1:-1] +
              V[1:-1, 0:-2] - 4*V[1:-1, 1:-1] + V[1:-1, 2:] +
              V[2:, 1:-1])
