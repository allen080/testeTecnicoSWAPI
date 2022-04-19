from math import floor

timesDay = {'day':1,'week':7,'month':30,'year':360}

def calculateShipStops(totalDistance, shipMGLT, shipConsumables):
    if type(shipMGLT) == str:
        return shipMGLT

    global timesDay
    horas = -1

    for i in timesDay:
        if consumables.endswith(i):
            horas = float(consumables.split(' ')[0]) * timesDay[i] * 24
            break

    if horas == -1:
        print(f'[!] erro: {horas}')
        exit(2)

    paradaInicial = horas*shipMGLT
    totalParadas = floor(totalDistance/paradaInicial)
    return totalParadas