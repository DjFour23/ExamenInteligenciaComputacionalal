# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 19:59:46 2022

@author: dbenavid5
"""

sueldoVendedor = int(input('Ingrese el sueldo base del vendedor: \n'))
totalenVentas = int(input('Valor obtenido en ventas: \n'))
sueldoEnVentas= totalenVentas * 0.15
sueldoTotal = sueldoVendedor + sueldoEnVentas

print(f"El vendedor gano ${sueldoEnVentas:,} en comisiones\n")
print(f"Al vendedor se le ha de pagar ${sueldoTotal:,} en total\n")

