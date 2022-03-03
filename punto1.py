# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 19:47:25 2022

@author: dbenavid5
"""

valorDonacion = int(input('Ingrese el valor de la donacion: \n'))
administracion = valorDonacion * 0.35;
sistemas = administracion * 0.25;
telecomunicaciones = sistemas *0.1;
contabilidad = valorDonacion - administracion - sistemas - telecomunicaciones;

print(f"Del valor de la donacion: ${valorDonacion:,}\n")
print(f"Telecomunicaciones obtuvo: ${telecomunicaciones:,}\n")
print(f"Sistemas obtuvo: ${sistemas:,}\n")
print(f"Administración obtuvo: ${administracion:,}\n")
print(f"Contabilidad obtuvo: ${contabilidad:,}\n")