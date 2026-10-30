"""Pruebas unitarias reproducibles desde la carpeta problemario-original-jorge-angel."""
import unittest
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from casos import CASOS
from metodos import METODOS,eliminacion_gaussiana,gauss_jordan,gauss_seidel

class PruebasProblemario(unittest.TestCase):
    def test_los_18_casos(self):
        for caso in CASOS:
            with self.subTest(caso=caso['id']):
                kwargs={'tolerancia':1e-10,'max_iter':45} if caso['metodo']=='seidel' else {}
                respuesta=METODOS[caso['metodo']](caso['A'],caso['b'],**kwargs)
                self.assertEqual(respuesta['estado'],caso['esperado'])
                if caso['solucion_esperada'] is not None:
                    self.assertLess(respuesta['residuo_inf'],1e-6)
                    for obtenido,esperado in zip(respuesta['solucion'],caso['solucion_esperada']):
                        self.assertAlmostEqual(obtenido,esperado,places=6)
    def test_entrada_mal_formada(self):
        for fn in [eliminacion_gaussiana,gauss_jordan,gauss_seidel]:
            with self.subTest(metodo=fn.__name__):
                with self.assertRaises(ValueError): fn([[1,2,3],[4,5,6]],[1,2])
                with self.assertRaises(ValueError): fn([[1,2],[3,4]],[1])
    def test_no_modifica_la_entrada(self):
        A=[[2,1],[1,3]];b=[4,7]
        for fn in [eliminacion_gaussiana,gauss_jordan,gauss_seidel]:
            fn(A,b)
            self.assertEqual(A,[[2,1],[1,3]])
            self.assertEqual(b,[4,7])
    def test_sistema_invertible_y_pivote_nulo(self):
        for fn in [eliminacion_gaussiana,gauss_jordan]:
            r=fn([[0,1],[1,1]],[2,5])
            self.assertEqual(r['estado'],'resuelto')
            self.assertAlmostEqual(r['solucion'][0],3)
            self.assertAlmostEqual(r['solucion'][1],2)

if __name__=='__main__':
    unittest.main()
