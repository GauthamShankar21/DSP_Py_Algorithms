import numpy as np
x=input('Enter the input signal=')
x1=[int(i) for i in x.split()]
y=input('Enter the input signal=')
x2=[int(i) for i in y.split()]
N = len(x1)+len(x2)-1
X1 = x1 + [0]*(N-len(x1))
X2 = x2 + [0]*(N-len(x2))
X1=np.array(X1)
X2=np.array(X2)
X3 = np.fft.fft(X1)
X4 = np.fft.fft(X2)
X5 = X3*X4
X6 = np.fft.ifft(X5)
print('Linear Conultion is=',X6)
