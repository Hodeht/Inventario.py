inventario = {}
#Modulo principal
def bienvenida():
    """Muestra un mensaje de bienvenida al sistema."""
    print("=====================================")
    print("  BIENVENIDO AL SISTEMA DE INVENTARIO")
    print("=====================================")

def agregar_producto(nombre, cantidad):
    """Agrega un producto al inventario (Paso por valor)."""
    
    if nombre in inventario:
        inventario[nombre] += cantidad
    else:
        inventario[nombre] = cantidad
    print(f" Producto '{nombre}' agregado/actualizado con {cantidad} unidades.")

def mostrar_inventario():
    """Muestra todos los productos en el inventario."""
    print("\n INVENTARIO ACTUAL ")
    if not inventario:
        print(" El inventario está vacío.")
    else:
        for producto, cantidad in inventario.items():
            print(f"- {producto}: {cantidad} unidades")
    print("-------------------------------")

def actualizar_producto(diccionario):
    """
    Actualiza un producto del inventario (Paso por referencia).
    Aquí modificamos directamente el diccionario recibido.
    """
    producto = input("Ingrese el nombre del producto a actualizar: ")
    if producto in diccionario:
        nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
        diccionario[producto] = nueva_cantidad  
        print(f" Producto '{producto}' actualizado a {nueva_cantidad} unidades.")
    else:
        print(" El producto no existe en el inventario.")


def menu():
    """Menú principal del sistema de inventario."""
    while True:
        print("\n=== MENÚ DE OPCIONES ===")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Actualizar producto")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad: "))
            agregar_producto(nombre, cantidad)  

        elif opcion == "2":
            mostrar_inventario()

        elif opcion == "3":
            actualizar_producto(inventario)  
        

        elif opcion == "4":
            print(" Gracias por usar el sistema de inventario. ¡Hasta luego!")
            break
        else:
            print("Opción inválida, intente de nuevo.")

bienvenida()

menu()
