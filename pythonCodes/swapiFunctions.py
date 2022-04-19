# Execução do calculo de paradas e outras funcionalidades da SWAPI

from math import floor
import requests

# estrutura de tempos a serem utilizados no calculo
timesDay = {'day':1,'week':7,'month':30,'year':360}

def getShipData(apiURL):
    # Pega as informações das naves de uma pagina da API

    apiRequest = requests.get(apiURL) # Faz a requisição na API

    if apiRequest.status_code != 200: # Checa se a requisição foi executada com sucesso 
        print(f'[!] {apiRequest.status_code}')
        exit(1)

    apiData = apiRequest.json() # Conteúdo da requisição em JSON
    shipsPageInfo = {
        'next': apiData['next'],
        'shipData': {}
    }

    for shipInfo in apiData['results']: # Percorre cada nave da requisição atual feita
        shipName = shipInfo['name']
        shipsPageInfo['shipData'][shipName] = [] # Adiciona uma nova nave encontrada

        # Pega a MGLT da nave se ela for informada pela API
        if shipInfo['MGLT'].isnumeric():
            shipsPageInfo['shipData'][shipName].append( float(shipInfo['MGLT']) )
        else:
            shipsPageInfo['shipData'][shipName].append('Unknown')

        # Pega os consumables da nave (tempo que ela consegue ficar navegando) e remove o plural (s) do final do tempo se houver (exemplo: weeks = week)
        shipsPageInfo['shipData'][shipName].append( shipInfo['consumables'].lower().rstrip('s') )
    
    return shipsPageInfo

def getAllShipsData(apiURL):
    # Pega as informações das naves de todas as paginas da API

    allShipsInfo = {} # Armazenará as informações de todos as naves da API

    while apiURL: # Pega as informações na API até a ultima nave (checada pelo ['next'])
        shipsPageInfo = getShipData(apiURL)

        # concatena a informação das naves da pagina atual com as anteriores
        allShipsInfo = {**allShipsInfo, **shipsPageInfo['shipData']} 
        # pega a proxima URL das naves da API (se for a ultima = None)
        apiURL = shipsPageInfo['next']
    
    return allShipsInfo # retorna todas as informacoes das naves da API

def calculateShipStops(totalDistance, shipMGLT, shipConsumables):
    global timesDay
    if type(shipMGLT) == str: # Verifica se a nave possui uma MGLT determinada na API 
        return shipMGLT

    # Converte o tempo que a nave possui para continuar navegando sem parar (consumables) em horas
    hours = -1 
    for i in timesDay:
        if shipConsumables.endswith(i):
            hours = float(shipConsumables.split(' ')[0]) * timesDay[i] * 24
            break

    if hours == -1: # Checa se a conversão foi feita corretamente
        print(f'[!] Error: {hours}')
        exit(2)

    firstStop = hours*shipMGLT
    totalStops = floor(totalDistance/firstStop) # calcula a quantidade de paradas com base na distancia e em quanto tempo leva para primeira parada
    return totalStops # retorna o total de paradas necessarias
