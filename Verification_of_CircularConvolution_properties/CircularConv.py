import numpy as np
import operator as op
def circular_conv(x,h):
  N=max(len(x),len(h))
  x1=np.zeros((N))
  h1=np.zeros((N))
  y=np.zeros((N))
  for i in range(len(x)):
    x1[i]=x[i]
  for i in range(len(h)):
    h1[i]=h[i]
  for i in range(N):
    for j in range(N):
      y[i]=y[i]+x1[j]*h1[op.mod((i-j),N)]
  return y
def comp_array(lhs,rhs):
  cnt=0
  for i in range(len(lhs)):
    if(lhs[i]==rhs[i]):
      cnt+=1
  return len(lhs),cnt

x=input('Enter the input signal=')
a=[int(i) for i in x.split()]
y=input('Enter the input signal=')
b=[int(i) for i in y.split()]
z=input('Enter the input signal=')
c=[int(i) for i in z.split()]

## circular convolution commutative property  a*b=b*a
lhs =circular_conv(a,b)
rhs =circular_conv(b,a)
[len1,len2]=comp_array(lhs,rhs)
if(len1==len2):
  print("commutative property of circular conovlution is satisfied")
  print("Commutative property result=",lhs)
else:
  print("Commutative property is not satisfied")

## Associative property using circular convolution a*(b*c)=(a*b)*c
lhs1=circular_conv(a,circular_conv(b,c))
rhs1=circular_conv(circular_conv(a,b),c)
[len1,len2]=comp_array(lhs1,rhs1)
if(len1==len2):
  print("Associative property is satisfied")
  print("Associative property result =",lhs1)
else:
  print("Associative property is not satisfied")


## Distributive property of circular convolution a*(b+c)=a*b + a*c
lhs2 = circular_conv(a,(b+c))
rhs2 = circular_conv(a,b)+circular_conv(a,c)
[len1,len2]=comp_array(lhs2,rhs2)
if(len1==len2):
  print("Distributive property is satisfied")
  print("Distributive property result=",lhs2)
else:
  print("Distributive property is not satisfied")
