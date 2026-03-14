# INVENTARIO - Historia de Usuario

## Guia paso a paso para ejecutar el programa en terminal windows

### **1**. Instalar Python

Primero necesitas intalar Pytioh en tu computadora.

* Ve a la página oficial:
    https://www.python.org/downloads/
* Descarga la versión mas reciente de Python
* Ejecuta el intalador.
* **MUY IMPORTANTE** antes de hacer clic en intalar, marca la casilla
* Luego haz clic en **Install Now**
Cuando termine la intalación, Python quedara lsito para usar.

### **2** Crea el archivo del programa

Ahora debes guardar tu código en un archivo.
* Abre **bloc de nota**.
* Copia tu código de python.
* Guarda el archivo con un nombre como:

``` 
inventario.py

```
**MUY IMPORTANTE**:
Debe terminar en **.py**

### **3**. Abrir la carpeta donde está el archivo

supongamos que el archivo esta en Documentos.
* Ve a la carpeta donde guardadte el archivo.
* Haz clic en la barra de direccion de la carpeta.
* Escribe:

```
cmd

```
* Presiona **Enter**.
Se abrira la terminal directamente en esa carpeta.

### **4**. Ejecuta el programa
En la terinal escribe:

```
python inventario.py

```

### Usar el programa

El programa empezara a pedir datos, por ejemplo

```
Ingrese nombre del producto:

```
Escribe el nombre y presionas **Enter**.

Luego te pedira:

```
Precio del producto:

```
y despues:

```
Cantidad deseada:

```
El programa calculara el total automatico

## Diagrama de flojo

![alt text](<Diagrama de flujo.png>)

Este programa en **Python** permite registrar la informacion básica de un producto u calcular el costo total de una compra.

---

el sisema solicita al usiario:

* Nombre del producto
* Precio del producto
* Cantidad de unidades

luego calcula automaticamente el ¨**costo total** multiplicando el prtecio por la cantidad u muestrea un **resumen del producto**.

Además, el programa incluye **validación de datos**, evitando que el usuario ingrese valores incorrectos para el precio o la cantidad.

---

## Funcionamiento del Programa

el programa está dividido en **tres fases del principales**:

### **1.** Entrada de datos

El sistema solicita al usuario el **nombre del produto**

```
nombre = input("Ingrese nombre del producto: ")
```
Después pide el **precio del producto**.
Se utiliza un ciclo **while** junto con **try/except** para validar que el usuario ingrese un número decimal válido.

```
while True:
    try:
        precio = float(input("Precio Del Producto: "))
        break
    except:
        print("ERROR: ingrese el precio correctamente ")

```

---

## **2**. Validacion de cantidad

el programa solicita la **cantidad del producto**.

Se utiliza nuevamente **while** con **try/except** para asegurase de que el usuario ingrese un número entero.

```
while True:
    try:
        cantidad = int(input("Ingrece la cantidad deseada: "))
        break
    except:
        print("ERROR: ingrese la cantidad correctamente ")

 ```

 Si el usuario escribe un valor incorrecto ( por ejemplo letras), el programa mostrará un mensaje de error y volverá a pedir el dato.

 ---

 ## **3**. Procesamiento de datos       
 
 Una vez que el programa obtiene los valores correctos, calcula el **costo total**
 
 ```

 costo_total = precio * cantidad

 ```

 La operación consiste en multiplicar:

```

Costo Total = Precio × Cantidad

```

## **4**. Salida de informacion

Finalmente el programa muestra un **resumen del producto registrado**.

```

print("\n === RESIUMEN DEL PRODUCTO ===\n")
print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad} | Total: {costo_total} ")

```

El resultado se verá similar a esto en la consola:

```

=== RESUMEN DEL PRODUCTO ===

Producto: Laptop | Precio: 1500 | Cantidad: 2 | Total: 3000

```

### AUTOR: **Joan Estremor**