import numpy as np

Z = np.arange(12).reshape((3, 4))
# print(Z)
S = np.array([0, 1, 2])
# print(np.add.reduceat(Z,S, axis=0))

A = np.array([[112887, 204288],
              [127076, 168281],
              [125565,  48593],
              [59113,  61300]])
print(np.where((A > 0) & (A < 262144)))
