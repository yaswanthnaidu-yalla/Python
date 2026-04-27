#simply performing operations on arrays without using loops.
import numpy as np
#example 1-
a = np.array([1,2,3,4,5,6,7])
num = 2
result = a+num
print(result)

#example 2-
b = np.array([1,2,3])
c = np.array([2,3,4])
res1 = b+c
print(res1)

#example 3
a3 = np.array([1,4,12])
res = a3>10
print(res)
#applying custom functions
a4 = np.array([1,3,6,9])
vec = np.vectorize(lambda x:x**3+x**2+x**1+1)
res2 = vec(a4)
print(res2)

#sum,mean,max i.e. aggregation operations
a5 = np.array([2,6,12])
r1 = a5.mean()
r2 = a5.max()+a5.sum()
print(r1 ,r2)

#its way faster than loops and much cleaner to implement
