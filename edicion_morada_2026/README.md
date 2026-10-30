# Problemario de Métodos Numéricos | Edición morada 2026

**Autor:** Ángel Jesús Moreno Trejo — **Matrícula:** 25030183  
**Institución:** Instituto Tecnológico Superior del Oriente del Estado de Hidalgo (ITESA)  
**Profesor:** Efrén Rolando Romero León  
**Carrera:** Ingeniería en Sistemas Automotrices

## Alcance
Versión completamente nueva del problemario de sistemas de ecuaciones lineales. Contiene **18 ejercicios diferentes** y soluciones en Python de tres algoritmos:

| Método | Casos | Correctos | Diagnósticos |
| --- | --- | ---: | ---: |
| Eliminación Gaussiana con pivoteo parcial | EG01–EG06 | 4 | 2 |
| Gauss-Jordan con pivoteo parcial | GJ01–GJ06 | 4 | 2 |
| Gauss-Seidel con validación de residuo | GS01–GS06 | 4 | 2 |

Todos los modelos automotrices son **sintéticos y de uso exclusivamente didáctico**.

## Código fuente real

- [metodos.py](metodos.py): implementaciones Python editables de los tres algoritmos.
- [casos.py](casos.py): definiciones numéricas reproducibles de los dieciocho sistemas.
- [ejecutar.py](ejecutar.py): ejecución y exportación de la tabla de resultados.
- [tests/test_algoritmos.py](tests/test_algoritmos.py): cinco pruebas unitarias.
- [resultados.csv](resultados.csv): resultados de una ejecución local verificada.

## Instrucciones
Se necesita Python 3.10 o posterior, sin instalar dependencias externas. Desde esta carpeta:

```bash
python ejecutar.py --detalle
python ejecutar.py --csv resultados.csv
python -m unittest discover -s tests -v
```

Se espera **18/18 ejercicios aprobados y cinco pruebas unitarias correctas**. Los casos de diagnóstico están diseñados para devolver un error controlado, no para producir resultados ficticios.

**Interpretación de códigos:** `resuelto` (solución única), `inconsistente` (sin solución), `indeterminado` (soluciones infinitas), `diagonal_nula` (reordenamiento o reformulación requerido), `no_convergencia` (iteraciones sin satisfacer criterio).

## Vinculación documental

El archivo de Word/PDF del problemario incluye enlaces permanentes a esta carpeta y a los archivos fuente. Los archivos de código se publicaron como texto fuente, **no como capturas**. El informe distingue claramente la validación local de la mera publicación en GitHub: no se afirma que una GitHub Action haya ejecutado las pruebas.

**Ruta del repositorio:** https://github.com/Angel25030183/M-todos-num-ricos/tree/main/edicion_morada_2026
