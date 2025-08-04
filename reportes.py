import os
from data.almacenamiento import RUTAS
from modulos.modulos_consola import (    mostrar_menu_principal,
    mostrar_menu_crear,
    mostrar_menu_eliminar,
    mostrar_menu_leer,
    mostrar_menu_actualizar
)

def ingredientes_stock_menor_400(ingredientes):
    return [i for i in ingredientes if i['stock'] < 400]

def hamburguesas_vegetarianas(hamburguesas):
    return [h for h in hamburguesas if h['categoria'] == "Vegetariana"]

def chefs_especialistas_carnes(chefs):
    return [c for c in chefs if c['especialidad'] == "Carnes"]

def aumentar_precio_ingredientes(ingredientes, aumento=1.5):
    for i in ingredientes:
        i['precio'] += aumento

def hamburguesas_preparadas_por(hamburguesas, chef_nombre):
    return [h for h in hamburguesas if h['chef'] == chef_nombre]

def nombre_descripcion_categorias(categorias):
    return [(c['nombre'], c['descripcion']) for c in categorias]

def eliminar_ingredientes_stock_cero(ingredientes):
    return [i for i in ingredientes if i['stock'] > 0]

def agregar_ingrediente_a_hamburguesa(hamburguesas, nombre_hamburguesa, ingrediente):
    for h in hamburguesas:
        if h['nombre'] == nombre_hamburguesa:
            h['ingredientes'].append(ingrediente)

def hamburguesas_con_ingrediente(hamburguesas, ingrediente):
    return [h for h in hamburguesas if ingrediente in h['ingredientes']]

def cambiar_especialidad_chef(chefs, nombre_chef, nueva_especialidad):
    for c in chefs:
        if c['nombre'] == nombre_chef:
            c['especialidad'] = nueva_especialidad

def ingrediente_mas_caro(ingredientes):
    return max(ingredientes, key=lambda i: i['precio'])

def hamburguesas_sin_ingrediente(hamburguesas, ingrediente):
    return [h for h in hamburguesas if ingrediente not in h['ingredientes']]

def incrementar_stock_ingrediente(ingredientes, nombre, cantidad):
    for i in ingredientes:
        if i['nombre'] == nombre:
            i['stock'] += cantidad

def eliminar_hamburguesas_menos_de_n_ingredientes(hamburguesas, n=5):
    return [h for h in hamburguesas if len(h['ingredientes']) >= n]

def agregar_chef(chefs, nombre, especialidad):
    chefs.append({'nombre': nombre, 'especialidad': especialidad})

def hamburguesas_ordenadas_por_precio(hamburguesas):
    return sorted(hamburguesas, key=lambda h: h['precio'])

def ingredientes_precio_entre(ingredientes, minimo, maximo):
    return [i for i in ingredientes if minimo <= i['precio'] <= maximo]

def actualizar_descripcion_ingrediente(ingredientes, nombre, nueva_descripcion):
    for i in ingredientes:
        if i['nombre'] == nombre:
            i['descripcion'] = nueva_descripcion

def hamburguesa_mas_cara_por_especialidad(hamburguesas, chefs, especialidad):
    chefs_gourmet = [c['nombre'] for c in chefs if c['especialidad'] == especialidad]
    hamburguesas_gourmet = [h for h in hamburguesas if h['chef'] in chefs_gourmet]
    return max(hamburguesas_gourmet, key=lambda h: h['precio'], default=None)

def ingredientes_con_numero_de_hamburguesas(ingredientes, hamburguesas):
    resultado = []
    for i in ingredientes:
        count = sum(1 for h in hamburguesas if i['nombre'] in h['ingredientes'])
        resultado.append({'ingrediente': i['nombre'], 'cantidad_hamburguesas': count})
    return resultado