'''
	Descrição: Script de teste técnico para calculo do Nº de paradas necessárias para se
		percorrer uma distancia nas espaçonaves listadas na SWAPI (https://swapi.dev)
	Criado por: Luan F. (allen080)
'''

import sys

# Adiciona e importa o arquivo com as funções utilizadas na API
sys.path.insert(1, "./pythonCodes")
from swapiFunctions import calculateShipStops, getAllShipsData

apiURL = f'https://swapi.dev/api/starships/' # URL Inicial da API

try: # Pegar o valor da distancia total a ser percorrida e tenta converter pra float
	if len(sys.argv) < 2: # Se não passou o valor como argumento de linha de comando, pede o valor na tela
		totalDistance = input('Distância a ser percorrida (em MGLT): ')
	else: # Se passou o valor como argumento de linha de comando (Usado na mainGUI) 
		totalDistance = sys.argv[1] 
	
	totalDistance = float(totalDistance) # tenta converter o valor recebido em float
except ValueError:
	print(f'\n[!] Distância "{totalDistance}" não é um número.')
	sys.exit(1)
except KeyboardInterrupt:
	sys.exit(3)

allShipsInfo = getAllShipsData(apiURL)

allShipStops = {} # Calculo da quantidade paradas necessarias por cada nave na distância informada

for shipInfo in allShipsInfo: # Percorre cada nave obtida da API
	# realiza o calculo do Nº de paradas em todas naves
	shipStop = calculateShipStops(totalDistance, 
		allShipsInfo[shipInfo][0], allShipsInfo[shipInfo][1]
	)

	allShipStops[shipInfo] = shipStop # adiciona nas informacoes totais

# exibe na tela o nome da nave e o tempo necessário
for i in allShipStops: 
	print(f'{i}: {allShipStops[i]}')

