#include <PID_v1.h>

int PIN_POSICION = A0; // Posición enviada por la camara.
int PIN_CONTROL = 13; // Señal de control para motores
int PIN_SETPOINT = A3; // SetPoint deseado ( el centro de la linea es la posicion deseada, sera = 0)

int motor1Forward = 2; 
int motor1Backward = 3;
int motor1pwmPin = 10;
int motor2Forward = 5;
int motor2Backward = 6;
int motor2pwmPin = 11;
int motor1newSpeed;
int motor2newSpeed;
int motor2Speed = 10; //Default 70
int motor1Speed = 10; //Default 120


//Define Variables we'll be connecting to... todas deben estar en la misma unidad.
double Setpoint, Input, Output;

//Specify the links and initial tuning parameters (GANANCIAS)
double Kp=10, Ki=5, Kd=0;
PID myPID(&Input, &Output, &Setpoint, Kp, Ki, Kd, DIRECT);

void setup()
{
   Serial.begin(9600);

  pinMode(motor1Forward, OUTPUT);
  pinMode(motor1Backward, OUTPUT);
  pinMode(motor1pwmPin, OUTPUT);
  pinMode(motor2Forward, OUTPUT);
  pinMode(motor2Backward, OUTPUT);
  pinMode(motor2pwmPin, OUTPUT);
  
  Input = Serial.read(); 
  Setpoint = 0; //
  myPID.SetMode(AUTOMATIC);  //turn the PID on
}

void loop()
{
   while(Serial.available()){
   Input = Serial.read(); //Read user input and trigger appropriate function
   }
  
  myPID.Compute();
  
   Ajuste();
  Serial.println(motor1newSpeed);
  
}

void Ajuste() {
  //Cambia la velocidad del motor proporcionalmente sumando la accion de control a un motor y restandola en el otro.
  motor2newSpeed = motor2Speed + Output;
  motor1newSpeed = motor1Speed - Output;
  // Ajusta el rango de 0- 1024 a 0-255 (Salida PWM Arduino)
  constrain(motor2newSpeed, 0, 255);
  constrain(motor1newSpeed, 0, 255);
  //El  carro avanza con la velocidad ajustada
  analogWrite(motor2pwmPin, motor2newSpeed);
  analogWrite(motor1pwmPin, motor1newSpeed);
  digitalWrite(motor2Forward, HIGH);
  digitalWrite(motor2Backward, LOW);
  digitalWrite(motor1Forward, HIGH);
  digitalWrite(motor1Backward, LOW);
}
