from string import ascii_lowercase

def es_heterograma(texto: str) -> bool:
    es_heterograma : bool = True
    letras = []
    for letra in texto:
        if not letra.lower() in letras:
            letras.append(letra.lower())
        else: 
            es_heterograma = False
            break
    return es_heterograma

def es_isograma(texto: str) -> bool:
    es_isograma : bool = True
    letras = {}
    for letra in texto:
        if letra in letras.keys():
            letras[letra] += 1
        else:
            letras[letra] = 1
    if len(set(letras.values())) > 1:
        es_isograma = False
    return es_isograma

def es_pangrama(texto: str) -> bool: 
    es_pangrama : bool = True
    alfabeto = list(ascii_lowercase)
    for letra in alfabeto:
        if not letra in texto.lower():
            es_pangrama = False
            break
    return es_pangrama

texto = input("Ingrese un texto: ")
heterograma = es_heterograma(texto)
isograma = es_isograma(texto)
pangrama = es_pangrama(texto)

if heterograma:
    print("Es un heterograma.")
else:
    print("No es un heterograma.")

if isograma:
    print("Es un isograma.")
else: 
    print("No es un isograma.")

if pangrama:
    print("Es un pangrama.")
else: 
    print("No es un pangrama.")

