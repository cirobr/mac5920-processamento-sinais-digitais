# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np

N = 20
L = 3; M = 7

h = np.zeros(N)
h[0] = 1/L
for m in range(1, M):
    h[m] = 1 / L
    h[-m] = 1 / L