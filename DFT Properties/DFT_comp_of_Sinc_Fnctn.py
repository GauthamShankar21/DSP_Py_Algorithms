#sinc function
import numpy as np
import matplotlib.pyplot as plt
from math import pi
fs =int(input('Enter the number of samples='))
res=1/fs
t = [i for i in np.arange (-0.5,0.5,res)]
x = [np.sinc(6*pi*i)for i in np.arange(-0.5,0.5,res)]
X1 = np.fft.fft(x)
X2 = np.fft.fftshift(X1)
f = [i for i in np.arange(-fs/2,fs/2)]
plt.subplot(2,1,1)
plt.plot(t,x)
plt.subplot(2,1,2)
plt.plot(f,abs(X2))
plt.show()
