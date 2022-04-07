#Computation of nN point DFT
import numpy as np
import matplotlib.pyplot as plt
from cmath import exp
from math import pi
x=input('Enter the input signal=')
x1=[int(i) for i in x.split()]
print('Input sequence is=')
N=len(x1)
print(N)
X=np.zeros((N),'complex')
for k in range(N):
  for n in range(N):
     X[k]=X[k]+x1[n]*exp (-1j*2*pi*k*n/N)
print('The dft using formula is=',X)
X1=np.fft.fft(x1)
print('The dft using built in routine is=',X1)
plt.subplot(4,1,1)
plt.stem(range(N),abs(X))
plt.xlabel('k---->')
plt.ylabel('amplitude---->')
plt.title('DFT magnitude using formula')
plt.subplot(4,1,2)
plt.stem(range(N),np.angle(X))
plt.xlabel('k---->')
plt.ylabel('amplitude---->')
plt.title('DFT magnitude using Built in Function')
plt.subplot(4,1,3)
plt.stem(range(N),abs(X1))
plt.xlabel('k---->')
plt.ylabel('amplitude---->')
plt.title('DFT phase using formula')
plt.subplot(4,1,4)
plt.stem(range(N),np.angle(X1))
plt.xlabel('k---->')
plt.ylabel('amplitude---->')
plt.title('DFT phase using Built in Function')
#plt.tight_layout()
plt.show()
