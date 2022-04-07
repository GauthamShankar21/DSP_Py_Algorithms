import numpy as np
import operator as op
def linear_conv(x,h):
  N=len(x)+len(h)-1
  x1=np.zeros((N))
  h1=np.zeros((N))
  y=np.zeros((N))
  m=len(x)
  n=len(h)
  for i in range(m):
    x1[i]=x[i]

  for i in range(n):
    h1[i]=h[i]
  for i in range(N):
    for j in range(i+1):
      y[i]=y[i]+x1[j]*h1[i-j]
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

## commutative property
lhs=linear_conv(a,b)
rhs=linear_conv(b,a)
(len1,len2)=comp_array(lhs,rhs)
if(len1==len2):
  print("commutative property is satisfied")
  print("result is",lhs)
else:
  print("not sarisfied1")

##assosiative property a*(b*c)=(a*b)*c
lhs1=linear_conv(a,linear_conv(b,c))
rhs1=linear_conv(linear_conv(a,b),c)
(len1,len2)=comp_array(lhs,rhs)
if(len1==len2):
  print("satisfied")
  print("result is ",lhs1)
else:
  print("not satisfied")

# distributive property a*(b+c)=a*b + a*c
lhs2=linear_conv(a,(b+c))
rhs2=linear_conv(a,b)+linear_conv(a,c)
(len1,len2)=comp_array(lhs2,rhs2)
if(len1==len2):
  print("satisfied")
  print("result is=",lhs2)
else:
  print("not satisfied")
