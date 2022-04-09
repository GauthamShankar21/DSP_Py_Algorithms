import numpy as np
x=input('Enter the input signal=')
x1=[int(i) for i in x.split()]
y=input('Enter the input signal=')
x2=[int(i) for i in y.split()]
X1 = np.fft.fft(x1)
X2 = np.fft.fft(x2)
X3=[]
for num1, num2 in zip(X1, X2):
	X3.append(num1 * num2)
X4 = np.fft.ifft(X3)
print('Cicular Convolution is=',X4)
