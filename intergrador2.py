# Parte 2
"""
Escribir un programa que corra un bucle infinito leyendo  e imprimiento las teclas 
y sólo terminará cuando se presione la tecla "↑" indicada como UP
"""

import keyboard
def main ():
    print("Presiona la tecla arriba para salir")
    while True:
        event = keyboard.read_event(suppress=True)
        
        if event.event_type == keyboard.KEY_UP and event.name == 'flecha arriba':
            print("programa terminado presionaste la tecla arriba")
            break
        else: 
            print(f'Tecla presionada: {event.name}')
if __name__ == '__main__':
    main()