import matplotlib.pylab as plt

Ns = []
dts = []

nombretxt = ["I", "II_F", "II_T", "III_F", "III_T", "IV_F", "IV_T", "V_F", "V_T"]

casos = 9

#----------------------------------------------------------------------------
#							Lectura archivos TXT 
#----------------------------------------------------------------------------

for i in nombretxt:

	txt = open(f"Rendimiento eigh_double_caso_{i}.txt", "r")

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

xlt = [10, 20, 50, 100, 200, 500, 1000, 5000, 1000, 2000, 5000]					# Values eje x
yvt = [0.0001, 0.001, 0.01, 0.1, 1, 10, 60, 600]									# Values eje y

ylt = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]		# Labels eje y

plt.suptitle("Desempeño EIGH (Val. y Vec. Propios)", fontsize = 18)
plt.title("Tipo de dato = double", fontsize = 10)

plt.ylabel("Tiempo transcurrido")
plt.xlabel("Tamaño matriz N")
plt.grid(False)

tipo = ["Eigh default", "driver=ev / overwrite_a=False", "driver=ev / overwrite_a=True", "driver=evd / overwrite_a=False", "driver=evd / overwrite_a=True", "driver=evr / overwrite_a=False", "driver=evr / overwrite_a=True", "driver=evx / overwrite_a=False", "driver=evx / overwrite_a=True"]

for i in range (casos):

	plt.loglog(Ns[i*n:(i+1)*n],dts[i*n:(i+1)*n], label= (f"Caso {tipo[i]}"), linewidth = 1.0)
	plt.scatter(Ns[i*n:(i+1)*n],dts[i*n:(i+1)*n])
	plt.legend(loc="upper left", fontsize = 8)

plt.xticks(xlt, xlt)			
plt.yticks(yvt, ylt)

plt.show()

