# Inicio

inventario = []

# FUNCIONES DE AGREGAR PRODUCTOS

def agregar_producto ():
    # Se le pedira los datos al usuario
    nombre = input("ingrese el nombre del poducto")

# Validamos que el precio sea un numero
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            break
        except:
            print("ERROR: ingrese un numero valido para el precio.")

    # validacion de la cantidad en número enteros
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad del producto: "))
            break
        except:
            print("ERROR: ingrese un numero valido para el precio.")

    # Creamos el diccionario de los productos
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

# lo agregamos a al lista de inventario
    inventario.append(producto)
    print("producto agregado correctamente.")

# FUNCIONES PARA MOSTRAR INVENTARIO
def mostrar_inventario():
    #Verificamos si la lista esta vacia
    if len(inventario) == 0:
        print("El inventario esta vacio.")
    else:
        print("=== INVENTARIO ===")
        # Recorremos la lista con un for
        for producto in inventario:
            print(f"producto:{producto['nombre']} | Precio:{producto['precio']} | Cantidad: {producto['cantidad']}")
            print()

# FUNCIONES PARA CALCULAR ESTADISTICAS
def calcular_estadisticas():
    if len(inventario) == 0:
        print("No hay productos para calcular estadisticas")
        return
    valor_total = 0
    total_productos = 0

    for producto in inventario:
        valor_total += producto["precio"] * producto["cantidad"]
        total_productos += producto["cantidad"]

# Mostramos resultados

    print("\n --- ESTADISTICAS --- ")
    print(f"valor total de inventario: {valor_total}")
    print(f"Cantidad total de producto: {total_productos}\n")

# MENU PRINCIPAL CON BUBLES 

def main():
 while True:

    print("=== MENU PRINCIPAL ===")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. calcular estadisticas")
    print("4. salir")

    opcion = input("SELECIONAR UNA OPCION: ")
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_inventario()
    elif opcion == "3":
        calcular_estadisticas()
    elif opcion == "4":
        print ("Saliendo del programa")
        break
    else:
        print("Opcion invalida")

main()