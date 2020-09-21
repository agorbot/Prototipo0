
const byte numChars = 6;
char receivedChars[numChars];

boolean newData = false;

void setup() {
    Serial.begin(9600);
    //Serial.println("<Arduino is ready>");
    pinMode(LED_BUILTIN, OUTPUT);
   
}

void loop() {
  //delay(10000);
  //Serial.println(Serial.available());  
    recibe_con_marcas();
    showNewData();
    
}

/////////////////////////////////////Recibe datos con inicio y fin, como ascii///////////////////////

void recibe_con_marcas() {
    static boolean recvInProgress = false;
    static byte ndx = 0;
    char startMarker = '<';
    char endMarker = '>';
    char rc;
 
  
    while (Serial.available() > 0 && newData == false) {
        rc = Serial.read();

        if (recvInProgress == true) {
            if (rc != (endMarker)) {
                receivedChars[ndx] = rc;
                ndx++;
                if (ndx >= numChars) {
                    ndx = numChars - 1;
                }
            }
            else {
                receivedChars[ndx] = '\0'; // terminate the string
                recvInProgress = false;
                ndx = 0;
                newData = true;
            }
        }
        else if (rc == (startMarker)) {
            recvInProgress = true;
        } 
    }
}

///////////////////////////////Hace algo con los datos recien recibidos (PID MOTORES, etc...)///////////////////

void showNewData() {
    if (newData == true) {
      delay(1000);
        //Serial.println(receivedChars);
        //Serial.print("This just in ... ");
        int recibidos = atoi(receivedChars); //convierte valor almacenado en recibidos a flotante con signo
        //Serial.println(receivedChars[0]);
        //Serial.print("como numero ... ");
        
        //Serial.println(recibidos);
        digitalWrite(LED_BUILTIN, HIGH);
        delay(2000);
        digitalWrite(LED_BUILTIN, LOW);
        delay(1000);
        newData = false;
        funcion(recibidos);

        //devolver();
    }
}
//////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////Hace algo (PID MOTORES, etc...)/////////////////////////////

char funcion(int entrada){

  int a = 0; 
  a=-entrada+3;
  protocolo(a);   

}

/////////////////////////////////// Para mandar valor ///////////////////////////////////////////

char protocolo(int valor){  //Genera valor a mandar a PC desde entero obtenido de algoritmo
  
  char valorAmandar[6];
    if (valor>0){ // Generar simbolo se signo
      valorAmandar[1] = '0';
  }
    else{
      valorAmandar[1] = '-';
      valor=valor*-1;
    }
    if (valor<10){ // Valor de las unidades
      valorAmandar[2] = '0'; 
      valorAmandar[3] = '0';
      valorAmandar[4] = (valor+'0');
      }
    
    if (valor<100 && valor>=10){  // Valor de las decenas
      valorAmandar[2] = '0';
      valorAmandar[3] = trunc(valor/10) + '0';
      valorAmandar[4] = (valor - (trunc(valor/10))*10)+'0';
      }  
   
   if (valor>100){  // Valor de las centenas
      valorAmandar[2]=trunc(valor/100)+'0';
      valorAmandar[3]=(trunc(valor/10)-(trunc(valor/100))*10)+'0';
      valorAmandar[4]=(valor - (trunc(valor/100))*100 -((trunc(valor/10)-(trunc(valor/100))*10))*10)+'0';
    }
    valorAmandar[0]='<';  //Inicio mensaje
    valorAmandar[5]='>';  //Fin mensaje
    //Serial.print ("Desde donde se arma la funcion ");
    
    Serial.print (valorAmandar[0]);
    Serial.print (valorAmandar[1]);
    Serial.print (valorAmandar[2]);
    Serial.print (valorAmandar[3]);
    Serial.print (valorAmandar[4]);
    Serial.print (valorAmandar[5]);



}
/////////////////////////////////////////////////////////////////////////
  
