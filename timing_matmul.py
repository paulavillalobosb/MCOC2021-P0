from numpy import zeros
from time import perf_counter

N = 5000					# Tamaño de las matrices

A = zeros((N, N)) +1		# Matriz A de tamaño NxN
B = zeros((N, N)) +2		# Matriz B de tamaño NxN

#print (f"A = {A}")
#print (f"B = {B}")

t1 = perf_counter()

C = A@B						# @ : multiplicador de matrices (matmul) / * : multiplicacion de arreglos

#print (f"C = {C}")

t2 = perf_counter()

dt = t2 - t1

print (f"dt = {dt}")





