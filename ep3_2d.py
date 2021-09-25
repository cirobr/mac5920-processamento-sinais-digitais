import math
import numpy as np

# Resposta do exercício 1a
def DFT2ingenua(A):
    M = A.shape[0]
    N = A.shape[1]
    Ahat = np.zeros((M, N), dtype = complex)
    for k in range(M):
        for l in range(N):
            soma1 = 0j
            for r in range(M):
                soma2 = 0j
                for s in range(N):
                    soma2 += A[r][s] * np.exp(-1j * 2 * math.pi * (k * r/M + l * s/N))
                soma1 += soma2
            Ahat[k][l] = soma1
    
    return Ahat

# Resposta do exercício 1b
def testeDFT2ingenua(M,N):
    for r in range(M):
        for s in range(N):
            e_rs = np.zeros((M,N)); e_rs[r][s] = 1
            DFTe_rs = [[ np.exp(-1j*2*math.pi*(r*k/M+s*l/N)) for k in range(M)] for l in range(N) ]
            DFTe_rs = np.array(DFTe_rs).T
            DFi = DFT2ingenua(e_rs)
            assert np.linalg.norm(DFT2ingenua(e_rs)-DFTe_rs) < 1e-8
            
for M,N in [(2**b,2**c) for (b,c) in np.ndindex((5,5))]:
    testeDFT2ingenua(M,N)
    print(f"A função DFT2ingenua passou no teste com MxN={M}x{N}!")
