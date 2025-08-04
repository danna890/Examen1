from modulos.modulos_consola import mostrar_menu_eliminar, mostrar_menu_principal
from data.almacenamiento import RUTAS

def eliminar():
    opcion = input("¿Está seguro de que desea eliminar el ingrediente? (si/no): ")
    if opcion.lower() == 'si':
        try:
            with open('ingredientes.txt', 'r') as archivo:
                ingredientes = archivo.readlines()
            with open('ingredientes.txt', 'w') as archivo:
                for ingrediente in ingredientes:
                    if ingrediente.strip() != 'ingrediente_a_eliminar':
                        archivo.write(ingrediente)
            print("Ingrediente eliminado correctamente.")
        except FileNotFoundError:
            print("El archivo de ingredientes no existe.")
        except Exception as e:
            print(f"Error al eliminar el ingrediente: {e}")
    else:
        print("Operación de eliminación cancelada.")
    pass

    while True:
        opcion = input("¿Desea eliminar otro ingrediente? (si/no): ")
        if opcion.lower() == 'si':
            eliminar()
            break
        elif opcion.lower() == 'no':
            print("Operación de eliminación finalizada.")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")
        