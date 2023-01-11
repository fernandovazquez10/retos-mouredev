leet_speak = {
    'A': '4', 'B': 'I3', 'C': '[', 'D': ')', 'E': '3', 'F': '!=', 'G': '&',
    'H': '#', 'I': '1', 'J': ',_|', 'K': '>|', 'L': '1', 'M': '/\/\\',  'N': '^/', 
    'O': '0', 'P': '|*', 'Q': '(_,)', 'R': 'I2', 'S': '5', 'T': '7', 'U': '(_)', 
    'V': '\/', 'W': '\/\/', 'X': '><', 'Y': 'j', 'Z': '2'
}

mensaje = str(input('Ingrese el mensaje que desea encriptar: '))
mensaje_leeteado = ""
for caracter in mensaje:
    if leet_speak.get(caracter.upper(), None):
        mensaje_leeteado += leet_speak[caracter.upper()]
    else: 
        mensaje_leeteado += caracter
print(f"Mensaje encriptado: {mensaje_leeteado}")
