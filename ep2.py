import math as m
import numpy as np

v_1 = np.array((1, 1, 0))
v_2 = np.array((-1, 1, 1))
v_3 = np.array((1, -1, 2))

S = np.array((v_1, v_2, v_3), dtype = float)
nRows = np.shape(S)[0]

innerProductZero = [np.inner(S[k,], S[l,]) == 0 for k in range(0, nRows-1) for l in range(k+1, nRows)]
print("Todos os produtos internos iguais a zero:", np.all(innerProductZero))



