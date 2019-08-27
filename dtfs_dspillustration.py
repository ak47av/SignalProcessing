# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 11:00:36 2019

@author: Sampath
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

Fs = 1000

def fourierSeries(signal,N):
    result = []
    T = len(signal)
    t = np.arange(T)
    for n in range(N+1):
        an = 2/T*(signal * np.cos(2*np.pi*n*t/T)).sum()
        bn = 2/T*(signal * np.sin(2*np.pi*n*t/T)).sum()
        result.append((an, bn))
    return np.array(result)

t_period = np.arange(0, 10, 1/Fs)
F1 = fourierSeries(signal.square(t_period), 2)
F2 = fourierSeries(signal.square(t_period), 500)


def reconstruct(P, anbn):
    result = 0
    t = np.arange(P)
    for n, (a, b) in enumerate(anbn):
        if n == 0:
            a = a/2
        result = result + a*np.cos(2*np.pi*n*t/P) + b * np.sin(2*np.pi*n*t/P)
    return result

plt.subplot(211)
plt.plot(t_period,reconstruct(len(t_period), F1[:100,:]))
plt.subplot(212)
plt.plot(t_period,reconstruct(len(t_period), F2[:100,:]))

