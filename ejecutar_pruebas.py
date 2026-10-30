"""Ejecuta los 18 ejercicios, imprime diagnóstico y comprueba expectativas."""
import argparse
import csv
from pathlib import Path
from casos import CASOS
from metodos import METODOS

def ejecutar(caso):
    metodo=METODOS[caso['metodo']]
    kwargs={'max_iter':45,'tolerancia':1e-10} if caso['metodo']=='seidel' else {}
    return metodo(caso['A'],caso['b'],**kwargs)

def main():
    parser=argparse.ArgumentParser(description='Problemario automotriz: 18 casos.')
    parser.add_argument('--csv',metavar='RUTA',help='Exporta resultados a CSV.')
    parser.add_argument('--detalle',action='store_true',help='Muestra operaciones/iteraciones.')
    args=parser.parse_args()
    filas=[]; aprobados=0
    for caso in CASOS:
        resultado=ejecutar(caso)
        ok_estado=resultado['estado']==caso['esperado']
        ok_sol=True
        if caso['solucion_esperada'] is not None:
            ok_sol=(resultado['solucion'] is not None and
                    max(abs(a-b) for a,b in zip(resultado['solucion'],caso['solucion_esperada']))<1e-6 and
                    resultado['residuo_inf']<1e-6)
        aprobado=ok_estado and ok_sol
        aprobados+=aprobado
        xs='' if resultado['solucion'] is None else ', '.join(f'{v:.6f}' for v in resultado['solucion'])
        r='' if resultado['residuo_inf'] is None else f"{resultado['residuo_inf']:.3e}"
        print(f"{caso['id']}: {resultado['estado']:<16} | x=({xs}) | residuo={r} | {'OK' if aprobado else 'ERROR'}")
        if args.detalle:
            for p in resultado['pasos']: print('  ',p)
            for paso in resultado.get('historial',[])[:6]:
                print('   iter={iteracion} x={x} cambio={cambio_rel:.3e} residuo={residuo_inf:.3e}'.format(**paso))
        filas.append({'id':caso['id'],'metodo':caso['metodo'],'esperado':caso['esperado'],
                      'obtenido':resultado['estado'],'solucion':xs,
                      'residuo_infinito':r,'veredicto':'OK' if aprobado else 'ERROR'})
    if args.csv:
        destino=Path(args.csv); destino.parent.mkdir(parents=True,exist_ok=True)
        with destino.open('w',newline='',encoding='utf-8-sig') as f:
            writer=csv.DictWriter(f,fieldnames=list(filas[0]))
            writer.writeheader();writer.writerows(filas)
        print(f'Resultados exportados a {destino}')
    print(f'RESUMEN: {aprobados}/{len(CASOS)} casos correctos')
    return 0 if aprobados==len(CASOS) else 1

if __name__=='__main__':
    raise SystemExit(main())
