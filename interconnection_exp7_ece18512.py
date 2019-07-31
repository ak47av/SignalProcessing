# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 08:48:57 2019

@author: cb.en.u4ece18512
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


t = np.arange(50)
fs = 600
x1 = 5*np.sin(2*np.pi*10*t*1/fs)
plt.subplot(5,3,4)
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

plt.subplot(5,3,1)
h1 = (1+signal.sawtooth(t/3,1)*np.exp(-0.0025*t))/2
plt.stem(t,h1)
h2 = np.sin(t)*np.exp(-0.05*t)
plt.subplot(5,3,2)
plt.title("cb.en.u4ece18512 exp7 Jul 31")
plt.stem(t,h2)

h3 = np.zeros(50)
ind1 = np.where((t<=50/3))
h3[ind1] = 1
ind2 = np.where((t>50/3)&(t<=100/3))
h3[ind2] = -1
ind3 = np.where((t>100/3)&(t<=50))
h3[ind3] = 1
plt.subplot(5,3,3)
plt.stem(t,h3)

plt.subplot(5,3,5)
y = np.zeros((99,99))
convolve = np.zeros(99)
h = newConvolve((h1+h2),h3)
t = np.arange(99)
plt.plot(t,h)

plt.subplot(5,3,6)
y = np.zeros((148,148))
convolve = np.zeros(148)
t = np.arange(148)
plt.plot(t,(newConvolve(x1,h)))

t = np.arange(50)
x2 = 5*np.sin(2*np.pi*50*t*1/fs)
plt.subplot(5,3,7)
plt.ylabel("f = 50")
plt.plot(t,x2)

plt.subplot(5,3,8)
t = np.arange(99)
plt.plot(t,h)

plt.subplot(5,3,9)
y = np.zeros((148,148))
convolve = np.zeros(148)
t = np.arange(148)
plt.plot(t,newConvolve(x2,h))

plt.subplot(5,3,10)
t = np.arange(50)
x3 = 5*np.sin(2*np.pi*100*t*1/fs)
plt.ylabel("f = 100 ")
plt.plot(t,x3)

plt.subplot(5,3,11)
t = np.arange(99)
plt.plot(t,h)

plt.subplot(5,3,12)
y = np.zeros((148,148))
convolve = np.zeros(148)
t = np.arange(148)
plt.plot(t,newConvolve(x3,h))

plt.subplot(5,3,13)
t = np.arange(50)
x4 = 5*np.sin(2*np.pi*200*t*1/fs)
plt.ylabel("f = 200")
plt.plot(t,x4)

plt.subplot(5,3,14)
t = np.arange(99)
plt.plot(t,h)

plt.subplot(5,3,15)
y = np.zeros((148,148))
convolve = np.zeros(148)
t = np.arange(148)
plt.plot(t,newConvolve(x4,h))

plt.savefig('newConvolve_exp7_arun.pdf')

