# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 09:56:05 2019

@author: cb.en.u4ece18512
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

def fourierCoeffs(sig,harmonics):
    coeffs= []
    T = len(sig)
    t = np.arange(T)
    for n in range(harmonics+1):
        an = 2/T*(sig*(np.cos(2*np.pi*t*n/T))).sum()
        bn = 2/T*(sig*(np.sin(2*np.pi*t*n/T))).sum()
        coeffs.append((an,bn))
    return coeffs

def reconstruct(P,anbn):
    wave = 0
    t = np.arange(P)
    for n,(a,b) in enumerate(anbn):
        if n==0:
            a = a/2
        wave =wave+ a*np.cos(2*np.pi*n*t/P) + b*np.sin(2*np.pi*n*t/P)
    return wave

def plotA(anbn):
    A = []
    for n,(a,b) in enumerate(anbn):
        A.append(a)
    return A

def plotB(anbn):
    B = []
    for n,(a,b) in enumerate(anbn):
        B.append(b)
    return B

def linear(sig1,sig2,harmonics):
    coeffs= []
    T = len(sig)
    t = np.arange(T)
    for n in range(harmonics+1):
        an = 2/T*(sig1*(np.cos(2*np.pi*t*n/T)) + (sig2*(np.cos(2*np.pi*t*n/T)))).sum()
        bn = 2/T*(sig1*(np.sin(2*np.pi*t*n/T)) + (sig2*(np.sin(2*np.pi*t*n/T)))).sum()
        coeffs.append((an,bn))
    return coeffs

fs = 300
harmonics = 150
t_period = np.linspace(0,1,fs)
sig = 2.5*(1+signal.sawtooth(t_period*24,0.95))
originalCoeffs = fourierCoeffs(sig,harmonics)

x1 = (1+signal.sawtooth(t_period*24,0.95))
x2 = 1.5*(1+signal.sawtooth(t_period*24,0.95))

x1Coeffs = fourierCoeffs(x1,harmonics)
x2Coeffs = fourierCoeffs(x2,harmonics)

plt.subplot(711)
plt.stem(plotA(x1Coeffs))
plt.ylabel("a1")

plt.subplot(712)
plt.stem(plotB(x1Coeffs))
plt.ylabel("b1")

plt.subplot(713)
plt.stem(plotA(x2Coeffs))
plt.ylabel("a2")

plt.subplot(714)
plt.stem(plotB(x2Coeffs))
plt.ylabel("b2")

mainCoeffs = linear(x1,x2,harmonics)

plt.subplot(715)
plt.stem(plotA(mainCoeffs))
plt.ylabel("a1+a2")

plt.subplot(716)
plt.stem(plotB(mainCoeffs))
plt.ylabel("b1+b2")

plt.subplot(717)
reconstructedWave = reconstruct(len(sig),mainCoeffs)
plt.plot(t_period,reconstructedWave)



