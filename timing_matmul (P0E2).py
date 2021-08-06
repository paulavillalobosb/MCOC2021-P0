from numpy import zeros, float16, float32, float64
from time import perf_counter


Ns = [1, 5, 10, 15, 20, 30, 40, 50, 60, 70, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000, 10000]
dts = []
mems = []

corridas = 10

for i in range (corridas):

	txt = open(f"Rendimiento{i+1}.txt", "w")

	for N in Ns:

		A = zeros((N, N)) +1		# Matriz A de tamaño NxN
		B = zeros((N, N)) +2		# Matriz B de tamaño NxN

		t1 = perf_counter()			# Tiempo inicial multiplicacion de matrices

		C = A@B						# @ : multiplicador de matrices (matmul) / * : multiplicacion de arreglos

		t2 = perf_counter()			# Tiempo final multiplicacion de matrices

		mem = A.nbytes + B.nbytes + C.nbytes

		dt = t2 - t1

		dts.append(dt)

		mems.append(mem)

		print (f"Para N = {N} :")
		print (f"Tiempo transcurrido = {dt} s")
		print (f"Uso de memoria = {mem} bytes")
		print ("")

		txt.write(f"{N} {dt} {mem}\n")


	txt.close()

	



















