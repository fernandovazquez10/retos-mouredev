import "dart:io";

String mostrarMarcador(Map marcador) {
    int puntosJugador1 = marcador["P1"];
    int puntosJugador2 = marcador["P2"];
    var marcadorFinal = "";
    var marcadorJugador1 = "";
    var marcadorJugador2 = "";
    if (puntosJugador1 == puntosJugador2 && puntosJugador1 >= 40){
        marcadorFinal = "Deuce";
    } else if(puntosJugador1 <= 40 && puntosJugador2 <= 40){
        marcadorJugador1 = "Love";
        marcadorJugador2 = "Love";
        if (puntosJugador1 > 0){
            marcadorJugador1 = puntosJugador1.toString();
        }
        if (puntosJugador2 > 0){
            marcadorJugador2 = puntosJugador2.toString();
        }
        marcadorFinal= marcadorJugador1 + "-" + marcadorJugador2;
    } else {
        int diferenciaPuntos = puntosJugador1 - puntosJugador2;
        diferenciaPuntos = diferenciaPuntos.abs();
        if (diferenciaPuntos > 3){
            marcadorFinal = "Ventaja P1";
            if (puntosJugador2 > puntosJugador1){
                marcadorFinal = "Ventaja P2";
            }
            if (diferenciaPuntos > 12){
                marcadorFinal = "Ha ganado el P1";
                if (puntosJugador2 > puntosJugador1){
                    marcadorFinal = "Ha ganado el P2";
                }
            }
        } else {
            if (diferenciaPuntos == 1){
                marcadorFinal = "Ventaja P1";
                if (puntosJugador2 > puntosJugador1){
                    marcadorFinal = "Ventaja P2";
                }
            } else {
                marcadorFinal = "Ha ganado el P1";
                if (puntosJugador2 > puntosJugador1){
                    marcadorFinal = "Ha ganado el P2";
                }
            }
        }
    }

    return marcadorFinal;
}


void main(){
    Map marcador = {
        "P1": 0, 
        "P2": 0
        };
    bool ganador = false;
    List historialMarcadores = [];
    
    while (ganador == false){
        stdout.write("Ingrese el jugador que ha anotado(P1 o P2): ");
        String? jugador = stdin.readLineSync();
        if (jugador == "P1" || jugador == "P2"){
            if (marcador[jugador] < 30){
                marcador[jugador] += 15;
            } else if (marcador[jugador] < 40){
                marcador[jugador] += 10;
            } else {
                marcador[jugador] += 1;
            }
            String displayMarcador = mostrarMarcador(marcador);
            historialMarcadores.add(displayMarcador);
            if (displayMarcador.contains("Ha ganado el") == true){
                ganador = true;
            }
        }else {
            stdout.write("Jugador inelegible.");
        }
    }

    print("-------------------------------");
    print("Marcador");
    for (final marcadorFinal in historialMarcadores){
        print(marcadorFinal);
    }
    print("--------------------------------");
}
