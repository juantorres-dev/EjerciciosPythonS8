from random import randint

def temperatura():
    listaTemperatura =  []
    for a in range(8):
        for i in range(20):

            diario = randint(0, 100)

            listaTemperatura.append(diario)

    return listaTemperatura


resultado = temperatura()

print(resultado)




