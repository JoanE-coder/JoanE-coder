# Inventario Inicio

nombre = input("Ingrese nombre del producto: ")

## Funciones de precio
while True:
    try:
        precio = float(input("Precio Del Producto: "))
        break
    except:
        print("ERROR: ingrese el precio correctamente ")


