#SingleInstance, Force
Gui, Font, s12 Bold
Gui, Add, Text, x140 y19 h20 , Teste Tecnico SWAPI

Gui, Font
Gui, Add, Text, x22 y59 w120 h30, Distancia a ser percorrida (em MGLT):
Gui, Add, Edit, x152 y59 w140 h20 vMglt
Gui, Font, s11
Gui, Add, Button, x310 y54 gCalcularParadasNavios, Calcular

Gui, Font, s10 bold
Gui, Add, Text, x122 y119 h20 vParadasTexto, Quantidade de paradas por nave:
Gui, Font
Gui, Add, ListView, x12 y139 w430 h170, Nome da Nave                  |Paradas necessarias

Gui, Show, w452 h320, Teste Tecnico SWAPI
return

CalcularParadasNavios:
    Gui, Submit, NoHide
    LV_Delete()

    GuiControl,, paradasTexto, [*] Calculando... 
    comando := "python main.py " . mglt . " > shipStops.txt"
    RunWait, %comspec% /c %comando%,,hide

    if(ErrorLevel != 0){
        GuiControl,, paradasTexto, [ ! ] Erro no calculo (ErrorCode: %ErrorLevel%)
        Return
    }

    GuiControl,, paradasTexto, Quantidade de paradas por nave:
    addDistancesList()

    Return
GuiClose:
    ExitApp

addDistancesList(){
    shipsInfo := FileOpen("shipStops.txt","r").Read()
    ;separador := "`r" ; `r = quebra de linha (\n)
    shipsInfoArray := splitStr(shipsInfo)

    For index,shipInfo in shipsInfoArray {
        shipInfoArray := splitStr(shipInfo,":")
        LV_Add("", shipInfoArray[1], shipInfoArray[2])
    }
    ;Loop, Parse, shipsInfo, % `separador
    {

    }
}

splitStr(str,delim="`r"){
    ; separa uma string em array de strings
    strVet := []
    Loop, Parse, str, % `delim
        strVet.Push(A_LoopField)
    return strVet
}
;RunWait, %comspec% /c "python main.py > retorno.txt",,hide
