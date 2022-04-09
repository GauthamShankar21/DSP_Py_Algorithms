#verification of sampling theorem
import numpy as np
import matplotlib.pyplot as plt
from math import cos,sin,pi
res = float(input('Enter the resolution(res)='))
fm = int(input('Enter the Signal frequency in Hz(fm)='))
t = [i for i in np.arange(0,1,res)]
xt = [cos(2*pi*fm*i)for i in np.arange(0,1,res)]
Fs1 = int(input('Enter the sampling frequency(fs) in Hz(>>fm)='))
N1=Fs1
T=1/Fs1
n = [i for i in np.arange(0,N1)]
xn1= [cos(2*pi*(fm/Fs1)*i)for i in np.arange(0,N1)]
xr = np.zeros((len(xt)))
t2=0.001
for t1 in range(int(1/res)):
  for n1 in range(N1):
    xr[t1] = xr[t1]+xn1[n1]*(sin((pi/T)*(t2-n1*T)))/((pi/T)*(t2-n1*T))
  t2 = t2+0.001
plt.subplot(3,1,1)
plt.plot(t,xt)
plt.subplot(3,1,2)
plt.stem(n,xn1)
plt.subplot(3,1,3)
plt.plot(t,xr)
plt.show()
