## autocorrelation and cross correlation 
import numpy as np
import matplotlib.pyplot as plt
def linear_conv(x,h):
  m=len(x)
  n=len(h)
  N=m+n-1
  y=np.zeros((N))
  x=list(x)
  h=list(h)
  x=x+[0]*(N-m)
  h=h+[0]*(N-n)
  for i in range(N):
    for j in range(i+1):
      y[i]=y[i]+x[j]*h[i-j]
  return y

def flip(x):
  N=len(x)
  y = np.zeros((N))
  for i in range(N):
     y[i]=x[N-1-i]
  return y

x1=input('Enter the input signal=')
x=[int(i) for i in x1.split()]
Y = linear_conv(x,flip(x))
print(Y)
N=len(Y)
n = [i for i in np.arange(np.ceil(-N/2),np.floor(N/2)+1)]
print("Autocorrelation is always symmetric about n=0")
print("Peak amplitude of autocorrelation function is n=0")
srt =np.sort(Y)
en1 =srt[N-1]
print('Energy of autocorrelation function is =',en1)
h1=input('Enter the input signal=')
h=[int(i) for i in h1.split()]
y1=linear_conv(x,np.flip(h))
print(y1)
print("Cross correlation function need not be symmetric about n=0")
print("Peak amplitude of cross correlation function need not be n=0")
plt.subplot(2,1,1)
plt.stem(n,Y)
plt.subplot(2,1,2)
plt.stem(n,y1)
plt.show()
