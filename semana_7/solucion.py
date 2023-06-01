casas = {
    1: {'nombre': 'Gryffindor', 'puntos': 0},
    2: {'nombre': 'Slytherin', 'puntos': 0},
    3: {'nombre': 'Hufflepoff', 'puntos': 0},
    4: {'nombre': 'Revenclaw', 'puntos': 0},
}

preguntas = []
pregunta_1 = """Situación no.1
1.- Respuesta gryffindor
2.- Respuesta Slytherin
3.- Respuesta hufflepoff
4.- Respuesta revenclaw
"""
preguntas.append(pregunta_1)

pregunta_2 = """Situación no.2
1.- Respuesta gryffindor
2.- Respuesta Slytherin
3.- Respuesta hufflepoff
4.- Respuesta revenclaw
"""
preguntas.append(pregunta_2)

pregunta_3 = """Situación no.3
1.- Respuesta gryffindor
2.- Respuesta Slytherin
3.- Respuesta hufflepoff
4.- Respuesta revenclaw
"""
preguntas.append(pregunta_3)

pregunta_4 = """Situación no.4
1.- Respuesta gryffindor
2.- Respuesta Slytherin
3.- Respuesta hufflepoff
4.- Respuesta revenclaw
"""
preguntas.append(pregunta_4)

pregunta_5 = """Situación no.5
1.- Respuesta gryffindor
2.- Respuesta Slytherin
3.- Respuesta hufflepoff
4.- Respuesta revenclaw
"""
preguntas.append(pregunta_5)

for pregunta in preguntas:
    print(pregunta)
    respuesta = int(input("Ingrese el numero de su respuesta: "))
    while not respuesta in range(1, 5):
        print("Respuesta invalida")
        respuesta = int(input("Ingrese el numero de su respuesta: "))
    casas[respuesta]['puntos'] += 1


