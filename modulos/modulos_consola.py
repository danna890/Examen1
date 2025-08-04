import json
import os
from typing import List, Dict
from data import almacenamiento


def mostrar_menu_principal():
    print("""
    ===========================================
            GESTION DE INVENTARIOS
    ===========================================
    1. Ver Ingredientes
    2. Ver Hamburguesas
    3. Ver Chef
    4. Ver Categorías
    5. Salir
    ===========================================
    """)
    
def mostrar_menu_actualizar():
    print("""
    ===========================================
            ACTUALIZAR REGISTROS
    ===========================================
    1. Actualizar Ingrediente
    2. Actualizar Hamburguesa
    3. Actualizar Chef
    4. Actualizar Categoría
    5. Volver al Menú Principal
    ===========================================
    """)

def mostrar_menu_eliminar():
    print("""
    ===========================================
            ELIMINAR REGISTROS
    ===========================================
    1. Eliminar Ingrediente
    2. Eliminar Hamburguesa
    3. Eliminar Chef
    4. Eliminar Categoría
    5. Volver al Menú Principal
    ===========================================
    """)

def mostrar_menu_leer():
    print("""
    ===========================================
            LEER REGISTROS
    ===========================================
    1. Leer Ingredientes
    2. Leer Hamburguesas
    3. Leer Chef
    4. Leer Categoría
    5. Volver al Menú Principal
    ===========================================
    """)
    
def mostrar_menu_crear():
    print("""
    ===========================================
            CREAR NUEVOS REGISTROS
    ===========================================
    1. Crear Ingrediente
    2. Crear Hamburguesa
    3. Crear Chef
    4. Crear Categoría
    5. Volver al Menú Principal
    ===========================================
    """)
    
def mostrar_menu_actualizar(elemtos: List[Dict], tipo: str = ''):
    if not elemtos:
        print(f"No hay {tipo} para actualizar." if tipo else "No hay elementos para actualizar.")
        return
    
    print(f"\n{'='*30}")
    print(f"        ACTUALIZAR {tipo.upper() if tipo else 'ELEMENTOS'}")
    print(f"{'='*30}")
    
    for i, elemento in enumerate(elemtos, 1):
        print(f"{i}. {elemento['titulo']}")
    
    indice = int(input("Seleccione el número del elemento a actualizar: ")) - 1
    if 0 <= indice < len(elemtos):
        nuevo_dato = input("Ingrese el nuevo dato: ")
        elemtos[indice]['titulo'] = nuevo_dato
        print("Elemento actualizado correctamente.")
    else:
        print("Índice no válido.")
        


