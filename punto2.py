from time import sleep

resultado = ""

def numero (lista):
    k = 1
    i = 0
    array = lista
    for i in range(len(lista)):
        if(lista[i]>lista[k]):
            c = array[i]
            d = array[k]
            
            array[i] = d
            array[k] = c
        k = k + 1
        if(k == len(lista)):
            return array
            break
numeros = [5,3,2,1,6,7,9]

ciclo = len(numeros)
for i in range(ciclo):
    resultado = numero(numeros)

print(resultado)