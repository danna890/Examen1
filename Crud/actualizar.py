
from modulos.modulos_consola import mostrar_menu_actualizar, mostrar_menu_principal
from data.almacenamiento import RUTAS


def actualizar():
    try:
        with open('ingredientes.txt', 'r') as archivo:
            ingredientes = archivo.readlines()
        
        print("Ingredientes actuales:")
        for i, ingrediente in enumerate(ingredientes, start=1):
            print(f"{i}. {ingrediente.strip()}")
        
        indice = int(input("Ingrese el número del ingrediente a actualizar: ")) - 1
        if 0 <= indice < len(ingredientes):
            nuevo_ingrediente = input("Ingrese el nuevo nombre del ingrediente: ")
            ingredientes[indice] = nuevo_ingrediente + '\n'
            
            with open('ingredientes.txt', 'w') as archivo:
                archivo.writelines(ingredientes)
            
            print("Ingrediente actualizado correctamente.")
        else:
            print("Índice no válido.")
    except Exception as e:
        print(f"Error al actualizar el ingrediente: {e}")
    pass

    while True:
        opcion = input("¿Desea actualizar otro ingrediente? (si/no): ")
        if opcion.lower() == 'si':
            actualizar()
            break
        elif opcion.lower() == 'no':
            print("Operación de actualización finalizada.")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")