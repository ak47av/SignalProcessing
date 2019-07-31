# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 09:59:40 2019

@author: cb.en.u4ece18512
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


t = np.arange(50)
fs = 800
x1 = 5*np.sin(2*np.pi*10*t*1/fs)
plt.subplot(5,3,1)
plt.ylabel("f = 10")
plt.stem(t,x1)

def newConvolve(x,h):
    for i in range(len(x)):
        for j in range(len(h)):
            y[i+j][j] += x[i]*h[j]
    for i in range(len(x)+len(h)-1):
        for j in range(len(x)+len(h)-1):
            convolve[i] += y[i][j]
    return convolve

h = -np.sinc(t)
plt.subplot(5,3,2)
plt.title("cb.en.u4ece18512 exp7 Jul 31")
plt.stem(t,h)

plt.subplot(5,3,3)
y = np.zeros((99,99))
convolve = np.zeros(99)
t = np.arange(99)
plt.plot(t,(newConvolve(x1,h)))

t = np.arange(50)
x2 = 5*np.sin(2*np.pi*50*t*1/fs)
plt.subplot(5,3,4)
plt.ylabel("f = 50")
plt.plot(t,x2)

plt.subplot(5,3,5)
plt.plot(t,h)

plt.subplot(5,3,6)
y = np.zeros((99,99))
convolve = np.zeros(99)
t = np.arange(99)
plt.plot(t,newConvolve(x2,h))

plt.subplot(5,3,7)
t = np.arange(50)
x3 = 5*np.sin(2*np.pi*100*t*1/fs)
plt.ylabel("f = 100 ")
plt.plot(t,x3)

plt.subplot(5,3,8)
plt.plot(t,h)

plt.subplot(5,3,9)
y = np.zeros((99,99))
convolve = np.zeros(99)
t = np.arange(99)
plt.plot(t,newConvolve(x3,h))

plt.subplot(5,3,10)
t = np.arange(50)
x4 = 5*np.sin(2*np.pi*200*t*1/fs)
plt.ylabel("f = 200")
plt.plot(t,x4)

plt.subplot(5,3,11)
plt.plot(t,h)

plt.subplot(5,3,12)
y = np.zeros((99,99))
convolve = np.zeros(99)
t = np.arange(99)
plt.plot(t,newConvolve(x4,h))

plt.savefig('exampleconvolution_ece18512.pdf')

