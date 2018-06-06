# -*- coding: utf-8 -*-
#
#
# Esto es un comentario

#Esto es un Heredoc

"""
Esto es el Here-doc
"""

mensaje = '''
Esto tambien es un comentario o heredoc
Esto es otra linea
'''

# cadenas de caracteres (strings)

nombre= "César"
apellido = 'García' #Esta es la preferida

nombre_completo = nombre + ' ' + apellido
print(nombre_completo)

print(len(nombre))
#Funcion

print(nombre.upper())
print(nombre.lower())
print(nombre.replace('é', 'x'))


#Formateo de cadenas
mensaje_de_saludo = 'Hola soy  %s' % nombre
print(mensaje_de_saludo)

nombre_dado = input("Dime tu nombre: ")

longitud_nombre = len(nombre_dado)

print('tu nombre tiene  %s letras'  % longitud_nombre)
