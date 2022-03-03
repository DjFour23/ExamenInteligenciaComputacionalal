# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 20:19:51 2022

@author: dbenavid5
"""

aRedes = int(input('Ingrese la cantidad de estudiantes de redes: \n'))
aCotabilidad = int(input('Ingrese la cantidad de estudiantes de Contabilidad: \n'))
aDiseño = int(input('Ingrese la cantidad de estudiantes de Diseño: \n'))
totalAlumnos = aRedes + aCotabilidad + aDiseño
pRedes = (aRedes/totalAlumnos) * 100
pCotabilidad = (aCotabilidad/totalAlumnos) * 100
pDiseño = (aDiseño/totalAlumnos) * 100
print(f"El porcentaje de estudiantes en redes es: {pRedes}%\n")
print(f"El porcentaje de estudiantes en redes es: {pCotabilidad}%\n")
print(f"El porcentaje de estudiantes en redes es: {pDiseño}%\n")