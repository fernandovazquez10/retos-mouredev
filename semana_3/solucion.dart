import 'dart:math';


class PasswordGenerator{
  int longitud;
  bool con_mayusculas;
  bool con_numeros;
  bool con_simbolos;

  PasswordGenerator(this.longitud, this.con_mayusculas, this.con_numeros, this.con_simbolos)
  : assert(
    longitud >= 8 && longitud <= 16,
    "Longitud debe ser un valor entre 8 y 16",
  );

  List obtener_letras(){
    var letrasList = [];
    const letras = "abcdefghijklmnopqrstuvwxyz";
    for (int posicion=0; posicion< letras.length; posicion++){
      letrasList.add(letras[posicion]);
    }
    return letrasList;
  }

  List obtener_simbolos(){
    List simbolosLista = [];
    const simbolos = "!#%&/()=?-.,@";
    for (int posicion=0; posicion < simbolos.length; posicion++){
      simbolosLista.add(simbolos[posicion]);
    }
    return simbolosLista;
  } 

  List obtener_numeros(){
    List numerosLista = [];
    for (int i=0; i < 10; i++){
      numerosLista.add(i.toString());
    }
    return numerosLista;
  }

  String generar(){
    List passwordList = [];
    List letras = obtener_letras();
    List caracteresDisponibles = [];
    final letrasSoporte = obtener_letras();
    final _random = new Random();
  
    if (con_mayusculas){
      for (int posicion = 0; posicion < letrasSoporte.length; posicion++){
        letras.add(letrasSoporte[posicion].toUpperCase());
      }
    }
    caracteresDisponibles += letras;
    if (con_numeros){
      caracteresDisponibles += obtener_numeros();
    }
    if (con_simbolos){
      caracteresDisponibles += obtener_simbolos();
    }
    for (int i = 0; i < longitud; i++){
      var caracter = caracteresDisponibles[_random.nextInt(caracteresDisponibles.length)];
      passwordList.add(caracter);
    }
    String password = passwordList.join("");
    return password;
  }
}

void main(){
  var passwordGenerator = PasswordGenerator(15, true, true, true);
  final password = passwordGenerator.generar(); 
  print("Su nueva contraseña es: $password");
}
