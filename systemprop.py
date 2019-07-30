import matplotlib.pyplot as plt
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

def sys2(n):
    y = step(n)-step(1-n)
    return y

def sys3(start,end,x,t):
    y = np.zeros(len(t))
    ind = np.where((t<=end)&(t>=start))
    y[ind] = x[ind]
    return y

def linearityChecker(k,l):
    plt.subplot(612)
    #plt.title("ky1[n]+ly2[n]")
    sig1 = k*sys1(1,n+1)+l*sys1(1,1-n)
    print(sig1)
    plt.stem(n,sig1)

    plt.subplot(613)
    #plt.title("y{kx1[n]+lx2[n]}")
    sig2 = sys1(k,n+1)+sys1(l,1-n)
    plt.stem(n,sig2)

    count = 0
    for (i, j) in zip(sig1, sig2):
        if (i == j):
            continue
        else:
            count = 1
            break

    if (count == 0):
        print("It is linear")

    else:
        print("It is non-linear")


linearityChecker(4,8)

def timeChecker(k,n):
    plt.subplot(614)
    sig1 = sys2(n-k)
    plt.stem(n,sig1)
    print(sig1)

    plt.subplot(615)
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

plt.subplot(611)
x=step(n)
plt.stem(n,x)

plt.subplot(616)
start = 0
end = 2
y = sys3(start,end,x,n)
plt.stem(n,y)

if (start<0):
    print("it is non causal")
else: print("It is causal")

plt.show()