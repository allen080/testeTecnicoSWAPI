import requests
from math import floor

distanciaSerPercorrida = 1000000

pageCount = 1
apiURL = f'https://swapi.dev/api/starships/' # URL Base da API
allShipsInfo = {}

while apiURL:
	apiRequest = requests.get(apiURL)
	if apiRequest.status_code != 200:
		print(f'[!] {apiRequest.status_code}')
		exit(1)

	apiData = apiRequest.json() # Conteúdo da requisição em JSON
	for shipInfo in apiData['results']:
		allShipsInfo[shipInfo['name']] = []
		for infoKey in ['consumables','MGLT']:
			allShipsInfo[shipInfo['name']].append(shipInfo[infoKey])

	apiURL = apiData['next']
	print(apiURL)
	pageCount += 1

print(len(allShipsInfo))
exit()



infoConsumables = apiData['consumables'].lower().rstrip('s')
naveMGLT = float(apiData['MGLT'])

times = {'day':1,'week':7,'month':30,'year':360}
horas = -1

for i in times:
	if consumables.endswith(i):
		horas = float(consumables.split(' ')[0]) * times[i] * 24
		break

if horas == -1:
	print(f'[!] erro: {horas}')
	exit(2)

paradaInicial = horas*naveMGLT
totalParadas = floor(distanciaSerPercorrida/paradaInicial)
print(totalParadas)
#print(html['name'])
