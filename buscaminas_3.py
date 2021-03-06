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

def mostrar_tablero(tablero, columna):
    """
    Muestra en filas y columnas la matriz que le pasemos
    """
    print("* " * (columna + 2))
    for fila in tablero:
        print("*", end=" ")
        for elemento in fila:
            print(elemento, end=" ")
        print("*")
    print("* " * (columna + 2))

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
                        if 0 <= y+i <= fila-1 and 0 <= x+j <= x+j <= columna-1:
                            if tablero[y+i][x+j] != 9:
                                tablero[y+i][x+j] += 1
    return tablero

def relleno(oculto, visible, y, x, fila, columna, value):
    """ Recorre todas las casilla vecinas y comprueba si son ceros, si asi las muestra,
    y recorre las vecinas de esta, hasta encontrar casillas con pista que tambien los muestra pero sirve de limitacion"""
    ceros = [(y,x)]
    while len(ceros) > 0:
        y, x = ceros.pop()
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if 0 <= y + i <= fila - 1 and 0 <= x + j <= columna - 1:
                    if visible[y+i][x+j] == value and oculto[y+i][x+j] == 0:
                        visible[y+i][x+j] = 0
                        if (y+i, x+j) not in ceros:
                            ceros.append((y+i, x+j))
                    else:
                        visible[y+i][x+j] = oculto[y+i][x+j]
    return visible

def tablero_completo(tablero, fila, columna, value):
    """Comprueba si el tablero no tiene ninguna casilla con el valor visible inicial"""
    for y in range(fila):
        for x in range(columna):
            if tablero[y][x] == value:
                return False
    return True

def reemplazar_ceros(tablero, fila, columna):
    for i in range(fila):
        for j in range(columna):
            if tablero[i][j] == 0:
                tablero[i][j] = ' '
    return tablero


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
    opcion = input("w(up)/s(down)/a(left)/d(right) - m - b(check)/v(uncheck)? ")
    return opcion

"""Parametros del juego """

columnas = 16
filas = 12

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

mostrar_tablero(visible,columnas)

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

    elif opcion == 'b':
        if real == '-':
            visible[y][x] = '$'
            real = visible[y][x]
            if (y,x) not in minas_marcadas:
                minas_marcadas.append((y,x))

    elif opcion == 'v':
        if real == '$':
            visible[y][x] = '-'
            real = visible[y][x]
            if (y,x) in minas_marcadas:
                minas_marcadas.remove((y,x))

    elif opcion == 'm':
        if oculto[y][x] == 9:
            visible[y][x] = '*'
            jugar = False

        elif oculto[y][x] != 0:
            visible[y][x] = oculto[y][x]
            real = visible[y][x]

        elif oculto[y][x] == 0:
            visible[y][x] = 0
            visible = relleno(oculto, visible, y, x, filas, columnas, "-")
            visible = reemplazar_ceros(visible, filas, columnas)
            real = visible[y][x]

    os.system("clear")
    mostrar_tablero(visible, columnas)

    ganar = False

    if tablero_completo(visible, filas, columnas, '-') and\
       sorted(minas_ocultas) == sorted(minas_marcadas) and real != '-':
        ganar = True
        jugar = False

if ganar:
    print("************************************")
    print("******FELICIDADES HAS GANADO *******")
    print("************************************")
else:
    print("************************************")
    print("******LO SIENTO HAS PERDIDO ********")
    print("************************************")
