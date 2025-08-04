"""
gestion de ingredientes 
desperdicios de productos no utilizados por la chef
falta de un sistema de gestion de inventario

PROBLEMA CRITICO GESTION DE INVENTARIO
PLANIFICACION DE PEDIDOS MAS PRECISA

Registro y Gestión de Ingredientes:

Operaciones CRUD para crear, leer, actualizar y eliminar ingredientes de la base de datos.

"""

from modulos import mostrar_menu_principal, mostrar_menu_actualizar, mostrar_menu_crear, mostrar_menu_eliminar, mostrar_menu_leer
from data.almacenamiento import RUTAS
from Crud import eliminar
from Crud import actualizar
from Crud import crear
from Crud import leer

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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            mostrar_menu_leer()
            opcion_leer = input("Seleccione una opción: ")
            if opcion_leer == '1':
                ingredientes = leer.leer()
                print("Ingredientes:", ingredientes)
            elif opcion_leer == '2':
                print("Funcionalidad de leer hamburguesas no implementada.")
            elif opcion_leer == '3':
                print("Funcionalidad de leer chef no implementada.")
            elif opcion_leer == '4':
                print("Funcionalidad de leer categoría no implementada.")
            elif opcion_leer == '5':
                continue
            else:
                print("Opción no válida.")
        
        elif opcion == '2':
            mostrar_menu_crear()
            opcion_crear = input("Seleccione una opción: ")
            if opcion_crear == '1':
                crear.crear()
            elif opcion_crear == '2':
                print("Funcionalidad de crear hamburguesa no implementada.")
            elif opcion_crear == '3':
                print("Funcionalidad de crear chef no implementada.")
            elif opcion_crear == '4':
                print("Funcionalidad de crear categoría no implementada.")
            elif opcion_crear == '5':
                continue
            else:
                print("Opción no válida.")
        
        elif opcion == '3':
            mostrar_menu_actualizar()
            opcion_actualizar = input("Seleccione una opción: ")
            if opcion_actualizar == '1':
                actualizar.actualizar()
            elif opcion_actualizar == '2':
                print("Funcionalidad de actualizar hamburguesa no implementada.")
            elif opcion_actualizar == '3':
                print("Funcionalidad de actualizar chef no implementada.")
            elif opcion_actualizar == '4':
                print("Funcionalidad de actualizar categoría no implementada.")
            elif opcion_actualizar == '5':
                continue
            else:
                print("Opción no válida.")
        
        elif opcion == '4':
            mostrar_menu_eliminar()
            opcion_eliminar = input("Seleccione una opción: ")
            if opcion_eliminar == '1':
                eliminar.eliminar_ingrediente()
            elif opcion_eliminar == '2':
                print("Funcionalidad de eliminar hamburguesa no implementada.")
            elif opcion_eliminar == '3':
                print("Funcionalidad de eliminar chef no implementada.")
            elif opcion_eliminar == '4':
                print("Funcionalidad de eliminar categoría no implementada.")
            elif opcion_eliminar == '5':
                continue
            else:
                print("Opción no válida.")