from numpy import double
import scipy.sparse as sp
import scipy.sparse.linalg as lin
from time import perf_counter

def laplaciana(N, t):
	d = sp.eye(N,N,1,dtype=t)
	return 2*sp.eye(N, dtype =t) - d - d.T


Ns = [1, 5, 10, 15, 20, 30, 40, 50, 60, 70, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000, 10000]
corridas = 10

for i in range (corridas):

	txt = open(f"Rendimiento_inv_{i+1}_matriz_llena.txt", "w")

	for N in Ns:
		
		t1 = perf_counter()	

		A = laplaciana(N, t = double)	

		t2 = perf_counter()		

		x = lin.inv(A)				

		t3 = perf_counter()				

		dt1 = t2 - t1
		dt2 = t3 - t2

		print (f"Para N = {N} :")
		print (f"Tiempo ensamblaje = {dt1} s")
		print (f"Tiempo solución = {dt2} s")
		print ("")

		txt.write(f"{N} {dt1} {dt2}\n")

	txt.close()

