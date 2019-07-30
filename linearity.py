import matplotlib.pyplot as plt
from scipy import signal
import numpy as np

n = np.linspace(-10,10,21)

def step(t):
    arr = np.zeros(len(t))
    ind = np.where((t<=5)&(t>=0))
    arr[ind] = 10
    return arr

def sys1(amplitude,n):
    y = amplitude*(step(n-1)-step(1-n))
    return y




def linearityChecker(k,l):
    plt.subplot(211)
    sig1 = k*sys1(1,n+1)+l*sys1(1,1-n)
    plt.stem(n,sig1)

    plt.subplot(212)
    sig2 = sys1(k,n+1)+sys1(l,1-n)
    plt.stem(n,sig2)

    if(sig1.all()==sig2.all()):
        print("It is linear")
    else:print("it is non-linear")

linearityChecker(4,8)

plt.show()