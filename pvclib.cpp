#include "Arduino.h"
#include "pvclib.h"

#if HWTYPE == PVCSERVO
 #include <Servo.h>
 #include "pvcservo.h"
#endif

#if HWTYPE == PVCSTEPPER
 #include "pvcstepper.h"
#endif

int xPosition = 0;
int yPosition = 0;

const char goToCmd = 'G';
const char readCmd = 'R';
const char scanCmd = 'S';
const char decreaseCmd = 'D';
const char increaseCmd = 'I';

const int dataPin = A0;

void pvcSetup()
{
  #if HWTYPE == PVCSERVO
   pvcServoSetup();
  #endif
  
  #if HWTYPE == PVCSTEPPER
   pvcStepperSetup();
  #endif
}

void pvcLoop()
{
  byte cmd[10];
  
  clearCmd(cmd);

  getCmd(cmd);

  printCmd(cmd);

  runCmd(cmd);
}


void getCmd(byte cmd[10])
{
  int x = 0;
  while (Serial.available() > 0) {
    cmd[x] = Serial.read();
    x++;
    delay(100);
  }
}

void runCmd(byte cmd[10])
{
  if (cmd[0] != '\n')
  {
    char letter = cmd[0];

    if (letter == goToCmd)
    {
      goTo(cmd);
    }  
    else if (letter == increaseCmd)
    {
      increase(cmd);
    }
    else if (letter == decreaseCmd)
    {
      decrease(cmd);
    }
    else if (letter == readCmd)
    {
      readValue(cmd);
    }
    else
    {
      Serial.println("Invalid command");
    }
  }
}

void printCmd(byte cmd[10])
{
  if (cmd[0] != '\n')
  {
    Serial.print("Cmd:");
    for (int i = 0; i < 10; i++)
    {
      if (cmd[i] != '\n')
        Serial.print(char(cmd[i]));
    }
    Serial.println();
  }
}

void clearCmd(byte cmd[10])
{
  for (int i = 0; i < 10; i++)
  {
    cmd[i] = '\n';
  }
}

void goTo(byte cmd[10])
{  

  Serial.println("Going to...");

  char axis = char(cmd[1]);

  // Get the number of degrees (up to 3 digits)
  char buffer[3];
  buffer[0] = cmd[2];
  buffer[1] = cmd[3];
  buffer[2] = cmd[4];
  int degrees = atoi(buffer);

  if (axis == 'X')
    xPosition = degrees;
  else if (axis == 'Y')
    yPosition = degrees;

  Serial.print("Axis:");
  Serial.println(axis);
  Serial.print("Degrees:");
  Serial.println(degrees);
  
  gimbalGo(xPosition, yPosition);
}

void increase(byte cmd[10])
{  
  Serial.println("Increasing...");

  char axis = char(cmd[1]);

  // Get the number of degrees (up to 3 digits)
  char buffer[3];
  buffer[0] = cmd[2];
  buffer[1] = cmd[3];
  buffer[2] = cmd[4];
  int degrees = atoi(buffer);

  if (axis == 'X')
    xPosition += degrees;
  else if (axis == 'Y')
    yPosition += degrees;

  Serial.print("Axis:");
  Serial.println(axis);
  Serial.print("Degrees:");
  Serial.println(degrees);
  
  gimbalGo(xPosition, yPosition);
}

void decrease(byte cmd[10])
{  
  Serial.println("Decreasing...");

  char axis = char(cmd[1]);

  // Get the number of degrees (up to 3 digits)
  char buffer[3];
  buffer[0] = cmd[2];
  buffer[1] = cmd[3];
  buffer[2] = cmd[4];
  int degrees = atoi(buffer);

  if (axis == 'X')
    xPosition -= degrees;
  else if (axis == 'Y')
    yPosition -= degrees;

  Serial.print("Axis:");
  Serial.println(axis);
  Serial.print("Degrees:");
  Serial.println(degrees);
  
  gimbalGo(xPosition, yPosition);
}

void readValue(byte cmd[10])
{
  Serial.println("Reading value...");

  int numberOfReadings = 1;

  if (cmd[1] != '\n')
  {
    char buffer[3];
    buffer[0] = cmd[1];
    buffer[1] = cmd[2];
    buffer[2] = cmd[3];
    numberOfReadings = atoi(buffer);
  }

  Serial.print("Number of readings:");
  Serial.println(numberOfReadings);

  for (int i = 0; i < numberOfReadings; i++)
  {
    int reading = analogRead(dataPin);

    // Start the line with "D;" to indicate the rest of the line is data
    Serial.print("D:");
    Serial.print(reading);
    Serial.print(";X:");
    Serial.print(xPosition);
    Serial.print(";Y:");
    Serial.print(yPosition);
    Serial.println(";");
  }
}

void gimbalGo(int x, int y)
{
  #if HWTYPE == PVCSERVO
   servoGimbalGo(x, y);
  #endif
  
  #if HWTYPE == PVCSTEPPER
   stepperGimbalGo(x, y);
  #endif
}
