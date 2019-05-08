def tablero_a_cadena(tablero):
    cadena = ""
    for fila in tablero:
        cadena += str(fila) + "\n"
    return cadena


def obtener_nombre_pieza(simbolo):
    """
    (str) -> str

    >>> obtener_nombre_pieza('p')
    'Peon blanco'
    >>> obtener_nombre_pieza('R')
    'Rey Negro'

    Retorna el nombre de la pieza del ajedrez dado su simbolo

    :param simbolo: la representacion de la pieza segun el enunciado
    :return: El nombre y color de la pieza
    """

    tipo = 'Negro'
    if simbolo.islower():
        tipo = 'blanco'
    retorno = simbolo.lower()
    if retorno == 'p':
        return 'Peon '+tipo
    elif retorno == 't':
        return 'Torre ' + tipo
    elif retorno == 'k':
        return 'Caballo ' + tipo
    elif retorno == 'a':
        return 'Alfil ' + tipo
    elif retorno == 'q':
        return 'Reina ' + tipo
    elif retorno == 'r':
        return 'Rey ' + tipo
    else:
        return 'No es una pieza'

def mover_torre(tablero, x_inicial, y_inicial, x_final, y_final):
    print(tablero)
    print(x_inicial)
    print(y_inicial)
    print(x_final)
    print(y_final)
    esTorre = True
    if (x_inicial == x_final or y_inicial == y_final):
        esTorre = tablero[x_inicial][y_inicial] in 'tT'

        if (esTorre):
            for x in range(x_inicial + 1, x_final):
                if (tablero[x][y_inicial] == ' '):
                    for y in range(y_inicial, y_final):
                        print(tablero[x_inicial][y])
                else:
                    print('Camino bloqueado,')
                    break

        else:
            print('No es una torre.')
    else:
        print('El movimiento no es valido')


if __name__ == '__main__':
    tablero = [
                [['t', 'k', 'a', 'q', 'r', 'a', 'k', 't'],
                [' ', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                ['T', 'K', 'A', 'R', 'Q', 'A', 'K', 'T']],
                0, 0, 4, 0
               ]

    mover_torre(tablero[0], tablero[1], tablero[2] , tablero[3], tablero[4])