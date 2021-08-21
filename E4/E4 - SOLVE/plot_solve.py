import matplotlib.pylab as plt

Ns = []
dts = []

casos = 7  				# Cantidad de casos

#----------------------------------------------------------------------------
#							Lectura archivos TXT 
#----------------------------------------------------------------------------

for i in range (casos):

	txt = open(f"Rendimiento solve_caso_{i+1}.txt", "r")

	for line in txt:
			
		sep = line.split()
		
		N = int(sep[0])
		dt = float(sep[1])
		
		Ns.append(N)
		dts.append(dt)


	txt.close()

contN = Ns.__len__()
n = int(contN/casos)      

#----------------------------------------------------------------------------
#								  Gráficos
#----------------------------------------------------------------------------

plt.figure(1)

# Grafico tiempo transcurrido

plt.subplot(1,1,1)

xlt = [10, 20, 50, 100, 200, 500, 1000, 5000, 1000, 2000, 10000]				# Values eje x
yvt = [0.0001, 0.001, 0.01, 0.1, 1, 10, 60, 600]									# Values eje y

ylt = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]		# Labels eje y

plt.title("Desempeño SOLVE (Solución Sistema de Ecuaciones)")
plt.ylabel("Tiempo transcurrido")
plt.xlabel("Tamaño matriz N")
plt.grid(False)

tiposolucion = ["inv. A", "solve default", "assume_a=pos", "assume_a=sym", "overwrite_a=True", "overwrite_b=True", "overwrite_a/b=True"]

for i in range (casos):

	plt.loglog(Ns[i*n:(i+1)*n],dts[i*n:(i+1)*n], label= (f"Caso {tiposolucion[i]}"), linewidth = 1.0)
	plt.scatter(Ns[i*n:(i+1)*n],dts[i*n:(i+1)*n])
	plt.legend(loc="upper left", fontsize = 8)

plt.xticks(xlt, xlt)			
plt.yticks(yvt, ylt)

plt.show()

