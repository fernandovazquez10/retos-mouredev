def mostrar_marcador(marcador: dir): 
    pts_jugador_1 = marcador['P1']
    pts_jugador_2 = marcador['P2']
    if pts_jugador_1 == pts_jugador_2 and pts_jugador_1 >= 40:
        display_marcador = "Deuce"
    elif pts_jugador_1 <= 40 and pts_jugador_2 <= 40: 
        display_jugador_1 = "Love"
        display_jugador_2 = "Love"
        if pts_jugador_1 > 0:
            display_jugador_1 = f"{pts_jugador_1}"
        if pts_jugador_2 > 0:
            display_jugador_2 = f"{pts_jugador_2}"
        display_marcador = f"{display_jugador_1} - {display_jugador_2}"
    else: 
        diferencia_pts = abs(pts_jugador_1 - pts_jugador_2)
        if diferencia_pts > 3: 
            display_marcador = "Ventaja P1"
            if pts_jugador_2 > pts_jugador_1:
                display_marcador = "Ventaja P2"
            if diferencia_pts >= 12:
                display_marcador = "Ha ganado el P1"
                if pts_jugador_2 > pts_jugador_1:
                    display_marcador = "Ha ganado el P2"
        else:
            if diferencia_pts == 1:
                display_marcador = "Ventaja P1"
                if pts_jugador_2 > pts_jugador_1:
                    display_marcador = "Ventaja P2"
            else:
                display_marcador = "Ha ganado el P1"
                if pts_jugador_2 > pts_jugador_1:
                    display_marcador = "Ha ganado el P2"
    
    return display_marcador

marcador = {'P1': 0, 'P2': 0}
ganador = False
historial_marcadores = []

while not ganador:
    jugador = input("Ingrese el jugador que ha anotado (P1 ó P2): ")
    jugador = jugador.upper().strip()
    if jugador in ['P1', 'P2']:
        if marcador[jugador] < 30:
            marcador[jugador] += 15
        elif marcador[jugador] < 40:
            marcador[jugador] += 10
        else:
            marcador[jugador] += 1
        display_marcador = mostrar_marcador(marcador)
        historial_marcadores.append(display_marcador)
        if "Ha ganado el" in display_marcador:
            ganador = True
    else: 
        print(f"ADVERTENCIA: Jugador {jugador} no legible debe ser P1 ó P2")

print("_________________________________________")
print("Marcador")
for marcador in historial_marcadores:
    print(marcador)
print("_________________________________________")
