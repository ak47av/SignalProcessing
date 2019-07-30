# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 12:53:50 2019

@author: Sampath
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def newConvolve(x,h):
    for i in range(len(x)):
        for j in range(len(h)):
            y[i][i+j]=x[i]*h[j]
    for i in range(len(x)+len(h)-1):
        for j in range(len(h)+len(x)-1):
            con[i]=y[j][i]+con[i]
    return con

plt.subplot(7,3,1)
t=np.arange(0,4*np.pi,1)
x1=7*np.sin(t)
h=-np.sinc(t)
plt.stem(t,x1)
y=np.zeros((25,25))
con=np.zeros(25)
t=np.arange(25)
plt.subplot(7,3,2)
plt.stem(t,newConvolve(x1,h))
plt.subplot(7,3,3)
plt.stem(t,np.convolve(x1,h))

plt.subplot(7,3,4)
t=np.arange(0,4*np.pi,1)
x2=7*np.sin(10*t)
plt.stem(t,x2)
y=np.zeros((25,25))
con=np.zeros(25)
t=np.arange(25)
plt.subplot(7,3,5)
plt.stem(t,newConvolve(x2,h))
plt.subplot(7,3,6)
plt.stem(t,np.convolve(x2,h))        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
plt.subplot(7,3,7)
t=np.arange(0,4*np.pi,1)
x3=7*np.sin(50*t)
plt.stem(t,x3)
y=np.zeros((25,25))
con=np.zeros(25)
t=np.arange(25)
plt.subplot(7,3,8)
plt.stem(t,newConvolve(x3,h))
plt.subplot(7,3,9)
plt.stem(t,np.convolve(x3,h))

plt.subplot(7,3,10)
t=np.arange(0,4*np.pi,1)
x4=7*np.sin(100*t)
plt.stem(t,x4)
y=np.zeros((25,25))
con=np.zeros(25)
t=np.arange(25)
plt.subplot(7,3,11)
plt.stem(t,newConvolve(x4,h))
plt.subplot(7,3,12)
plt.stem(t,np.convolve(x4,h))

plt.subplot(7,3,13)
t=np.arange(0,4*np.pi,1)
x5=7*np.sin(150*t)
plt.stem(t,x5)
y=np.zeros((25,25))
con=np.zeros(25)
t=np.arange(25)
plt.subplot(7,3,14)
plt.stem(t,newConvolve(x5,h))
plt.subplot(7,3,15)
plt.stem(t,np.convolve(x5,h))

plt.subplot(7,3,16)
t=np.arange(0,4*np.pi,1)
x6=7*np.sin(200*t)
plt.stem(t,x6)
y=np.zeros((25,25))
con=np.zeros(25)
t=np.arange(25)
plt.subplot(7,3,17)
plt.stem(t,newConvolve(x6,h))
plt.subplot(7,3,18)
plt.stem(t,np.convolve(x6,h))


t = np.arange(0,30,1)
plt.subplot(7,3,19)
sq = signal.square(t,duty=0.5)
plt.stem(t,sq)

def newConvolve2(x,h):
    y=[]
    temp=0
    for i in range(len(x)):
        for j in range(0,i+1,1):
            temp += (x[j]*h[i-j])
        y.append(temp)
        temp=0
    return y

plt.subplot(7,3,20)
t = np.arange(0,30,1)
h2=-np.sinc(t)
plt.stem(t,newConvolve2(sq,h2))
t = np.arange(0,59)
plt.subplot(7,3,21)
plt.stem(t,np.convolve(sq,h2))





