import json
import os

RUTAS = {
    "ingredientes": "data/ingredientes.json",
    "chef": "data/chef.json",
    "categorias": "data/categorias.json",
    "hamburguesas": "data/hamurguesas.json"
}


def crear(tipo: str):
    archivo = RUTAS.get(tipo)
    if not archivo:
        print("Tipo no válido.")
        return
    if not os.path.exists(archivo):
        with open(archivo, 'w') as f:
            pass
        
def leer(tipo: str, datos: list):
    archivo = RUTAS.get(tipo)
    if archivo and os.path.exists(archivo):
        try:
            with open(archivo, 'r') as f:
                for linea in f:
                    datos.append(json.loads(linea.strip()))
        except Exception as e:
            print(f"Error al leer el archivo {tipo}: {e}")


def leer(tipo = str):
    try:
        with open(RUTAS["ingredientes"], 'r') as archivo:
            ingredientes = archivo.readlines()
            ingredientes = [ingrediente.strip() for ingrediente in ingredientes]
            return ingredientes
    except FileNotFoundError:
        print("El archivo de ingredientes no existe.")
        return []
    except Exception as e:
        print(f"Error al leer los ingredientes: {e}")
        return []

def eliminar():
    opcion = input("¿Está seguro de que desea eliminar el ingrediente? (si/no): ")
    if opcion.lower() == 'si':
        try:
            with open(RUTAS["ingredientes"], 'r') as archivo:
                ingredientes = archivo.readlines()
            with open(RUTAS["ingredientes"], 'w') as archivo:
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
        
def actualizar():
    id_ingrediente = input("Ingrese el ID del ingrediente a actualizar: ")
    nuevo_nombre = input("Ingrese el nuevo nombre del ingrediente: ")
    try:
        with open(RUTAS["ingredientes"], 'r') as archivo:
            ingredientes = archivo.readlines()
        with open(RUTAS["ingredientes"], 'w') as archivo:
            for ingrediente in ingredientes:
                if ingrediente.strip() == id_ingrediente:
                    archivo.write(nuevo_nombre + '\n')
                else:
                    archivo.write(ingrediente)
        print("Ingrediente actualizado correctamente.")
    except FileNotFoundError:
        print("El archivo de ingredientes no existe.")
    except Exception as e:
        print(f"Error al actualizar el ingrediente: {e}")
        
