x1=input('Enter the input signal=')
x=[int(i) for i in x1.split()]
N=len(x)
x=np.array(x)
lhs=sum(abs(x)**2)
rhs=sum(abs(np.fft.fft(x))**2)*(1/N)
if(lhs==rhs):
  print("Parsevals theorem is verified")
  print(lhs,rhs)
