
tablero = [["_","_","_"],["_","_","_"],["_","_","_"]]

for fila in tablero: 
    print(' | '.join(fila))

xoy = None
while True:
    if xoy != "X" and xoy != "O":
        xoy = input ("Elija si usara X o O para jugar. (letra x o letra o en mayuscula): ")
    else:
        break

print ("\nComienzan las X ... \nAl elegir la posicion de tu jugada pon numero de fila y columna de la posicion 0 , 1 o 2\n\n")


def ganador (tablero):
    for fila in tablero:
        if fila[0] == fila[1] == fila[2] != "_":
            return "ganador"
    for i in (0,1,2):
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != "_":
            return "ganador"
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != "_":
        return "ganador"
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != "_":
        return "ganador"
    else:
        return "empate"

def eleccion (tablero):
    ver = False
    while ver == False:
        x = int(input ("Elija donde colocar su ficha (FILA 0,1,2): "))
        y = int(input ("Elija donde colocar su ficha (COLUMNA 0,1,2): "))
        
        if x not in {0,1,2} or y not in {0,1,2}:
            print ("Espacio incorrecto, coloque 0, 1 o 2\n") 
        elif tablero[x][y] != "_":
            print ("Espacio ocupado\n")
        else:
            ver = True
    return (x,y)

contador = 0
estado = "empate"

while estado == "empate":

    x,y = eleccion(tablero) #se llama funcion eleccion para que el jugador coloque su pieza

    if contador % 2 == 0: #Se verifica si corresponde poner X o O dependiendo el turno y se coloca
        tablero[x][y] = "X"
    else:
        tablero[x][y] = "O"
    
    estado = ganador(tablero) #en cada vuelta de elecciones se verifica si hay un ganador

    for fila in tablero: #imprimimos el tablero en cada jugada para ver como va
        print(' | '.join(fila))

    contador += 1
    if contador == 9 and estado == "empate":
        print ("\n\n JUEGO EMPATADO \n")
        break

if estado == "ganador" and contador % 2 == 0:
    print ("\n\n TENEMOS UN GANADOR, el ganador es O\n")
elif estado == "ganador" and contador % 2 != 0:
    print ("\n\n TENEMOS UN GANADOR, el ganador es X\n")
        
