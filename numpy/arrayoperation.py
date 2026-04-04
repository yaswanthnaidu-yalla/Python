import numpy as np
a = np.array([[2,3,4],[3,4,5]])
print(a)
#dtype gives the type of elements present in the array.
#type can be specified while creation
c = np.array([[1,2],[3,4]], dtype=complex)
print(c)
#creating an array of zeroes and ones
d = np.zeros((3,3))
e= np.ones((4,4))
print(d)
print(e)

#using arange to create arrays
b = np.arange(1,10,2)
print(b)

#using linspace

print(np.linspace(0,7,20))
print(np.sin(a))
