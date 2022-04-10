import numpy as np
def filter(b,a,x):
  N=len(x)
  b=list(b)+[0]*(N-len(b))
  a=list(a)+[0]*(N-len(a))
  y=np.zeros((N))
  for n in range(N):
    term1=0
    term2=0
    for k in range(n+1):
      term1=term1-a[k]*y[n-k]
      term2=term2+b[k]*x[n-k]
    y[n]=term1+term2
  return y   
x=input('Enter the input signal=')
b=np.array([int(i) for i in x.split()])
y=input('Enter the input signal=')
a=[int(i) for i in y.split()]   
z=input('Enter the input signal=')
x=[int(i) for i in z.split()]
y = filter(b,a,x)
print(y)
