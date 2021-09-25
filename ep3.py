import math
import numpy as np

def DFTingenua(x):
    N = len(x); n = np.array(range(N))
    X = np.ndarray(N, dtype=complex)
    for k in range(N):
        # Calcula a expressão X[k] = Σ x[n]*e^(-i2πkn/N)
        X[k] = sum(x*np.exp(-1j*2*math.pi*k*n/N))
    return X

# teste automatizado:
# para cada vetor e_r da base canônica, computa sua DFT
# e compara com a expressão teórica DFT(e_r)=\overline{E_r} (E_r conjugado)
def testeDFTingenua(N):
    for r in range(N):
        e_r = np.zeros(N); e_r[r] = 1
        DFTe_r = [ np.exp(-1j*2*math.pi*r*k/N) for k in range(N) ]
        
        assert np.linalg.norm(DFTingenua(e_r)-DFTe_r) < 1e-8

for N in [2**b for b in range(10)]:
    testeDFTingenua(N)
    print(f"A função DFTingenua passou no teste com N={N}!")
    