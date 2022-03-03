# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 19:51:29 2022

@author: dbenavid5
"""

inversion1 = float(input('Ingrese el valor de la primera inversion: \n'))
inversion2 = float(input('Ingrese el valor de la segunda inversion: \n'))
inversion3 = float(input('Ingrese el valor de la tercera inversion: \n'))
valorTotalInv = inversion1 + inversion2 + inversion3;
print(f"El valor total de la inversion es: ${valorTotalInv:,}\n")
pi1 = (inversion1/valorTotalInv) * 100
pi2 = (inversion2/valorTotalInv) * 100
pi3 = (inversion3/valorTotalInv) * 100
print(f"El inversor 1 invirtio ${valorTotalInv:,} lo cual es el {pi1}% de la inversion\n")
print(f"El inversor 2 invirtio ${valorTotalInv:,} lo cual es el {pi2}% de la inversion\n")
print(f"El inversor 3 invirtio ${valorTotalInv:,} lo cual es el {pi3}% de la inversion\n")
