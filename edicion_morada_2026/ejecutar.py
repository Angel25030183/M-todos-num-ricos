"""Ejecución reproducible de los 18 ejercicios de la edición morada."""
import argparse
import csv
from casos import CASOS
from metodos import METODOS

def evaluar(c):
    opciones = {"max_iter":60,"tolerancia":1e-10} if c["metodo"]=="seidel" else {}
    r=METODOS[c["metodo"]](c["A"],c["b"],**opciones)
    ok=r["estado"]==c["esperado"]
    if c["x_ref"] is not None:
        ok = ok and r["solucion"] is not None
        if r["solucion"] is not None:
            ok = ok and max(abs(x-y) for x,y in zip(r["solucion"],c["x_ref"]))<1e-6
            ok = ok and r["residuo_inf"] is not None and r["residuo_inf"]<1e-6
    return r,bool(ok)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--detalle",action="store_true")
    parser.add_argument("--csv",default="resultados.csv")
    args=parser.parse_args()
    rows=[]
    for c in CASOS:
        r,ok=evaluar(c)
        print(c["clave"],r["estado"],"OK" if ok else "REVISAR")
        if args.detalle: print("A =",c["A"],"b =",c["b"],"x =",r["solucion"])
        rows.append({"id":c["clave"],"metodo":c["metodo"],"esperado":c["esperado"],
                     "observado":r["estado"],"verificado":"OK" if ok else "REVISAR",
                     "solucion":str(r["solucion"] or ""),
                     "residuo":str(r["residuo_inf"] if r["residuo_inf"] is not None else "")})
    with open(args.csv,"w",newline="",encoding="utf-8-sig") as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]))
        w.writeheader();w.writerows(rows)
    n=sum(row["verificado"]=="OK" for row in rows)
    print(f"VERIFICACIÓN: {n}/{len(rows)} casos aprobados")
    return 0 if n==len(rows) else 1

if __name__=="__main__": raise SystemExit(main())
