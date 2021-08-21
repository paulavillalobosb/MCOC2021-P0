# MCOC2021-P0

# Mi computador principal

* Marca/modelo: MacBook Air (13-inch, 2017)
* Tipo: Notebook
* Año adquisición: 2018
* Procesador:
  * Marca/Modelo: Intel Core i5
  * Velocidad Base: 1.8 GHz
  * Velocidad Máxima: 2.9 GHz
  * Numero de núcleos: 2
  * Humero de hilos: 2
  * Arquitectura: 
  * Set de instrucciones: 
* Tamaño de las cachés del procesador
  * L2: 256KB
  * L3: 3000KB
* Memoria 
  * Total: 8 GB
  * Tipo memoria: DDR3
  * Velocidad 1600 MHz
  * Numero de (SO)DIMM: 
* Tarjeta Gráfica
  * Marca / Modelo: Intel HD Graphics 6000
  * Memoria dedicada: 1536 MB
  * Resolución: 1440x900
* Disco 1: 
  * Marca: APPLE SSD SM0128G
  * Tipo: SSD
  * Tamaño: 128 GB
  * Particiones: 1
  * Sistema de archivos: APFS

  
* Dirección MAC de la tarjeta wifi: 64:c7:53:e2:85:ae
* Dirección IP (Interna, del router): 192.168.1.254
* Dirección IP (Externa, del ISP): 192.168.1.10
* Proveedor internet: Gtd

# Desempeño MATMUL

1. ¿Cómo difiere el gráico del profesor/ayudante?

Tal como se pide en el enunciado de la entrega, no observan mayores diferencias en temas de diseño del gráfico ya que fue posible replicar "exactamente" el modelo requirido. Pero se pueden observar algunas diferencias en en el comportamiento del gráfico, si bien poseen un comportamiento similar, se obserbar diferencias en los tiempos y uso de memorias por tamaño de matriz para cada corrida, esto se debe a que los computadores utilizados son de diferentes modelos con diferentes procesadores y capacidad. Se puede notar que en el gráfico entregado por el profesor la linea punteada negra correspondiente a la capacidad es mayor a 10 GB mientras que la linea que representa la capacidad en mi computador corresponde a 8 GB.  

2. ¿A qué se pueden deber las diferencias en cada corrida?

En el primer gráfico, se pueden observar diferencias en el tiempo transcurrido por tamaño de matriz en cada corrida, esto puede deberse a la diferencia de recursos disponibles en cada corrida. 

3. El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser?

La linealidad observada en el gráfico de memoria puede ser debido a que el gráfico representa la capacidad de memoria utilizada para cada matriz, lo cual no va a cambiar en el tiempo. 

4. ¿Qué versión de Python esta usando?

3.9.6

5. ¿Qué versión de numpy está usando? 

1.21.1

6. Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen (screenshot) de su uso de procesador durante alguna corrida para confirmar. 

![CPU](https://user-images.githubusercontent.com/88356859/128527425-0f9582a0-d260-4325-ab55-685a3078a29f.png)

* Gráficos de rendimiento

![Gráficos](https://user-images.githubusercontent.com/88356859/128528301-15768a11-fbf6-4192-8d4d-9181f28919a8.png)


# Desempeño INV

* Gráficos de rendimiento - Numpy

![numpy_single](https://user-images.githubusercontent.com/88356859/129998455-f1e0a20c-fc32-4fa6-b05d-9b772d2b8b55.png)
![numpy_double](https://user-images.githubusercontent.com/88356859/129998450-167f66a8-1428-4063-9257-411f9004d291.png)

   --> En los casos de _half y longdouble_ no fue posible correr el código.


* Graficos de rendimeinto - Scipy/overwrite_a = True

![scipytrue_half](https://user-images.githubusercontent.com/88356859/129998602-32e743de-147a-4a83-818c-a5285de40f7a.png)
![scipytrue_single](https://user-images.githubusercontent.com/88356859/129998608-0f72268c-6d2b-4da0-86ad-75cc071cc8d7.png)
![scipytrue_longdouble](https://user-images.githubusercontent.com/88356859/129998604-02b87097-cfec-4694-bc7f-d1d9bbe46d09.png)
![scipytrue_doublepng](https://user-images.githubusercontent.com/88356859/129998594-2d994f0f-b03a-4a5e-8da5-08b667b8d685.png)


* Graficos de rendimeinto - Scipy/overwrite_a = False

![scipyfalse_half](https://user-images.githubusercontent.com/88356859/129998707-28481f4e-96ba-4833-8aba-8245a10cf2c2.png)
![scipyfalse_single](https://user-images.githubusercontent.com/88356859/129998714-95a1fb4a-0436-4ca3-8ebe-2477fed49b69.png)
![scipyfalse_double](https://user-images.githubusercontent.com/88356859/129998723-7db8003e-6c4d-4a99-8fc8-b27f81dd3235.png)
![scipyfalse_longdouble](https://user-images.githubusercontent.com/88356859/129998731-2dc78ce8-a31c-4f4b-9f5d-d9e1bcf155ac.png)

# Desempeño SOLVE y EIGH

![solve](https://user-images.githubusercontent.com/88356859/130304195-a61bb731-f977-4385-939f-f434f787d404.png)

En el grafico de desempeño del algoritmo SOLVE se puede observar que al asumir la matriz definida positiva (curva color verdeoscuro) el tiempo transcurrido es menor que en el resto de los casos (se puede observar claramente despues de N = 20). Por otro lado, se puede notar que al invertir la matriz y multiplicarla por el vector b el tiempo transcurrido es mayor que para el resto de los casos desde N = 20 aproximadamente tambien se observa que para matrices de N muy pequeños es el caso con el menor tiempo transcurrido. Tambien se puede observar que asmiendo que la matriz es simétrica entre N 20 y 50 tiene un pick de tiempo considerablemnte mayor al resto de los casos. 



![eigh single](https://user-images.githubusercontent.com/88356859/130304052-3594fa9c-8632-47ca-bc11-af4324032f7d.png)
![eigh double](https://user-images.githubusercontent.com/88356859/130304049-c4be5510-fdbf-4469-99a3-ccb43f88f6c5.png)

Luego, en los graficos de desempeño de la funcion EIGH no se observan mayores diferencias entre los tipos de datos single y double. Se puede observar en ambos graficos que los casos "driver = ev" y "driver = evx" con "overwrite_a = True / False" tienen un tiempo transcurrido mayor al resto de los casos. 

