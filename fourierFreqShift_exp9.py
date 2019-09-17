# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 09:47:53 2019

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

def shiftedCoeffs(sig,harmonics):
    coeffs = []
    T = len(sig)
    t = np.arange(T)
    for n in range(harmonics+1):
        an = 2/T*(sig*(np.cos((2*np.pi*t*n/T) - (4*2*np.pi*t/T)))).sum()
        bn = 2/T*(sig*(np.sin((2*np.pi*t*n/T) - (4*2*np.pi*t/T)))).sum()
        coeffs.append((an,bn))
    return coeffs

fs = 300
harmonics = 150
t_period = np.linspace(0,1,fs)
sig = 2.5*(1+signal.sawtooth(t_period*24,0.95))
originalCoeffs = fourierCoeffs(sig,harmonics)

shiftCoeffs = shiftedCoeffs(sig,harmonics)
shift = reconstruct(len(sig),shiftCoeffs)

plt.subplot(611)
plt.plot(t_period,sig)
plt.ylabel("original")
plt.ylim(0,5)
    
plt.subplot(612)
plt.stem(plotA(originalCoeffs))
plt.ylabel("a1")

plt.subplot(613)
plt.stem(plotB(originalCoeffs))
plt.ylabel("b1")

plt.subplot(614)
plt.stem(plotA(shiftCoeffs))
plt.ylabel("a2")

plt.subplot(615)
plt.stem(plotB(shiftCoeffs))
plt.ylabel("b2")

plt.subplot(616)
plt.plot(t_period,shift)
plt.ylabel("freq shifted")
plt.ylim(-10,10)
