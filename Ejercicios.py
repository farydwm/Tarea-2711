#faryd walteros primer commit
    ## V es el numero de vacas-Kv el numero de metros cuadrados que nesesita una vaca- N la cantidad de metros cuadrados de la granja-x la produccion de leche diaria 

V = int(input("Ingresa el número de vacas: "))
Kv = 5
N = int(input("Ingresa el número de metros cuadrados de la granja: "))
X = float(input("Ingresa el número de produccion de leche: "))

## segundo commit Juan Pablo Gomez
    ## si la cantidad de metros de la granja es menor al que nesesitan las vacas para producir leche 
    ## calculo de produccion semanal 
def ProduccionSemanal (V,Kv,N,X):
    if V * Kv > N:
        return ("las vacas no tienen suficientes metros cuadrados de pasto")
    Xsemanal = V * X * 7 
    return Xsemanal 

ProduccionLecheSem = ProduccionSemanal (V,Kv,N,X)
print (f"la produccion de leche semanal en la granja es de:{ProduccionLecheSem} litos")
# Datos de las aves
mes_dias = 30  # número de días en un mes
gallinas = A // 3  # 1/3 de las aves son gallinas
mitad_gallinas = gallinas // 2  # la mitad de las gallinas ponen huevos cada 3 días
