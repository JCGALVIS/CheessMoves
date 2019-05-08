from unittest import TestCase
from movimientos import *

class Test_movimientos(TestCase):

    def test_tablero_a_cadena(self):
        dado = []
        espero = ""
        obtengo = tablero_a_cadena(dado)
        self.assertEquals(espero, obtengo)

    def test_obtener_nombre_pieza(self):
        dado = 'p'
        espero = 'Peon blanco'
        obtengo = obtener_nombre_pieza(dado)
        self.assertEquals(espero, obtengo)

    def test_mover_torre(self):
        dado = [
                [['t', 'k', 'a', 'q', 'r', 'a', 'k', 't'],
                ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                ['T', 'K', 'A', 'R', 'Q', 'A', 'K', 'T']],
                0, 0, 3, 3
               ]
        espero = []
        obtengo = mover_torre(dado[0], dado[1], dado[2] , dado[3], dado[4])
        self.assertEquals(espero, obtengo)