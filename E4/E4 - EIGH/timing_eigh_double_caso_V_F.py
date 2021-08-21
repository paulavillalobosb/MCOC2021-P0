from numpy import float32, float64
from time import perf_counter
from scipy.linalg import eigh
from laplaciana import laplaciana
 
Ns = [2, 5, 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100, 150, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1500, 2000]

corridas = 10

txt = open(f"Rendimiento eigh_double_caso_V_F.txt", "w")

for N in Ns:
	
	contdt = 0
	
	for i in range (corridas):

		A = laplaciana(N, dtpe = float64)			# float64 -> double

		t1 = perf_counter()			# Tiempo inicial 

		w,h = eigh(A, driver = 'evx', overwrite_a = False)		# Valores y vectores propios			

		t2 = perf_counter()			# Tiempo final 

		dt = t2 - t1
		
		contdt = contdt + dt

		print (f"Para N = {N} :")
		print (f"Tiempo transcurrido = {dt} s")
		print (f"Contador dt = {contdt} s")
		print ("")

	dtfinal = contdt/corridas

	txt.write(f"{N} {dtfinal} \n")

txt.close()

