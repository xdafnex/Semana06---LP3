# -*- coding: utf-8 -*-
"""
Created on Mon May  6 15:08:05 2024

@author: Dell
"""
import camelcase

nombre = "dafne ayelen huertas gonzales"

print(nombre.upper())
print(nombre.title())

#Creamos un objeto llamado cam
cam = camelcase.CamelCase()
print("Con camelcase....")

# imprimimos el nombre en formato título
# utilizamos camelcase
print(cam.hump(nombre))

# Para resolver el problema
# creamos otro objeto llamado cam2
# al definir el objeto, incluimos los argumentos
# 'flor' y 'león' 
cam2 = camelcase.CamelCase('dafne','gonzales')
print(cam2.hump(nombre))
