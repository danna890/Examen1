from modulos.modulos_consola import mostrar_menu_leer, mostrar_menu_principal
from data.almacenamiento import RUTAS

def leer():
    try:
        with open('ingredientes.txt', 'r') as archivo:
            ingredientes = archivo.readlines()
            ingredientes = [ingrediente.strip() for ingrediente in ingredientes]
            return ingredientes
    except FileNotFoundError:
        print("El archivo de ingredientes no existe.")
        return []
    except Exception as e:
        print(f"Error al leer los ingredientes: {e}")
        return []