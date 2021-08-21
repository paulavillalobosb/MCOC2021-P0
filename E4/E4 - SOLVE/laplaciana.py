#from numpy import zeros
from numpy import float32
from numpy import eye

#def laplaciana(N,dtype):
	
#	A = zeros((N,N),dtype=dtype)
	
#	for i in range (N):
		
#		A[i,i] = 2

#		for j in range (max(0,i-2),i):
		
#			if abs(i-j) == 1:
		
#				A[i,j] = -1
#				A[j,i] = -1

#	return A


def laplaciana(N, dtpe):
	
	e = eye(N) - eye(N,N,1)			# eye : crea una matriz identidad
	A = e + e.T
	return A



