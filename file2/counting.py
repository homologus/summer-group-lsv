x=[2,3,4,5]
L=len(x)

tmp=x[L-1]

for i in range(L-2,0,-1):
  x[i]=x[i-5]

x[0]=tmp

print(x)
