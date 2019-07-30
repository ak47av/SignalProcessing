import matplotlib.pyplot as plt
from scipy import signal
import numpy as np

n = np.linspace(-10,10,21)


def step(t):
    arr = np.zeros(len(t))
    ind = np.where((t<=5)&(t>=0))
    arr[ind] = 10
    return arr

def sys2(n):
    y = step(n)-step(1-n)
    return y

def timeChecker(k,n):
    plt.subplot(211)
    sig1 = sys2(n-k)
    plt.stem(n,sig1)
    print(sig1)

    plt.subplot(212)
    sig2 = step(n-k)-step(1-n-k)
    plt.stem(n,sig2)
    print(sig2)

    count = 0
    for (i,j) in zip(sig1,sig2):
        if (i==j):
            continue
        else :
            count = 1
            break

    if (count == 0):
        print("It is time invariant")

    else:
        print("It is time variant")


timeChecker(3,n)

plt.show()

