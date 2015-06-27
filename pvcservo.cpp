#include "Arduino.h"
#include <Servo.h>
#include "pvcservo.h"

const int servoXPin = 8;
const int servoYPin = 9; 

Servo servoX;
Servo servoY;

void pvcServoSetup()
{
  servoX.attach(servoXPin);  // attaches the servo
  servoY.attach(servoYPin);  // attaches the servo
}

void gimbalGo(int x, int y)
{
  int xPosition = 0;
  int yPosition = 0;
  
  /*Serial.print("Moving servo - ");
  Serial.print("X:");
  Serial.print(x);
  Serial.print(";Y:");
  Serial.println(y);*/
  
  int mappedX = map(x, 0, 90, 90, 0);
  int mappedY = map(y, 0, 90, 90, 0);
  
  /*Serial.print("Mapped X:");
  Serial.println(mappedX);
  
  Serial.print("Mapped Y:");
  Serial.println(mappedY);*/
  
  servoX.write(mappedX);
  delay(15);
  
  servoY.write(mappedY);
  delay(15);
}
