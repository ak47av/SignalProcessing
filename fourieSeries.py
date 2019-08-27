#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:56:01 2019

@author: akav
"""

#given fourier approximation is for a right sawtooth signal

import numpy as np
import matplotlib.pyplot as plt


plt.style.use("ggplot")

t = np.linspace(-5,5,1000)

T = 2

harmonics = 30

def a(n):
    n = int(n)
    return 0#return Co-Efficient An
    
def b(n):
    n = int(n)
    return ((-2*np.cos(n*np.pi)/(np.pi*n))+(2*np.sin(n*np.pi)/(np.pi*np.pi*n*n))) #return Co-Efficient Bn

def w(n):
    global T 
    wn = (2*np.pi*n)/T
    return wn

def trigSeries(n,t):
    a0 = 0 #enter constant coeffiecient A0
    wave = a0/2
    
    for n in range(1,harmonics):
        try:
            wave = wave+(a(n)*np.cos(w(n)*t))+(b(n)*np.sin(w(n)*t))
        except:
            print('passs')
            pass
    return wave



f = []

for i in t:
    f.append(trigSeries(harmonics,i))
    
plt.plot(t,f)    
    
        