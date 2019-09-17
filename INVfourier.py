# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 11:22:39 2019

@author: Sampath
"""

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import signal

def invFourier(xk):
    N = len(xk)
    sig = []
    for k in range(N):
        xn = 0
        for t in range(N):
            xn += (1/(2*np.pi))*xk[t]*(math.cos(2*np.pi*k*t/N)+(1j*math.sin(2*np.pi*k*t/N)))
        sig.append(xn)
    return sig

Fs = 500
w = np.linspace(0,2*np.pi,Fs)

def step(w):
    arr = np.zeros(len(w))
    ind = np.where((w<=3*np.pi/2)&(w>=np.pi/2))
    arr[ind] = 1
    return arr

plt.subplot(511)
plt.plot(w,step(w))

hn = invFourier(step(w))

t = np.linspace(0,Fs,Fs)

freq = 10
xn = np.sin(2*np.pi*freq*t) + np.sin(2*np.pi*3*t)

plt.subplot(512)
plt.plot(hn)

plt.subplot(513)
plt.plot(t,xn)

plt.subplot(514)
plt.plot(np.convolve(hn,xn))

freq = 1
xn = np.sin(2*np.pi*freq*t)
plt.subplot(515)
plt.plot(np.convolve(hn,xn))