import numpy as np
from time import perf_counter

def matriz_laplaciana(N, t):
	return np.eye(N, dtype =t) - np.eye(N,N,1,dtype=t)

Ns = [1, 5, 10, 15, 20, 30, 40, 50, 60, 70, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000, 10000]

corridas = 10

for i in range (corridas):

	txt = open(f"Rendimiento{i+1}_matriz_llena.txt", "w")

	for N in Ns:
		
		t1 = perf_counter()	
		
		A = matriz_laplaciana(N, t = np.float64)
		B = matriz_laplaciana(N, t = np.float64)		

		t2 = perf_counter()		

		C = A@B						

		t3 = perf_counter()				

		dt1 = t2 - t1
		dt2 = t3 - t2

		print (f"Para N = {N} :")
		print (f"Tiempo ensamblaje = {dt1} s")
		print (f"Tiempo solución = {dt2} s")
		print ("")

		txt.write(f"{N} {dt1} {dt2}\n")

	txt.close()


