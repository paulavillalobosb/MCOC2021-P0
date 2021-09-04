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


# Matrices dispersas y complejidad computacional

En esta entrega se analizó el tiempo de ensamblaje, solución MATMUL y la complejidad computacional para matrices llenas y dispersas. 

* Matrices Llenas

En primer lugar, se graficó el tiempo de ensamblaje y solución de multiplicacion de dos matrices llenas de tamaños N entre 1 y 10.000. Para este caso se utilizaron dos matrices laplacianas creadas a partir de la siguiente función:

```python
def matriz_laplaciana(N, t):
 return np.eye(N, dtype =t) - np.eye(N,N,1,dtype=t)
 ```

En este caso se desarrolló una función en donde se pide el tamaño de la matriz deseada y el tipo de dato a utilizar (en este caso _double/float64_) y utilizando la función _eye_ de la libreria _numpy_ retorna una matriz laplaciana. Con esta función se desarrollaron y luego multiplicaron dos matrices, midiendo los tiempos transcurridos, generando el siguiente gráfico:

![llena](https://user-images.githubusercontent.com/88356859/131050147-55cac61b-cde8-4a66-9700-f7a2dbe23a3d.png)

En este grafico se puede observar que el tiempo de ensamblaje sigue un comportamiento de complejidad matricial de orden 2 _O(H^2)_ y el tiempo de solución un comportamiento de complejidad matricial de orden 3 _O(H^3)_.


* Matrices Dispersas

Por otro lado, se graficó el tiempo de ensamblaje y solución de multiplicacion de dos matrices dispersas de tamaños N entre 1 y 20.000.000. 

Para este caso se utilizaron dos matrices laplacianas creadas a partir de la siguiente función:

```python
def matriz_laplaciana(N, t):
	return sparse.eye(N, dtype =t) - sparse.eye(N,N,1,dtype=t)
```

En este caso, se utilizó la libreria scipy.sparse para crear las matrices requeridas, de esta manera se optimizó el tiempo de ensamblaje. 

Luego, se definieron como matrices de filas dispersas comprimidas _csr.matrix()_ en donde fila a fila se almacenan los datos distintos de cero, para lograr optimizar el tiempo de solución. Finalmente se multiplicaron las matrices y se graficaron los tiempos transcurridos:

![dispersa 20 mill (max)](https://user-images.githubusercontent.com/88356859/131051187-98121a55-ec48-4890-8572-0d1e43923cd9.png)

En este grafico se puede observar que utilizando la libreria scipy.sparse y matrices dispersas se logro disminuir considerablemnte los tiempos de desarrollo, llegando a utilizar matrices de tamaño del orden de 20.000.000. Es posible notar que los tiempos en un inicio se comportan de manera constante hasta las matrices de tamaño N=10.000 aproximadamente, y luego siguen un comportamiento de orden 1 _O(H^1)_.


Finalmente, es evidente notar que las matrices dispersas optimizaron de manera considerable su tiempo de ensamblaje y solución, esto se puede observar al comparar en ambos gráficos los tiempos para matrices entre N=1 y N=10.000, en donde en el primer caso, se siguen comportamientos de ordenes entre 2 y 3 llegando a superar los 10 segundos de ejecusión; mientras que en el segundo caso, se mantiene constante en un intervalo de tiempo entre 0.1 y 10 milisegundos, además se pudo seguir aumentando exponencialmente el tamaño de las matrices, cosa que no fue posible para el caso de matrices llenas. 


# Matrices dispersas y complejidad computacional Parte 2

* Complejidad algoritmica de SOLVE

![solve dispersa](https://user-images.githubusercontent.com/88356859/132078999-06891716-1028-426b-b2a6-f37ddddac4fa.png)
![solve llena](https://user-images.githubusercontent.com/88356859/132079000-e8957de0-e62c-445c-9376-15120f6ff5f4.png)


* Complejidad algoritmica de INV

![inv dispersa](https://user-images.githubusercontent.com/88356859/132078946-e614ee9d-20c5-4f23-bad3-32f6cb2445fd.png)
![inv llena](https://user-images.githubusercontent.com/88356859/132078951-66f92210-03d1-4945-b7ad-6ad494b46058.png)

* Codigo de ensamblaje Matriz Laplaciana

```python
def laplaciana(N, t):
	d = sp.eye(N,N,1,dtype=t)
	return 2*sp.eye(N, dtype =t) - d - d.T
```



1. Diferencia en el comportamiento de los algoritmos en el caso de matrices llenas y dispersas.
2. ¿Cuál parece la complejidad asintotica para el ensamblado y solución en ambos casos?
3. ¿Como afecta el tamaño de las matrices al comportamiento aparente?
4. ¿Que tan estables son las corridas?





