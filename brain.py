#Tateti-Raya en consola, version= super develop finalizado en el main.py
import sys
player1 = input("nombre player 1: ")
player2 = input("nombre player 2: ")

gana = []

tablero = ["1","2","3","4","5","6","7","8","9"]
tableroControl = [0, 1, 2, 3, 4, 5, 6, 7, 8]
total_mueve = 0
fin = False
Turno = player1

def check_win(tablero):
    posibles = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[2,4,6],[0,4,8]]
    for y in range(8):
        primera = posibles[y]
        marca = ""
        gana=0
        for t in range(3): #range 3 recorre cada posibilidad
            gg = primera[t]
            x = tablero[gg]
            if x == "x":
                if (marca == "o"):
                    gana = gana - 1
                else:
                    gana = gana + 1
                    marca = "x"
            elif x == "o":
                if marca == "x":
                    gana = gana -1
                else:
                    marca = "o"
                    gana = gana +1
            if gana == 3:
                return True
    return False

def marca_tablero(tableroControl, valor,total_mueve):
    index = 0
    for x in range(len(tableroControl)):
        if x == (int(valor) -1):
            if tableroControl[x] == "--":
                index = "--"
                break
            else:
                tableroControl[x] = "--"
                index = x
                total_mueve += 1
                break
    return index, total_mueve

while (not fin):
    print(tablero[6]," ",tablero[7]," ",tablero[8])
    print(tablero[3]," ",tablero[4]," ",tablero[5])
    print(tablero[0]," ",tablero[1]," ",tablero[2])
    print(total_mueve)
    if total_mueve < 9:
        print(tableroControl)
        mensaje = "Turno de %s:" % Turno
        valor = input(mensaje)
        posMarcar, total_mueve = marca_tablero(tableroControl, valor,total_mueve)
        if Turno == player1:
            if posMarcar != "--":
                tablero[posMarcar] = "x"
                Turno = player2
        else:
            if posMarcar != "--":
                tablero[posMarcar] = "o"
                Turno = player1
        gana = check_win(tablero)
        print(gana)
        if gana:
            print(tablero[6], " ", tablero[7], " ", tablero[8])
            print(tablero[3], " ", tablero[4], " ", tablero[5])
            print(tablero[0], " ", tablero[1], " ", tablero[2])
            if Turno == player1:
                print("gano: ",player2)
            else:
                print("gano: ",player1)
            fin = True
    else:
        print("NO Hubo Ganadores")
        fin = True
sys.exit(0)

