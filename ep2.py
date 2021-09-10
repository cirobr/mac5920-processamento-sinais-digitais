import math
import numpy as np

v_1 = np.array((1, 1, 0))
v_2 = np.array((-1, 1, 1))
v_3 = np.array((1, -1, 2))

S = np.array((v_1, v_2, v_3), dtype = float)
nVectors = np.shape(S)[0]
print("base S: \n", S)

innerProductZero = [np.inner(S[k, :], S[l, :]) == 0 for k in range(0, nVectors-1) for l in range(k+1, nVectors)]
print("\nTodos os produtos internos iguais a zero:", np.all(innerProductZero))



x = np.array((3, 4, 5), dtype=float)
print("vetor x: ", x)

num = np.inner(x, S)
den = np.diagonal(np.inner(S, S))
a = num / den
x_hat = np.sum((a * S.T), axis=1)

print("coeficientes a: ", a)
print("vetor x_hat é igual ao vetor x: ", np.all(x == x_hat))



print("vetor x: ", x)
print("\nbase S: \n", S)

S_linha = S.T / np.sqrt(np.diagonal(np.inner(S, S)))
S_linha = S_linha.T
print("\nbase ortonormal S': \n", S_linha)
print("\nnorma unitária para s vetores de S': ", np.linalg.norm(S_linha, axis=1))

num = np.inner(x, S_linha)
den = np.diagonal(np.inner(S_linha, S_linha))
a_linha = num / den
x_hat = np.sum((a_linha * S_linha.T), axis=1)

print("coeficientes a': ", a_linha)
print("vetor x_hat é igual ao vetor x: ", np.linalg.norm(x - x_hat) < 1e-12)