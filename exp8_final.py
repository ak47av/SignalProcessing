# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 11:32:11 2019

@author: Sampath
"""

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

sig = 2.5*(1+signal.sawtooth(t_period*24,0.95)) #substitute your required signal
plt.subplot(511)
plt.plot(t_period,sig)

harmonics = 150 #adjust this for approximations, don't go above fs/2 
coeffs = fourierCoeffs(sig,harmonics)

h = np.arange(0,harmonics+1)

#plot a coefficients
plt.subplot(512)
plt.stem(h,plotA(coeffs))

#plot b coefficients
plt.subplot(513)
plt.stem(h,plotB(coeffs))



reqSignal = reconstruct(len(sig),coeffs)

#approximated wave
plt.subplot(514)
plt.plot(t_period,reqSignal)


#difference between actual wave and approximation
plt.subplot(515)
plt.plot(t_period,(sig-reqSignal))








 



