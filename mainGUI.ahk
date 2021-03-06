/* Interface Gráfica para Exibição e Cálculo das paradas das naves
*/

#SingleInstance, Force
#Include, ahkCodes/gui.ahk
#Include, ahkCodes/funcoesAuxiliares.ahk

SCRIPT_PATH := "./main.py"

Return

CalcularParadasNavios:
    ; Label que será chamada quando apertar o botão de calcular um valor

    Gui, Submit, NoHide ; Da um submit na GUI para pegar o valor da MGLT
    LV_Delete() ; Limpa a ListView

    ; Execução do script python (retorno no arquivo shipStops.txt) 
    GuiControl,, paradasTexto, [*] Calculando... 
    comando := "python " . SCRIPT_PATH . " " . mglt . " > shipStops.txt"
    RunWait, %comspec% /c %comando%,, hide

    if(ErrorLevel != 0){ ; Checa se ouve algum erro
        GuiControl,, paradasTexto, [ ! ] Erro no calculo (ErrorCode: %ErrorLevel%)
        Return
    }

    GuiControl,, paradasTexto, Quantidade de paradas por nave:
    addDistancesList() ; adiciona as informações obtidas na ListView
    Return

GuiClose: ; Encerra o programa quando clicar em fechar a GUI
    ExitApp

addDistancesList(){
    ; Exibe as informações do arquivo (de retorno do script python) na tela
    shipsInfo := FileOpen("shipStops.txt","r").Read() ; Pega o conteúdo do arquivo gerado
    shipsInfoArray := splitStr(shipsInfo)

    ; Percorre cada linha do arquivo gerado, separando o nome da nave da quantidade de paradas
    For index,shipInfo in shipsInfoArray {
        shipInfoArray := splitStr(shipInfo,":")
        LV_Add("", shipInfoArray[1], shipInfoArray[2]) ; Adiciona na lista as informações
    }
}
