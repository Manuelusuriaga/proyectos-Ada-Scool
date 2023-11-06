import os
from readchar import readkey,key

def cadena_a_laberinto(laberinto):
    #Dividomos la cadena rn lineas
    linea = laberinto.strip().split("\n")
    #creamos matriz vacia
    mapa = []
    # iteramos atravez de las lineas y convertimos cada linea a una lista de caracteres
    for line in linea:
        mapa.append(list(line))
#Establecemos los puntos de inicio y final en las coordenadas 
    inicio = (0,0)
    final = (len(mapa[0]) - 1, len(mapa) - 1) 
    return mapa, inicio, final
#Escribir una función que limpie la pantalla y muestre la matriz
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
def mostrar_matriz(mapa):
    for linea in mapa:
        print("".join(linea))
#Implementar el main loop en una función
def main_loop(mapa, inicio, final):
    px, py = inicio
    while(px, py,) != final :
# Asignar el carácter "P" a la posición actual del jugador
        limpiar_pantalla()
    mapa[px][py] = 'P'
    mostrar_matriz(mapa)
    mapa[px][py] 
# Definimos dos variables px y py que contienen las coordenadas del jugador
    tecla = readkey()
    if tecla == key.UP and px > 0 and mapa[px - 1][py] != '#':
        px -= 1  # Flecha arriba
    elif tecla == key.DOWN and px < len(mapa) - 1 and mapa[px + 1][py] != '#':
        px += 1  # Flecha abajo
    elif tecla == key.LEFT and py > 0 and mapa[px][py - 1] != '#':
        py -= 1  # Flecha izquierda
    elif tecla == key.RIGHT and py < len(mapa[0]) - 1 and mapa[px][py + 1] != '#':
        py += 1  # Flecha derecha
    print ("Terminaste")

laberinto = """..###################
....#...............#
#.#.#####.#########.#
#.#...........#.#.#.#
#.#####.#.###.#.#.#.#
#...#.#.#.#.....#...#
#.#.#.#######.#.#####
#.#...#.....#.#...#.#
#####.#####.#.#.###.#
#.#.#.#.......#...#.#
#.#.#.#######.#####.#
#...#...#...#.#.#...#
###.#.#####.#.#.###.#
#.#...#.......#.....#
#.#.#.###.#.#.###.#.#
#...#.#...#.#.....#.#
###.#######.###.###.#
#.#.#.#.#.#...#.#...#
#.#.#.#.#.#.#.#.#.#.#
#.....#.....#.#.#.#.#
###################.."""

mapa = cadena_a_laberinto(laberinto)
inicio = (0, 0)
final = (len(mapa) - 1, len(mapa[0]) - 1)
main_loop(mapa, inicio, final)
    
