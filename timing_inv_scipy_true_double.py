from time import perf_counter
from numpy import zeros
from numpy import half, single, double, longdouble
from scipy.linalg import inv
from laplaciana import laplaciana

Ns = [1, 5, 10, 15, 20, 30, 40, 50, 60, 70, 80, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000]
dts_inv = []
mems = []

corridas = 10

for i in range (corridas):

	txt = open(f"Rendimiento{i+1} scipy_true_double.txt", "w")

	for N in Ns:

		t1 = perf_counter()

		A = laplaciana(N, dtype = double)

		t2 = perf_counter()

		Am1 = inv(A, overwrite_a = True)

		t3 = perf_counter()

		dt_ensamblaje = t2 - t1			# Tiempo que se demora en armar la matriz
		dt_inversion = t3 - t2			# Tiempo que se demora en invertir la matriz

		mem = A.nbytes + Am1.nbytes

		print (f"Para N = {N} :")
		print (f"Tiempo ensamblaje: {dt_ensamblaje} s")
		print (f"Tiempo inversion: {dt_inversion} s")
		print (f"Uso memoria: {mem} bytes")
		print ("")

		dts_inv.append(dt_inversion)

		mems.append(mem)


		txt.write(f"{N} {dt_inversion} {mem}\n")


	txt.close()
