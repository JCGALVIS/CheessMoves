from unittest import TestCase
from movimientos import *

class Test_movimientos(TestCase):
    def test_tablero_a_cadena(self):
        dado = []
        espero = ""
        obtengo = tablero_a_cadena(dado)
        self.assertEquals(espero, obtengo)
    def test_obtener_nombre_pieza(self):
        dado = 'k'
        espero = "Caballo blanco"
        obtengo = obtener_nombre_pieza(dado)
        self.assertEquals(espero, obtengo)
        dado = 'p'
        espero = "Peon blanco"
        obtengo = obtener_nombre_pieza(dado)
        self.assertEquals(espero, obtengo)
        dado = 't'
        espero = "Torre blanco"
        obtengo = obtener_nombre_pieza(dado)
        self.assertEquals(espero, obtengo)
        dado = 'a'
        espero = "Alfil blanco"
        obtengo = obtener_nombre_pieza(dado)
        self.assertEquals(espero, obtengo)
        dado = 'q'
        espero = "Reina blanco"
        obtengo = obtener_nombre_pieza(dado)
        self.assertEquals(espero, obtengo)
        dado = 'r'
        espero = "Rey blanco"
        obtengo = obtener_nombre_pieza(dado)
        self.assertEquals(espero, obtengo)
    def test_mover_torre(self):
        dado = [
            [['t', 'k', 'a', 'q', 'r', 'a', 'k', 't'],
            [' ', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['T', 'K', 'A', 'R', 'Q', 'A', 'K', 'T']],
            0,0,4,0
        ]
        espero = [
            [' ', 'k', 'a', 'q', 'r', 'a', 'k', 't'],
            [' ', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['t', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['T', 'K', 'A', 'R', 'Q', 'A', 'K', 'T']
        ]
        obtengo = mover_torre(dado[0], dado[0], dado[0] , dado[4], dado[0])
        self.assertEquals(espero, obtengo)
        self.assertRaises(ValueError)

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

    def test_mover_caballo(self):
        dado = [
            [['t', 'k', 'a', 'q', 'r', 'a', 'k', 't'],
             ['p', 'p', ' ', 'p', 'p', 'p', 'p', 'p'],
             [' ', ' ', 'p', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['T', 'K', 'A', 'R', 'Q', 'A', 'K', 'T']],
            0, 1, -1, 8
        ]
        espero =  'Posición final no valida.'
        obtengo = mover_caballo(dado[0], dado[1], dado[2] , dado[3], dado[4])
        self.assertEquals(espero, obtengo)

        dado = [
            [['t', 'k', 'a', 'q', 'r', 'a', 'k', 't'],
             ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['T', 'K', 'A', 'R', 'Q', 'A', 'K', 'T']],
            0, 0, 1, 3
        ]
        espero = 'No es un caballo.'
        obtengo = mover_caballo(dado[0], dado[1], dado[2] , dado[3], dado[4])
        self.assertEquals(espero, obtengo)

        dado = [
            [['t', 'k', 'a', 'q', 'r', 'a', 'k', 't'],
             ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['T', 'K', 'A', 'R', 'Q', 'A', 'K', 'T']],
            0, 1, 3, 1
        ]
        espero =  'Movimiento es invalido.'
        obtengo = mover_caballo(dado[0], dado[1], dado[2] , dado[3], dado[4])
        self.assertEquals(espero, obtengo)

        dado = [
            [['t', 'k', 'a', 'q', 'r', 'a', 'k', 't'],
             ['p', 'p', ' ', 'p', 'p', 'p', 'p', 'p'],
             [' ', ' ', 'p', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['T', 'K', 'A', 'R', 'Q', 'A', 'K', 'T']],
            0, 1, 2, 2
        ]
        espero =  'Ficha amiga.'
        obtengo = mover_caballo(dado[0], dado[1], dado[2] , dado[3], dado[4])
        self.assertEquals(espero, obtengo)

        dado = [
            [['t', 'k', 'a', 'q', 'r', 'a', 'k', 't'],
             ['p', 'p', ' ', 'p', 'p', 'p', 'p', 'p'],
             [' ', ' ', 'P', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['T', 'K', 'A', 'R', 'Q', 'A', 'K', 'T']],
            0, 1, 2, 2
        ]
        espero =  ['t', 'k', 'a', 'q', 'r', 'a', 'k', 't'],
        ['p', 'p', ' ', 'p', 'p', 'p', 'p', 'p'],
        [' ', ' ', 'k', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        ['T', 'K', 'A', 'R', 'Q', 'A', 'K', 'T']

        obtengo = mover_caballo(dado[0], dado[1], dado[2] , dado[3], dado[4])
        self.assertEquals(espero, obtengo)