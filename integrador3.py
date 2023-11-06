# Parte 3
""""
Iniciar con un número en 0, leer la tecla `n` 
del teclado en un bucle, por cada presionada,
 borrar la terminal y e imprimir el nuevo número
   hasta el número 50.
"""

import os
import keyboard

# Funcion para borrar la terminal 
def clear_terminal():
    os.system('cls')

#Funcion imprimir el numero actual 
def print_number(number):
    print(f'Numero actual: {number}')

number= 0

while number <50:
    clear_terminal()
    print_number(number)
    key = keyboard.read_event()
    if key.name == 'n':    
        number += 1
print("Se ha alcanzado el numero 50")

