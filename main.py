from modulos.modulos_consola import mostrar_menu_principal, mostrar_menu_crear, mostrar_menu_eliminar, mostrar_menu_leer, mostrar_menu_actualizar
from data.almacenamiento import RUTAS
from Crud import eliminar, actualizar, crear, leer
import reportes

def main():    
    while True:
        mostrar_menu_principal()
        opcion = input("Selecciona una opción (1-8): ").strip()
        if opcion == '1':
            mostrar_menu_principal()
        elif opcion == '2':
            mostrar_menu_crear()
        elif opcion == '3':
            mostrar_menu_eliminar()
        elif opcion == '4':
            mostrar_menu_leer()
        elif opcion == '5':
            mostrar_menu_actualizar()
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 8.")

if __name__ == "__main__":
        main()
        

