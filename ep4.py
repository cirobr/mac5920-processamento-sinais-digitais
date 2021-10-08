# importa dependências
import math as m
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import dct, idct

# realiza compressão/descompressão de x com parâmetro de limiarização c e devolve x~, Dc e Pc
def CompDescomp(x,c):
    # calcula DCT e faz compressão por limiarização
    C=dct(x, norm='ortho')
    cM = c*np.max(abs(C)) # limiar de compressão
    CC = C*(abs(C)>=cM) # DCT comprimida
    xtil = idct(CC, norm='ortho') # sinal reconstruído
    Pc = sum(abs(C)>=cM)/x.size # taxa de compressão (proporção de coeficientes mantidos)
    if np.linalg.norm(x)**2>0:
        Dc = np.linalg.norm(x-xtil)**2/np.linalg.norm(x)**2 # distorção relativa
    else:
        Dc = np.linalg.norm(x-xtil)**2 # calcula distorção absoluta se sinal é nulo
    return xtil,Pc,Dc


# gera sinal descontínuo com 30% de +1 e o restante -1, no intervalo [0,256)
N=256;M=0.3;x = -1+2*(np.array(range(N))<M*N);

# realiza compressão/descompressão com c=0.1
xtil,Pc,Dc = CompDescomp(x,0.1)

# Resposta do exercício 1a
def c_otimo(x, d):
    eps = 0.001
    c = np.arange(0, 1 + eps, eps)
    
    for i in range(len(c)):
        Dc = CompDescomp(x, c[i])[2]
        cStar = c[i]
        if Dc > d:
            cStar = c[i-1] 
            if i == 0:
                cStar = 0                
            break
    
    return (cStar)

# Resposta do exercício 2a
def CompDescompSegm(x, B):

    qtSeg = int(len(x) / B)
    xSegments = []

    delta = 1e-8
    cStar        = np.zeros(qtSeg)
    xTilSegments = []
    PcSegments   = np.zeros(qtSeg)
    DcSegments   = np.zeros(qtSeg)

    for i in range(qtSeg):

        # recortar x em segmentos
        a = i * B
        b = (i+1) * B
        s = x[a : b]
        xSegments.append(s)
        
        # comprimir cada segmento e escolher o respectivo limiar ótimo
        cStar[i] = c_otimo(xSegments[i], delta)
        xTilSeg, PcSegments[i], DcSegments[i] = CompDescomp(xSegments[i], cStar[i])
        xTilSegments.append(xTilSeg)
    
    # Calcula sinal reconstruído
    xTil = np.ravel(xTilSegments)
    
    # Calcular a taxa de compressão média
    Pc = np.mean(PcSegments)
    
    # Calcular a distorção relativa
    Dc = np.linalg.norm()

    return (xTil, Pc)

print(CompDescompSegm(x, 32)[1])

