#!/usr/bin/env python

'''
Divisió. Calcula el quocient i el residu de dos nombres enters
Insitut Icària
Programació - 1r Batxillerat - Curs 2025 - 26
Demana dos nombres enters, calcula el quocient i residu,
i els mostra per pantalla
'''

__author__ = "Lorenzo Flores"
__contact__ = "lflores@instituticaria.cat"
__date__ = "2025/10/17"

dividend = int(input())
divisor = int(input())
quocient = dividend // divisor
residu = dividend % divisor

print(f"Divisió: {dividend}/{divisor}")
print(f"Quocient: {quocient}")
print(f"Residu: {residu}")
