from numpy import ones, float32
from time import perf_counter
from scipy.linalg import solve
from laplaciana import laplaciana
 
Ns = [1, 5, 10, 15, 20, 30, 40, 50, 60, 70, 80, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000]

corridas = 10

txt = open(f"Rendimiento solve_caso_3.txt", "w")

for N in Ns:
	
	contdt = 0
	
	for i in range (corridas):

		A = laplaciana(N, dtpe = float32)
		b = ones(N)

		t1 = perf_counter()							# Tiempo inicial 

		x = solve(A,b,assume_a='pos')				# Solucion sistema de ecuaciones		

		t2 = perf_counter()							# Tiempo final 

		dt = t2 - t1
		
		contdt = contdt + dt

		print (f"Para N = {N} :")
		print (f"Tiempo transcurrido = {dt} s")
		print (f"Contador dt = {contdt} s")
		print ("")

	dtfinal = contdt/corridas

	txt.write(f"{N} {dtfinal} \n")

txt.close()



