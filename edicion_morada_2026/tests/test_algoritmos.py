"""Pruebas unitarias de la edición morada."""
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from ejecutar import evaluar
from casos import CASOS
from metodos import eliminacion_gaussiana,gauss_jordan,gauss_seidel

class Verificacion(unittest.TestCase):
    def test_los_18_ejercicios(self):
        self.assertEqual(len(CASOS),18)
        for c in CASOS:
            with self.subTest(caso=c["clave"]):
                _,ok=evaluar(c)
                self.assertTrue(ok)
    def test_pivote_intercambiable(self):
        for metodo in [eliminacion_gaussiana,gauss_jordan]:
            x=metodo([[0,1],[2,1]],[3,7])
            self.assertEqual(x["estado"],"resuelto")
            self.assertAlmostEqual(x["solucion"][0],2)
    def test_inconsistencia(self):
        self.assertEqual(gauss_jordan([[1,2],[2,4]],[3,7])["estado"],"inconsistente")
    def test_conservacion_original(self):
        A=[[4,1],[1,3]];b=[9,7]
        for m in [eliminacion_gaussiana,gauss_jordan,gauss_seidel]:m(A,b)
        self.assertEqual(A,[[4,1],[1,3]])
        self.assertEqual(b,[9,7])
    def test_dimension(self):
        with self.assertRaises(ValueError):eliminacion_gaussiana([[1,2]],[3])

if __name__=="__main__":unittest.main()
