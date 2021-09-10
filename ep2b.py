import numpy as np
import math as m

n = np.arange(0, 4)

E0 = np.exp(1j * 2 * m.pi * 0 * n / 4)
E1 = np.exp(1j * 2 * m.pi * 1 * n / 4)
E2 = np.exp(1j * 2 * m.pi * 2 * n / 4)
E3 = np.exp(1j * 2 * m.pi * 3 * n / 4)

E = np.array((E0, E1, E2, E3), dtype=complex)
nVectors = np.shape(E)[0]
print("base E: \n", E)

innerProducts = [np.inner(E[k, :], np.conjugate(E[l, :])) for k in range(0, nVectors-1) for l in range(k+1, nVectors)]
innerProducts = np.array(innerProducts)
print("\nprodutos internos:\n", innerProducts)
print("\nTodos os produtos internos iguais a zero:", np.all(np.absolute(innerProducts) < 1e-12))



x = np.array((1, 5, -2, 3), dtype=complex)
print("vetor x: ", x)

num = np.inner(x, np.conjugate(E))
den = np.diagonal(np.inner(E, np.conjugate(E)))
a = num / den
x_hat = np.sum((a * E.T), axis=1)

print("coeficientes a: ", a)
print("vetor x_hat é igual ao vetor x: ", np.all(np.absolute(x - x_hat) < 1e-12))
