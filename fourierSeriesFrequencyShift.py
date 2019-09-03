import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

def fourierCoeffs(sig,N):
    result = []
    T = len(sig)
    t = np.arange(T)
    for n in range(N+1):
        an = 2/T*(sig * np.cos(2*np.pi*n*t/T)).sum()
        bn = 2/T*(sig * np.sin(2*np.pi*n*t/T)).sum()
        result.append((an, bn))
    return np.array(result)

def shiftCoeffs(sig,N):
    result = []
    T = len(sig)
    t = np.arange(T)
    for n in range(N + 1):
        an = 2 / T * (sig * np.cos((2 * np.pi * n * t / T)-(8 * np.pi *2* t / T))).sum()
        bn = 2 / T * (sig * np.sin((2 * np.pi * n * t / T)-(8 * np.pi *2* t / T))).sum()
        result.append((an, bn))
    return np.array(result)

def reconstruct(P, anbn):
    result = 0
    t = np.arange(P)
    for n, (a, b) in enumerate(anbn):
        if n == 0:
            a = a/2
        result = result + a*np.cos(2*np.pi*n*t/P) + b * np.sin(2*np.pi*n*t/P)
    return result

def plotA(anbn):
    A =[]
    for n, (a, b) in enumerate(anbn):
        A.append(a)
    return A

def plotB(anbn):
    B =[]
    for n, (a, b) in enumerate(anbn):
        B.append(b)
    return B


fs = 300
harmonics = 150
t_period = np.linspace(0,2,fs)

sig = 2.5*(1+signal.square((t_period*24),0.7))

coeffs = fourierCoeffs(sig,harmonics)
shiftedCoeffs = shiftCoeffs(sig,harmonics)

plt.subplot(711)
plt.stem(plotA(coeffs))

plt.subplot(712)
plt.stem(plotB(coeffs))

plt.subplot(713)
plt.stem(plotA(shiftedCoeffs))

plt.subplot(714)
plt.stem(plotB(shiftedCoeffs))

req1 = reconstruct(len(sig),coeffs)
req2 = reconstruct(len(sig),shiftedCoeffs)

plt.subplot(715)
plt.plot(req1)

plt.subplot(716)
plt.plot(req2)

plt.show()