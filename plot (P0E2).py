import matplotlib.pylab as plt


Ns = []
dts = []
mems = []

corridas = 10  			# Cantidad de veces que se corrió el codigo

ram = 8000000000		# 8 Gb --> 8*10^9 bytes (capacidad computador)


#----------------------------------------------------------------------------
#							Lectura archivos TXT 
#----------------------------------------------------------------------------

for i in range (corridas):

	txt = open(f"Rendimiento{i+1}.txt", "r")

	for line in txt:
			
		sep = line.split()
		
		N = int(sep[0])
		dt = float(sep[1])
		mem = float(sep[2])
		
		Ns.append(N)
		dts.append(dt)
		mems.append(mem)

	txt.close()

contN = Ns.__len__()
n = int(contN/corridas)      

#----------------------------------------------------------------------------
#								  Gráficos
#----------------------------------------------------------------------------

plt.figure(1)

# Grafico tiempo transcurrido

plt.subplot(2,1,1)

xlt = [10, 20, 50, 100, 200, 500, 1000, 5000, 1000, 2000, 10000, 20000]					# Values eje x
yvt = [0.0001, 0.001, 0.01, 0.1, 1, 10, 60, 600]									# Values eje y

ylt = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]		# Labels eje y

plt.title("Rendimiento A@B")
plt.ylabel("Tiempo transcurrido")
plt.grid(True)

for i in range (n):
	plt.loglog(Ns[i*n:(i+1)*n],dts[i*n:(i+1)*n], linewidth = 1.0)
	plt.scatter(Ns[i*n:(i+1)*n],dts[i*n:(i+1)*n])

plt.xticks(xlt, [])			
plt.yticks(yvt, ylt)

# Grafico uso de memoria

plt.subplot(2,1,2)

xlm = [10, 20, 50, 100, 200, 500, 1000, 5000, 1000, 2000, 10000, 20000]							# Values eje x
yvm = [1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, ram, 50000000000]		# Values eje y

ylm = ["1 KB", "10 KB", "100 KB", "1 MB", "10 MB", "100 MB", "1 GB", "8 GB", "50 GB"]		# Labels eje y

plt.ylabel("Uso memoria")
plt.xlabel("Tamaño matriz N")
plt.grid(True)

for i in range(n):
	plt.loglog(Ns[i*n:(i+1)*n],mems[i*n:(i+1)*n], linewidth = 1.0, color = "tab:blue")
	plt.scatter(Ns[i*n:(i+1)*n],mems[i*n:(i+1)*n], color = "tab:blue")

plt.axhline(y = ram, linestyle = "--", color = "black")

plt.xticks(xlm, xlm, rotation = 45)
plt.yticks(yvm, ylm)


plt.show()

