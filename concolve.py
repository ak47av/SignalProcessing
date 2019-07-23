# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

n = np.linspace(-5,5,1000)

x1 = np.sinc(2*np.pi*n)
x2 = np.sin(2*np.pi*n)

x = np.convolve(x1,x2)

n = np.linspace(-5,14,1999)
plt.plot(n,x)