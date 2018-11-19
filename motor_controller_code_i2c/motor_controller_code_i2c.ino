#include <Wire.h>
#include <Servo.h>

#define SLAVE_ADDRESS 12

int enA = 6;
int in1 = 8;
int in2 = 7;
int servoPIN = 10;

Servo steeringServo;


void setup() {
  Serial.begin(9600);
  Wire.begin(SLAVE_ADDRESS);
  Wire.onReceive(receiveData);
  pinMode(enA, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  steeringServo.attach(servoPIN);
}


void loop() {
  delay(100);
}


void receiveData(int byteCount) {
  int cmd[3];
  int i = 0;
  
  while(Wire.available()) {
    cmd[i] = Wire.read();
    i++;
  }

  // send the throttle value to the motor
  analogWrite(enA, cmd[1]);
  digitalWrite(in1, 1);
  digitalWrite(in2, 0);

  // send the steering value to the servo
  steeringServo.write(cmd[2]);
}
