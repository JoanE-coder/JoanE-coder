# Inventario Inicio

nombre = input("Ingrese nombre del producto: ")

## Funciones de precio
while True:
    try:
        precio = float(input("Precio Del Producto: "))
        break
    except:
        print("ERROR: ingrese el precio correctamente ")

## Funcion de cantidad
while True:

    try:
        cantidad = int(input("Ingrece la cantidad deseada: "))
        break
    except:
        print("ERROR: ingrese la cantidad correctamente ")

## Funcion de costo total   
costo_total = precio * cantidad

## Resumen de los productos
print("\n === RESIUMEN DEL PRODUCTO ===\n")
print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad} | Total: {costo_total} ") 
