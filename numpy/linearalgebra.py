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

#solcing equations and inverting matrices -
#we use np.linalg.solve(a,b) to solve for x in ax=b
#linald.lstsq() finds best fir minimizing difference between , when system doesnt have an exact solution, predicted and actual values
#functions used
# tensorsolve() for tensor equations
#inv and pinv for inverse and pseudo inverse of a matrix
#tensorinv()for inverse of a n dimension array.

#special functions used-
#np,linalg.det() for determinant of a matrix, trace(),numpy.linalg.norm()	Matrix or vector norm.
#numpy.linalg.cond()	Compute the condition number of a matrix.
#numpy.linalg.matrix_rank()	Return matrix rank of array using SVD method
#numpy.linalg.cholesky()	Cholesky decomposition.
#numpy.linalg.qr()	Compute the qr factorization of a matrix.
#numpy.linalg.svd()	Singular Value Decomposition.

#finally eigen value functions
#to get an array of eigen values and matrix of eigenvalues  for a hermitian or real symmetric matrices we use
#-- linalg.eigh()
#for normal matrices we use - linalg.eig()
#some commonly used functions-
#linalg.eigvals()	Compute the eigenvalues of a general matrix.
#linalg.eigvalsh(a[, UPLO])	Compute the eigenvalues of a complex Hermitian or real symmetric matrix.