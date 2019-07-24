# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 09:59:03 2019

@author: cb.en.u4ece18512
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

n = np.linspace(0,30,30)

h = np.sinc(2*np.pi*n+(np.pi/2))
plt.subplot(5,2,1)
plt.stem(n,h)

freq = 10
x1 = 7*np.sin(2*np.pi*n*freq)
plt.subplot(5,2,2)
n = np.linspace(0,30,30)
plt.stem(n,x1)

plt.subplot(5,2,3)
x1 = 7*np.sin(2*np.pi*n*freq)
n = np.linspace(0,59,59)
plt.stem(n,np.convolve(x1,h)) 

freq = 50
plt.subplot(5,2,4)
x1 = 7*np.sin(2*np.pi*n*freq)
n = np.linspace(0,88,88)
plt.stem(n,np.convolve(x1,h))

freq = 70
plt.subplot(5,2,5)
x1 = 7*np.sin(2*np.pi*n*freq/400)
n = np.linspace(0,117,117)
plt.stem(n,np.convolve(x1,h))

freq = 100
plt.subplot(5,2,6)
x1 = 7*np.sin(2*np.pi*n*freq)
n = np.linspace(0,146,146)
plt.stem(n,np.convolve(x1,h))

freq =150
plt.subplot(5,2,7) 
x1 = 7*np.sin(2*np.pi*n*freq)
n = np.linspace(0,175,175)
plt.stem(n,np.convolve(x1,h))  

freq=175
plt.subplot(5,2,8)
x1 = 7*np.sin(2*np.pi*n*freq)
n = np.linspace(0,204,204)
plt.stem(n,np.convolve(x1,h)) 

freq = 200
plt.subplot(5,2,9)
x1 = 7*np.sin(2*np.pi*n*freq)
n = np.linspace(0,233,233)
plt.stem(n,np.convolve(x1,h))

plt.subplot(5,2,10)
plt.ylim(-2,2)
ip = signal.square(n,duty=0.5)
n = np.linspace(0,262,262)
plt.stem(n,np.convolve(ip,h))