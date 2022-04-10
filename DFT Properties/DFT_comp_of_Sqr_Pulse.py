import numpy as np
import matplotlib.pyplot as plt
x = np.ones(fs)
fs =int(input('Enter the number of samples='))
res=1/fs
t = [i for i in np.arange(-0.5,0.5,res)]
a=int(fs/4)
print(a)
for n in range(a):
  x[n]=0
  x[(a+int(fs/2))+n]=0
x1 = np.fft.fft(x)
x2 = np.fft.fftshift(x1)
f = [i for i in np.arange(-fs/2,fs/2)]
plt.subplot(2,1,1)
plt.plot(t,x)
plt.subplot(2,1,2)
plt.plot(f,abs(x2))
plt.show()
