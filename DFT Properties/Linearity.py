##Linearity property
import numpy as np
a1=int(input('Enter the value of 1st constant='))
a2=int(input('Enter the value of 2nd constant='))
x=input('Enter the input signal=')
x1=[int(i) for i in x.split()]
y=input('Enter the input signal=')
x2=[int(i) for i in y.split()]
print(type(x2))
X1 = [element * a1 for element in x1]
X2 = [element * a2 for element in x2]
X=[]
for (item1, item2) in zip(X1, X2):
    X.append(item1+item2)
lhs=np.fft.fft(X)
print(lhs)
rhs = a1*np.fft.fft(x1)+a2*np.fft.fft(x2)
print(rhs)
if(list(lhs)==list(rhs)):
  print("Linearity property is satisfied")
  print(lhs,rhs)
