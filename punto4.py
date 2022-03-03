# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 20:10:50 2022

@author: dbenavid5
"""

taller1 = float(input('Ingrese la nota del taller 1: \n'))
taller2 = float(input('Ingrese la nota del taller 2: \n'))
taller3 = float(input('Ingrese la nota del taller 3: \n'))
examen = float(input('Ingrese la nota del examen: \n'))
proyecto = float(input('Ingrese la nota del proyecto: \n'))
notaTalleres = ((taller1 + taller2 + taller3)/3) *0.5
notaExamen = examen * 0.3
NotaProyecto = proyecto * 0.2
NotaFinal = NotaProyecto + notaExamen + notaTalleres
print(f"La nota final es: ${NotaFinal:,}\n")