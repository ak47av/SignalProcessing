import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

plt.subplot(421)
t = np.arange(10)
x = signal.square(t,duty = 0.5)
plt.plot(t,x)

plt.subplot(422)
t = np.arange(10)
h1 = np.sin(t)
plt.plot(t,h1)

plt.subplot(423)
t = np.arange(10)
h2 = np.cos(t)
plt.plot(t,h2)

plt.subplot(424)
t = np.arange(19)
plt.plot(t,np.convolve(x,h1))

plt.subplot(425)
t = np.arange(28)
plt.plot(t,np.convolve(np.convolve(x,h1),h2))

plt.subplot(426)
t = np.arange(28)
plt.plot(t,np.convolve(x,np.convolve(h1,h2)))



plt.show()