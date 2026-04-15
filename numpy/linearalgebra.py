#simply matrix operations in python but fancier, used in many places and helps in plotting stuff too
import numpy as np
 
A = np.array([[6, 1, 1],
              [4, -2, 5],
              [2, 8, 7]])
 
# Rank of a matrix
print("Rank of A:", np.linalg.matrix_rank(A))
 
# Trace of matrix A
print("Trace of A:", np.trace(A))
 
# Determinant of a matrix
print("Determinant of A:", np.linalg.det(A))
 
# Inverse of matrix A
print("Inverse of A:\n", np.linalg.inv(A))
 
print("Matrix A raised to power 3:\n", np.linalg.matrix_power(A, 3))

#can do dot products using n.dot() for complex values np.use vdot()
#common functions used
#matmul() - matrix product of two arrays
#inner() - inner product of two arrays
#outer() - compute outer products of two arrays
#linalg.multi_dot() - dot product of two or more arrays in single function call
#tensordot() - compute tensor dor product alonf specied axes
#einsum() - einstein summation convention on operands
#einsum_path() - lowest cost contraction order of an einsum expression by considering the creation of intermediate arrays
#linalg.matrix_power() - raise a square matrix to integer power 
#kron() - kronecker product of two arrays.
