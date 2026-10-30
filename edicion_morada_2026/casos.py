"""18 ejercicios nuevos de sistemas de ecuaciones lineales, con datos didácticos.

Para los casos resueltos, el vector indicado es la solución de referencia y b
se calcula mediante A @ x. Para los casos de diagnóstico, el vector es b.
"""
RAW = [["EG01","gauss","Presiones de frenado",[[3,1],[2,5]],[120,80],"resuelto"],["EG02","gauss","Soportes de transmisión",[[0,4,-1],[6,2,1],[1,-1,5]],[8,6,4],"resuelto"],["EG03","gauss","Corrientes del alternador",[[9,-1,0],[2,11,-1],[0,1,7]],[10,7,4],"resuelto"],["EG04","gauss","Rigidez del chasis",[[6,1,0,1],[1,7,-2,0],[0,-2,8,1],[1,0,1,9]],[30,40,25,35],"resuelto"],["EG05","gauss","Presiones contradictorias",[[1,2],[2,4]],[9,19],"inconsistente"],["EG06","gauss","Resistencias térmicas insuficientes",[[1,1,1],[2,2,2],[1,-1,0]],[6,12,1],"indeterminado"],["GJ01","jordan","Consumo auxiliar",[[4,2],[1,5]],[6,3],"resuelto"],["GJ02","jordan","Caudales de refrigerante",[[0,2,1],[3,-1,2],[1,1,5]],[12,9,7],"resuelto"],["GJ03","jordan","Deformaciones del diferencial",[[7,-1,0],[2,8,1],[0,1,6]],[3,5,2],"resuelto"],["GJ04","jordan","Fuerzas en cuatro neumáticos",[[6,1,0,0],[1,7,-1,0],[0,-1,8,2],[0,0,1,9]],[100,80,90,70],"resuelto"],["GJ05","jordan","Calibración contradictoria",[[1,-2],[3,-6]],[4,13],"inconsistente"],["GJ06","jordan","Válvula con parámetros ambiguos",[[2,1,1],[4,2,2],[0,1,-1]],[9,18,1],"indeterminado"],["GS01","seidel","Temperaturas del rectificador",[[14,-1,1],[-2,13,-1],[1,-1,12]],[45,47,43],"resuelto"],["GS02","seidel","Voltajes de celdas",[[12,-1,0],[-1,11,-1],[0,-2,10]],[3.7,3.65,3.75],"resuelto"],["GS03","seidel","Válvulas de suspensión",[[10,1,-1],[1,9,2],[-1,2,11]],[15,18,12],"resuelto"],["GS04","seidel","Motor de cuatro fases",[[16,-1,0,1],[-2,15,-1,0],[0,-1,14,-2],[1,0,-2,13]],[8,7,9,6],"resuelto"],["GS05","seidel","Actuador con diagonal nula",[[0,2],[3,8]],[5,6],"diagonal_nula"],["GS06","seidel","Control con acoplamiento inestable",[[1,4],[3,1]],[5,4],"no_convergencia"]]
CASOS = []
for clave, metodo, titulo, A, vector, esperado in RAW:
    es_correcto = esperado == "resuelto"
    b = [sum(ai*xi for ai, xi in zip(fila, vector)) for fila in A] if es_correcto else vector
    CASOS.append({"clave": clave, "metodo": metodo, "titulo": titulo, "A": A,
                  "b": b, "x_ref": vector if es_correcto else None,
                  "esperado": esperado})
