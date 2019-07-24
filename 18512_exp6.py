# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 08:44:40 2019

@author: cb.en.u4ece18512
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

n = np.linspace(0,30)

h = np.sinc(2*np.pi*n+(np.pi/2))
plt.subplot(6,2,1)
plt.stem(n,h)
plt.ylabel("h(t)")

freq = 10   
x1 = 7*np.sin(2*np.pi*n*freq)
plt.subplot(6,2,2)
plt.stem(n,x1)
plt.ylabel("x(t),f=10")


def newConvolve(x,h):
    y =[]
    temp=0
    for i in range(len(x)):
        for j in range(0,i+1,1):
            temp += x[j]*h[i-j]
        y.append(temp)
        temp = 0
    return y
    
plt.subplot(6,2,3)
x1 = 7*np.sin(2*np.pi*n*freq)
plt.stem(n,newConvolve(x1,h)) 

freq = 50
plt.subplot(6,2,4)
x1 = 7*np.sin(2*np.pi*n*freq)
plt.stem(n,newConvolve(x1,h))
plt.ylabel("x(t),f=50")



freq = 70
plt.subplot(6,2,5)
x1 = 7*np.sin(2*np.pi*n*freq)
plt.stem(n,newConvolve(x1,h))
plt.ylabel("x(t),f=70")

freq = 100
plt.subplot(6,2,6)
x1 = 7*np.sin(2*np.pi*n*freq)
plt.stem(n,newConvolve(x1,h))
plt.ylabel("x(t),f=100")


freq =150
plt.subplot(6,2,7)
x1 = 7*np.sin(2*np.pi*n*freq)
plt.stem(n,newConvolve(x1,h))  
plt.ylabel("x(t),f=150")


freq=175
plt.subplot(6,2,8)
x1 = 7*np.sin(2*np.pi*n*freq)
plt.stem(n,newConvolve(x1,h)) 
plt.ylabel("x(t),f=175")


freq = 200
plt.subplot(6,2,9)
x1 = 7*np.sin(2*np.pi*n*freq)
plt.stem(n,newConvolve(x1,h))
plt.ylabel("x(t),f=200")


plt.subplot(6,2,10)
plt.ylim(-2,2)
ip = signal.square(n,duty=0.5)
plt.stem(n,newConvolve(ip,h))
plt.ylabel("ip(t),dutyCycle=0.5")

plt.subplot(6,2,11)
plt.ylim(-2,2)
ip = signal.square(n,duty=0.25)
plt.stem(n,newConvolve(ip,h))
plt.ylabel("ip(t),dutyCycle=0.25")

plt.subplot(6,2,12)
plt.ylim(-2,2)
ip = signal.square(n,duty=0.75)
plt.stem(n,newConvolve(ip,h))
plt.ylabel("ip(t),dutyCycle=0.75")



        
