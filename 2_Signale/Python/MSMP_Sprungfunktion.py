import numpy as np
import matplotlib.pyplot as plt

def sprung_heaviside(x, M):
    return np.heaviside(x-M, 1)

def sprung_signum(x, M):
    y = 2/(1+np.sign(x-M))
    index = np.argwhere(x==M)
    y[index] = 1
    return y

def sprung_where(x, M):
    y = np.zeros(x.shape)
    indices = np.argwhere(x<M)
    y[indices] = 0
    indices = np.argwhere(x>=M)
    y[indices] = 1
    return y
    
def sprung_schleife(x, M):
    y = np.ones(x.shape)
    for idx in range(0, len(x)):
        if x[idx]<M:
            y[idx] = 0
    return y

def sprung_indexing(x, M):
    y = np.ones(x.shape)
    y[x<M] = 0
    return y

x = np.linspace(-2, 8, 11)
M = 3
y = sprung_indexing(x, 4)

plt.stem(x, y)

    