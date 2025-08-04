from modulos import mostrar_menu_crear, mostrar_menu_principal
from data.almacenamiento import RUTAS

def crear():
    ingrediente = input("Ingrese el nombre del ingrediente a agregar: ")
    try:
        with open('ingredientes.txt', 'a') as archivo:
            archivo.write(ingrediente + '\n')
        print("Ingrediente agregado correctamente.")
    except Exception as e:
        print(f"Error al agregar el ingrediente: {e}")
    pass
