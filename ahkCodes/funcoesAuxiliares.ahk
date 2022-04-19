#SingleInstance, Force

splitStr(str, separador="`r"){
    /*  Separa uma string em array de strings (default: \n)
        OBS: no AutoHotKey -> `r = \n 
    */
    strVet := []
    
    Loop, Parse, str, % `separador ; Percorre a string delimitando no separador
        strVet.Push(A_LoopField)
    return strVet
}
