class QueSos{
  int numero;

  QueSos(this.numero){}

  bool esFibbonacci(){
    int n_1 = 0;
    int n_2 = 1;
    int c = -1;
    int aux = 0; 
    bool continuar = true;
    bool fibbonacci = false;

    while (continuar == true){
      c++;
      if (c==0){
        aux = n_1;
      }else if (c==1){
        aux = n_2;
      } else {
        aux = n_1 + n_2;
        n_1 = n_2;
        n_2 = aux;
      }
      if (numero == aux){
        continuar = false;
        fibbonacci = true;
      }else if (numero < aux){
        continuar = false;
      }
    }
    return fibbonacci;
  }

  bool esPrimo(){
      int n = 2;
      bool primo = false;
      while (n < numero){
        if (numero % n == 0 ){
          primo = true;
        }
        n++;
      }
      return primo;
  }

  bool esPar(){
    bool par = false;
    if (numero % 2 == 0){
      par = true;
    }
    return par;
  }

  String display(){
    var esPrimoString = "no es primo";
    if (esPrimo()){
      esPrimoString = "es primo";
    }
    var esFibbonacciString = "no es fibonacci";
    if (esFibbonacci()){
      esFibbonacciString = "es fibonacci";
    }
    var esParString = "no es par";
    if (esPar()){
      esParString = "es par";
    }
    final display = "$numero $esPrimoString, $esFibbonacciString, $esParString";
    return display;
  }

}


void main(){
  final numero = QueSos(8);
  print(numero.display());
}
