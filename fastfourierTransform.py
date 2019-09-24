#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 18:32:20 2019

@author: akav
"""
import math
import cmath
import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, fftfreq, ifft

def fourier(xn):
    N = len(xn)
    sig = []
    for k in range(N):
        xk = 0
        for t in range(N):
            xk += xn[t]*(math.cos(2*np.pi*k*t/N)+(1j*math.sin(2*np.pi*k*t/N)))
        sig.append(xk)
    return sig

n = 1000

Lx = 100

omg = 2.0*np.pi/Lx

x = np.linspace(0,Lx,n)
y1 = 1.0*np.cos(5.0*omg*x)
y2 = 1.0*np.sin(10.0*omg*x)
y3 = 0.5*np.sin(20.0*omg*x)

y = y1+y2+y3

freqs = fftfreq(n)

mask = freqs>0

fft_vals = np.asarray(fft(y))

fft_phase = 2.0*(fft_vals/n)
fft_theo = 2.0*np.abs(fft_vals/n)

plt.figure(1)
plt.plot(x,y)

plt.figure(2)
plt.subplot(211)
plt.plot(freqs[mask],fft_theo[mask])

plt.subplot(212)
plt.plot(x,ifft(fft_vals))

plt.figure(3)
plt.subplot(211)
plt.plot(np.angle(fft_vals))

plt.subplot(212)
plt.plot(np.abs(fft_vals))