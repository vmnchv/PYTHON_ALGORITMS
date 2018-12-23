def funct1(n)
t = 1
#for i in range(1, n + 1):
t = t * -0.5
return funct1(n) + funct1(n-1)
print(funct1(4))