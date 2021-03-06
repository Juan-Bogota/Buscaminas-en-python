#!/usr/bin/python3
"""Juego buscaminas"""
import random
import os

def crear_tablero(fila, columna, value):
    """Crea una matriz con filas y columnas
       el valor de cada fila-columna
    """
    tablero = []
    for i in range(fila):
        tablero.append([])
        for j in range(columna):
            tablero[i].append(value)
    return tablero

def mostrar_tablero(tablero):
    """
    Muestra en filas y columnas la matriz que le pasemos
    """

    for fila in tablero:
        for elemento in fila:
            print(elemento, end=" ")
        print()

def coloca_minas(tablero, minas, fila, columna):
    """Coloca en el tablero el numero de minas"""

    minas_ocultas = []
    numero = 0
    while numero < minas:
        y = random.randint(0,fila-1)
        x = random.randint(0,columna-1)
        if tablero[y][x] != 9:
            tablero[y][x] = 9
            numero += 1
            """Guarda la informacion de las minas ocultas con lo pues del usuario"""
            minas_ocultas.append((y,x))
    """ tablero con las minas puesta y la lista de las minas"""
    return tablero, minas_ocultas

def colocar_pistas(tablero, fila, columna):
    """valida si la casilla es 9 correspondiente a una mina y le asigna valores en todas las direcciones"""


    for y in range(fila):
        for x in range(columna):
            if tablero[y][x] == 9:
                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        if 0 < y+i <= fila-1 and 0 <= x+j <= x+j <= columna-1:
                            if tablero[y+i][x+j] != 9:
                                tablero[y+i][x+j] += 1
    return tablero
"""
            if tablero[y][x] == 9:
                if x < columna-1:
                    if tablero[y][x+1] != 9:
                        tablero[y][x+1] += 1
                if x > 0:
                    if tablero[y][x-1] != 9:
                        tablero[y][x-1] += 1
                if y > 0:
                    if tablero[y-1][x] != 9:
                        tablero[y-1][x] += 1
                if y < filas-1:
                    if tablero[y+1][x] != 9:
                        tablero[y+1][x] += 1

"""


def presentacion():
    """Presentacion inicial"""

    os.system("clear")

    print("+++++++++++++++++++")
    print("+                 +")
    print("+   BUSCAMINAS    +")
    print("+                 +")
    print("+                 +")
    print("+ w/a/s/d - mover +")
    print("+                 +")
    print("+   m - mostrar   +")
    print("+   b - marcar    +")
    print("+  d - desmarcar  +")
    print("+                 +")
    print("+++++++++++++++++++")
    input("Enter para empezar la partida...")

def menu():
    """ devuelve el movimiento u opcion elegida por el usuario"""
    print()
    opcion = input("w/s/a/d - m - b/v? ")
    return opcion

"""Parametros del juego """

columnas = 16
filas = 14

visible = crear_tablero(filas, columnas, "-")
oculto = crear_tablero(filas, columnas, 0)

"""Minas"""

oculto, minas_ocultas = coloca_minas(oculto, 20, filas, columnas)
oculto = colocar_pistas(oculto, filas, columnas)
presentacion()

"""colocamos el punto de inicio de la partido(cursor)"""

y = random.randint(2, filas-3)
x = random.randint(2, columnas-3)
"""Vamos a guardar el verdadero valor de la casilla antes de situar la ficha,
asi cuando la ficha se mueva podemos recuperar el valor que tenia antes de que
se situase la ficha en esa casilla y una vez guardado el valor real de la casilla
pues en esa casilla situamos el valor de X"""

real = visible[y][x]
visible[y][x] = "X"

"""borrar la pantalla"""
os.system("clear")

mostrar_tablero(oculto)

"""Principal"""
"""minas marcadas por el usuario para compararlos con las minas ocultas(colaca minas)"""
minas_marcadas = []

jugar = True

while jugar:
    opcion = menu()
    if opcion == 'w':
        if y == 0:
            y = 0
        else:
            visible[y][x] = real
            y -= 1
            real = visible[y][x]
            visible[y][x] = "X"
    elif opcion == 's':
        if y == filas -1:
            y = filas - 1

        else:
            visible[y][x] = real
            y += 1
            real = visible[y][x]
            visible[y][x] = "X"
    elif opcion == 'a':
        if x == 0:
            x = 0
        else:
            visible[y][x] = real
            x -= 1
            real =  visible[y][x]
            visible[y][x] = "X"

    elif opcion == 'd':
        if x == columnas -1:
            x = columnas -1
        else:
            visible[y][x] = real
            x += 1
            real = visible[y][x]
            visible[y][x] = "X"

    os.system("clear")

    mostrar_tablero(visible)
