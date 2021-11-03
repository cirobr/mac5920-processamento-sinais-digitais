import math
import numpy as np
#import matplotlib.pyplot as plt
from scipy.fft import fft, ifft
from scipy.linalg import circulant

N = 4

h = np.array((1, 2-1j, -1j, -1+2j))
print("Vetor não trivial h:", h)

H = fft(h)
print("\nDFT de h...........:", H)

Mh = circulant(h)
print("\nMatriz circulante Mh:\n", Mh)

A = np.linalg.eig(Mh)
print("\nAutovalores de Mh:\n", A[0])
print("\nAutovetores de Mh:\n", A[1])

ks = np.arange(N)
ms = np.arange(N)

for k in ks:
    E = [ (np.exp(1j * 2 * math.pi * k * m/N) ) for m in ms ]
    E = np.array(E)
    esq = np.matmul(Mh, E)
    dire = H * E
    print("\n", esq)
    print("\n", dire)
    break