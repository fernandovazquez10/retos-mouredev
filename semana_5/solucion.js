leat_speak = {
    'A': '4', 'B': 'I3', 'C': '[', 'D': ')', 'E': '3', 'F': '!=', 'G': '&',
    'H': '#', 'I': '1', 'J': ',_|', 'K': '>|', 'L': '1', 'M': "/\\/\\", 'N': '^/', 
    'O': '0', 'P': '|*', 'Q': '(_,)', 'R': 'I2', 'S': '5', 'T': '7', 'U': '(_)', 
    'V': '\/', 'W': '\/\/', 'X': '><', 'Y': 'j', 'Z': '2'
};

var mensaje_leeteado = "El mensaje encriptado es: ";
var mensaje;

mensaje = prompt("ingrese el mensaje que desea cifrar: ");
for (var i in mensaje){
    let caracter = mensaje.charAt(i).toUpperCase();
    if (leat_speak[caracter] !== undefined){
        mensaje_leeteado = mensaje_leeteado + leat_speak[caracter];
    }
    else{
        mensaje_leeteado = mensaje_leeteado + caracter;
    }
} 
alert(mensaje_leeteado)
