#SingleInstance, Force
/* Criação da Interface Gráfica de Exibição
*/

; Titulo da GUI
Gui, Font, s12 Bold
Gui, Add, Text, x140 y19 h20 , Teste Tecnico SWAPI

; Pegar a distância a ser percorrida
Gui, Font
Gui, Add, Text, x22 y59 w120 h30, Distancia a ser percorrida (em MGLT):
Gui, Add, Edit, x152 y59 w140 h20 vMglt
Gui, Font, s11
Gui, Add, Button, x310 y54 gCalcularParadasNavios, Calcular

; Exibição das distancias
Gui, Font, s10 bold
Gui, Add, Text, x122 y119 h20 vParadasTexto, Quantidade de paradas por nave:
Gui, Font
Gui, Add, ListView, x12 y139 w430 h170, Nome da Nave                  |Paradas necessarias

; Exibe a GUI
Gui, Show, w452 h320, Teste Tecnico SWAPI