import os
from readchar import readkey, key
from pydantic import BaseModel
import random 


class NotFileError(Exception):
    pass

class Juego(BaseModel):
    mapa: list | None
    laberinto: str | None
    inicio: tuple | None
    final: tuple | None

    def cadena_a_laberinto(self,laberinto) -> None:
        self.mapa = [list(fila.strip()) for fila in self.laberinto.split("\n")]

    def limpiar_pantalla(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')

    def mostrar_matriz(self, mapa) -> None:
        for fila in self.mapa:
            print(''.join(fila))

    def main_loop(self, laberinto, inicio,final = None) -> None:
        
        
        px, py = inicio
        while (px, py) != final:
            self.limpiar_pantalla()
            self.mapa[px][py] = 'P'
            self.mostrar_matriz(self.mapa)
            self.mapa[px][py] = '.'

            tecla = readkey()
            if tecla == key.UP and px > 0 and self.mapa[px - 1][py] != '#':
                px -= 1  # Flecha arriba
            elif tecla == key.DOWN and px < len(self.mapa) - 1 and self.mapa[px + 1][py] != '#':
                px += 1  # Flecha abajo
            elif tecla == key.LEFT and py > 0 and self.mapa[px][py - 1] != '#':
                py -= 1  # Flecha izquierda
            elif tecla == key.RIGHT and py < len(self.mapa[0]) - 1 and self.mapa[px][py + 1] != '#':
                py += 1  # Flecha derecha
        print ("Terminaste")

class JuegoArchivo():
    def __init__(self):
        laberinto = self.leer_archivo()
        self.juego = Juego(inicio=(0,0),laberinto=laberinto,mapa=None,final = None)
    
    def leer_archivo(self) -> str:
        path = "/Users/acer//mapas"
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
        if os.path.exists(path):
            mapas = os.listdir(path)
            laberinto = list()
            if len(mapas) > 0:
                mapa = random.choice(mapas)
                with open(path+'/'+mapa,"r") as archivo:
                    laberinto = archivo.read()
            else:
                raise NotFileError("No hay archivos en la carpeta, se cargara mapa por defecto")
        return laberinto.strip()
    
    def comenzar_juego(self):
        self.juego.convertir_laberinto(self.juego.laberinto)
        self.juego.main_loop(self.juego.mapa,self.juego.inicio,final=(len(self.juego.mapa) - 1, len(self.juego.mapa[0]) - 1))

Jugar = JuegoArchivo()
Jugar.comenzar_juego()