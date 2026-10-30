"""Tres solucionadores didácticos de Ax=b, sin bibliotecas externas.

Estados: resuelto, inconsistente, indeterminado, diagonal_nula, no_convergencia.
El residuo infinito comprueba max_i |(Ax)_i-b_i|.
"""
from __future__ import annotations
from math import isfinite
EPS = 1e-12

def _datos(A, b):
    """Valida y copia datos para no modificar matrices originales."""
    if not isinstance(A, (list, tuple)) or not A:
        raise ValueError('A debe ser una matriz cuadrada no vacía.')
    n = len(A)
    if not all(isinstance(fila, (list, tuple)) and len(fila) == n for fila in A):
        raise ValueError('A debe ser cuadrada, sin filas incompletas.')
    if not isinstance(b, (list, tuple)) or len(b) != n:
        raise ValueError('b debe tener tantos elementos como filas en A.')
    try:
        M = [[float(v) for v in fila] for fila in A]
        y = [float(v) for v in b]
    except (TypeError, ValueError) as exc:
        raise ValueError('Todos los datos deben ser numéricos.') from exc
    if not all(isfinite(v) for fila in M for v in fila) or not all(isfinite(v) for v in y):
        raise ValueError('Los valores deben ser finitos.')
    return M, y

def residuo_infinito(A, b, x):
    """Norma infinito del residuo: max(abs(Ax-b))."""
    return max(abs(sum(aij * xj for aij, xj in zip(fila, x)) - bi)
               for fila, bi in zip(A, b))

def _respuesta(estado, solucion=None, residuo=None, pasos=None, **extras):
    return {'estado': estado, 'solucion': solucion, 'residuo_inf': residuo,
            'pasos': pasos or [], **extras}

def eliminacion_gaussiana(A, b, eps=EPS):
    """Pivoteo parcial + eliminación hacia delante + sustitución regresiva."""
    M, y = _datos(A, b)
    n = len(M)
    U = [fila + [v] for fila, v in zip(M, y)]
    pasos, fila_pivote = [], 0
    for columna in range(n):
        piv = max(range(fila_pivote, n), key=lambda i: abs(U[i][columna]))
        if abs(U[piv][columna]) <= eps:
            continue
        if piv != fila_pivote:
            U[fila_pivote], U[piv] = U[piv], U[fila_pivote]
            pasos.append(f'Intercambiar F{fila_pivote+1} y F{piv+1}')
        for i in range(fila_pivote+1, n):
            factor = U[i][columna] / U[fila_pivote][columna]
            U[i] = [v - factor*p for v, p in zip(U[i], U[fila_pivote])]
            if abs(factor) > eps:
                pasos.append(f'F{i+1} <- F{i+1} - ({factor:.6g})F{fila_pivote+1}')
        fila_pivote += 1
        if fila_pivote == n:
            break
    for fila in U:
        if all(abs(v) <= eps for v in fila[:n]) and abs(fila[n]) > eps:
            return _respuesta('inconsistente', pasos=pasos, rango_A=fila_pivote)
    if fila_pivote < n:
        return _respuesta('indeterminado', pasos=pasos, rango_A=fila_pivote)
    x = [0.0]*n
    for i in range(n-1, -1, -1):
        x[i] = (U[i][n] - sum(U[i][j]*x[j] for j in range(i+1, n)))/U[i][i]
    return _respuesta('resuelto', x, residuo_infinito(M, y, x), pasos, rango_A=n)

def gauss_jordan(A, b, eps=EPS):
    """Pivoteo parcial + reducción por filas hasta [I|x]."""
    M, y = _datos(A, b)
    n = len(M)
    R = [fila + [v] for fila, v in zip(M, y)]
    pasos, fila_pivote = [], 0
    for columna in range(n):
        piv = max(range(fila_pivote, n), key=lambda i: abs(R[i][columna]))
        if abs(R[piv][columna]) <= eps:
            continue
        if piv != fila_pivote:
            R[fila_pivote], R[piv] = R[piv], R[fila_pivote]
            pasos.append(f'Intercambiar F{fila_pivote+1} y F{piv+1}')
        divisor = R[fila_pivote][columna]
        R[fila_pivote] = [v / divisor for v in R[fila_pivote]]
        pasos.append(f'F{fila_pivote+1} <- F{fila_pivote+1}/({divisor:.6g})')
        for i in range(n):
            if i == fila_pivote:
                continue
            factor = R[i][columna]
            R[i] = [v - factor*p for v, p in zip(R[i], R[fila_pivote])]
            if abs(factor) > eps:
                pasos.append(f'F{i+1} <- F{i+1} - ({factor:.6g})F{fila_pivote+1}')
        fila_pivote += 1
        if fila_pivote == n:
            break
    for fila in R:
        if all(abs(v) <= eps for v in fila[:n]) and abs(fila[n]) > eps:
            return _respuesta('inconsistente', pasos=pasos, rango_A=fila_pivote)
    if fila_pivote < n:
        return _respuesta('indeterminado', pasos=pasos, rango_A=fila_pivote)
    x = [R[i][-1] for i in range(n)]
    return _respuesta('resuelto', x, residuo_infinito(M, y, x), pasos, rango_A=n)

def gauss_seidel(A, b, x0=None, tolerancia=1e-9, max_iter=500, eps=EPS):
    """Actualización secuencial; verifica cambio relativo y residuo escalado."""
    M, y = _datos(A, b)
    n = len(M)
    if tolerancia <= 0 or max_iter < 1:
        raise ValueError('tolerancia y max_iter deben ser positivos.')
    if x0 is None:
        x = [0.0]*n
    else:
        if len(x0) != n:
            raise ValueError('x0 debe tener longitud n.')
        x = [float(v) for v in x0]
        if not all(isfinite(v) for v in x):
            raise ValueError('x0 debe contener valores finitos.')
    dominancia = all(abs(M[i][i]) > sum(abs(M[i][j]) for j in range(n) if j != i)
                    for i in range(n))
    if any(abs(M[i][i]) <= eps for i in range(n)):
        return _respuesta('diagonal_nula', iteraciones=0, historial=[],
                          diagonal_dominante=dominancia)
    historial = []
    escala_b = max(1.0, max(abs(v) for v in y))
    for k in range(1, max_iter+1):
        anterior = x.copy()
        for i in range(n):
            suma = sum(M[i][j]*x[j] for j in range(n) if j != i)
            x[i] = (y[i] - suma)/M[i][i]
        if not all(isfinite(v) for v in x):
            return _respuesta('no_convergencia', iteraciones=k,
                              historial=historial, diagonal_dominante=dominancia)
        cambio = max(abs(a-b) for a,b in zip(x, anterior))/max(1.0, max(abs(v) for v in x))
        res = residuo_infinito(M, y, x)
        historial.append({'iteracion': k, 'x': x.copy(), 'cambio_rel': cambio,
                          'residuo_inf': res})
        if cambio <= tolerancia and res/escala_b <= tolerancia:
            return _respuesta('resuelto', x, res, iteraciones=k,
                              historial=historial, diagonal_dominante=dominancia)
        if max(abs(v) for v in x) > 1e25:
            break
    return _respuesta('no_convergencia', iteraciones=len(historial),
                      historial=historial, diagonal_dominante=dominancia)

METODOS = {'gauss': eliminacion_gaussiana,
           'jordan': gauss_jordan,
           'seidel': gauss_seidel}
