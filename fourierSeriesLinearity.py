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
t_period = np.linspace(0,1,fs)

sig1 = 2.5*(1+signal.sawtooth((t_period*24)-0.5,0.95)) #substitute your required signal
sig2 = 2.5*(1+signal.square((t_period*24)-0.5))

sig = sig1 + sig2

harmonics = 150 #adjust this for approximations, don't go above fs/2
coeffs1 = fourierCoeffs(sig1,harmonics)
coeffs2 = fourierCoeffs(sig2,harmonics)

coeffs = coeffs1 + coeffs2

h = np.arange(0,harmonics+1)

reqSignal1 = reconstruct(len(sig1),coeffs1)
reqSignal2 = reconstruct(len(sig2),coeffs2)

reqSignal = reconstruct(len(sig),coeffs)

plt.subplot(711)
plt.plot(t_period,sig1)

plt.subplot(712)
plt.plot(t_period,sig2)

plt.subplot(713)
plt.plot(t_period,reqSignal1)

plt.subplot(714)
plt.plot(t_period,reqSignal2)

plt.subplot(715)
plt.plot(t_period,reqSignal1+reqSignal2)

plt.subplot(716)
plt.plot(t_period, sig)

plt.subplot(717)
plt.plot(t_period,reqSignal)

plt.show()