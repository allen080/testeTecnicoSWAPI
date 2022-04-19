import sys
import requests
import swapiFunctions # arquivo com as funções utilizadas na API

apiURL = f'https://swapi.dev/api/starships/' # URL Inicial da API

try:
	if len(sys.argv) < 2:
		totalDistance = input('Distância a ser percorrida (em MGLT): ')
	else:
		totalDistance = sys.argv[1]
	totalDistance = float(totalDistance)
except ValueError:
	print(f'\n[!] Distância "{totalDistance}" não é um número.')
	sys.exit(1)
except KeyboardInterrupt:
	sys.exit(2)


allShipsInfo = {}

while apiURL:
	apiRequest = requests.get(apiURL)
	if apiRequest.status_code != 200:
		print(f'[!] {apiRequest.status_code}')
		exit(1)

	apiData = apiRequest.json() # Conteúdo da requisição em JSON
	for shipInfo in apiData['results']:
		shipName = shipInfo['name']
		allShipsInfo[shipName] = []

		if shipInfo['MGLT'].isnumeric():
			allShipsInfo[shipName].append( float(shipInfo['MGLT']) )
		else:
			allShipsInfo[shipName].append('Unknown')
		allShipsInfo[shipName].append( shipInfo['consumables'].lower().rstrip('s') )

	apiURL = apiData['next']

allShipStops = {}
for shipInfo in allShipsInfo:	
	shipStop = swapiFunctions.calculateShipStops(totalDistance, 
		allShipsInfo[shipInfo][0], allShipsInfo[shipInfo][1]
	)

	allShipStops[shipInfo] = shipStop

for i in allShipStops:
	print(f'{i}: {allShipStops[i]}')

