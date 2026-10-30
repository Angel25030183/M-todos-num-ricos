# Guía de código fuente — Ángel Jesús Moreno Trejo

Alumno: Ángel Jesús Moreno Trejo (25030183). ITESA. Profesor: Efrén Rolando Romero León.

Este repositorio aloja los códigos del segundo problemario original de 18 ejercicios, con Eliminación Gaussiana (G01-G06), Gauss-Jordan (J01-J06) y Gauss-Seidel (S01-S06). Las matrices son datos didácticos sintéticos.

## Archivos

- `metodos.py`: implementaciones de los tres métodos.
- `casos.py`: los 18 sistemas del informe.
- `ejecutar_pruebas.py`: pruebas reproducibles y reporte.
- `tests/test_metodos.py`: comprobaciones unitarias.
- `resultados.csv`: tabla de resultados de referencia.

## Ejecutar desde una terminal en la raíz del repositorio

```bash
python ejecutar_pruebas.py --detalle
python ejecutar_pruebas.py --csv resultados.csv
python -m unittest discover -s tests -v
```

La consola permite comprobar el resultado de cada caso y las pruebas unitarias. El código está en formato de texto `.py`, no como imágenes. El registro CSV es una referencia de las pruebas locales; la publicación de archivos no significa que GitHub haya ejecutado automáticamente los programas.
