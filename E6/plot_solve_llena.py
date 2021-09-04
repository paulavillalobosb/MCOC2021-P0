import matplotlib.pylab as plt

#----------------------------------------------------------------------------
#							Lectura archivos TXT 
#----------------------------------------------------------------------------

Ns = []

dts1 = []
dts2 = []

corridas = 10			

for i in range (corridas):

	txt = open(f"Rendimiento_solve_{i+1}_matriz_llena.txt", "r")

	for line in txt:
			
		sep = line.split()
		
		N = int(sep[0])
		dt1 = float(sep[1])
		dt2 = float(sep[2])
		
		Ns.append(N)
		dts1.append(dt1)
		dts2.append(dt2)

	txt.close()

contN = Ns.__len__()
n = int(contN/corridas)      


#----------------------------------------------------------------------------
#								  Gráficos
#----------------------------------------------------------------------------

plt.figure(1)

# Grafico tiempo ensamblaje

plt.subplot(2,1,1)

xlt = [10, 20, 50, 100, 200, 500, 1000, 5000, 1000, 2000, 10000, 20000, 50000, 100000, 500000, 1000000, 5000000, 10000000, 20000000]				
yvt = [0.0001, 0.001, 0.01, 0.1, 1, 10, 60, 600]									

ylt = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]		

plt.title("Rendimiento SOLVE Matriz Llena")
plt.ylabel("Tiempo Ensamblaje")

for i in range (corridas):
	plt.loglog(Ns[i*n:(i+1)*n],dts1[i*n:(i+1)*n], color = "black", alpha = 0.5, linewidth = 1)
	plt.scatter(Ns[i*n:(i+1)*n],dts1[i*n:(i+1)*n], color = "black", alpha = 0.5, s = 2)
	

orden = [0, 1, 2, 3, 4]

for j in orden:
   
    Nj = []

    for i in Ns:

        Nn = i**j
        Nj.append(Nn)
    
    ajuste = dts1[-1]/Nj[-1]
    Najustado = []

    for k in Nj:
        najustado = k * ajuste
        Najustado.append(najustado)

    plt.loglog(Ns,Najustado,'--', label= (f"O(N^{j})"), linewidth = 0.75) 

plt.legend(loc="upper left", fontsize = 8)	
plt.ylim(0.000001,600)
plt.xticks(xlt, [])			
plt.yticks(yvt, ylt)


# Grafico tiempo solucion

plt.subplot(2,1,2)

xlm = [10, 20, 50, 100, 200, 500, 1000, 5000, 1000, 2000, 10000, 20000, 50000, 100000, 500000, 1000000, 5000000, 10000000, 20000000]				
yvm = [0.0001, 0.001, 0.01, 0.1, 1, 10, 60, 600]								

ylm = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]			

plt.ylabel("Tiempo Solución")
plt.xlabel("Tamaño Matriz N")

for i in range(corridas):
	plt.loglog(Ns[i*n:(i+1)*n],dts2[i*n:(i+1)*n], color = "black", alpha = 0.5, linewidth = 1) 
	plt.scatter(Ns[i*n:(i+1)*n],dts2[i*n:(i+1)*n], color = "black", alpha = 0.5, s = 2) 
	

orden = [0, 1, 2, 3, 4]

for j in orden:
   
    Nj = []

    for i in Ns:

        Nn = i**j
        Nj.append(Nn)

    ajuste = dts2[-1]/Nj[-1]
    Najustado = []

    for k in Nj:
        najustado = k * ajuste
        Najustado.append(najustado)

    plt.loglog(Ns,Najustado,'--', label= (f"O(N^{j})"), linewidth = 0.75) 

plt.legend(loc="upper left", fontsize = 8)	

plt.ylim(0.000001,600)
plt.xticks(xlm, xlm, rotation = 45)
plt.yticks(yvm, ylm)

plt.show()

