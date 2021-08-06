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



