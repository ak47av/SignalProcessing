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
t_period = np.linspace(0,10,fs)

sig = 2.5*(1+signal.square((t_period*5),0.5)) #substitute your required signal
plt.subplot(611)
plt.plot(t_period,sig)

harmonics = 150 #adjust this for approximations, don't go above fs/2
coeffs = fourierCoeffs(sig,harmonics)

h = np.arange(0,harmonics+1)

reqSignal = reconstruct(len(sig),coeffs)

plt.subplot(612)
plt.plot(plotA(coeffs))

shift = 2.5*(1+signal.square((t_period*5)+1,0.5))

plt.subplot(613)
plt.plot(plotB(coeffs))

shiftCoeffs = fourierCoeffs(shift,harmonics)
shiftedSignal = reconstruct(len(shift),shiftCoeffs)

plt.subplot(614)
plt.plot(plotA(shiftCoeffs))

plt.subplot(615)
plt.plot(plotB(shiftCoeffs))

plt.subplot(616)
plt.plot(t_period,shiftedSignal)

plt.show()