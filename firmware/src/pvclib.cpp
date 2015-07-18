#include "Arduino.h"
#include "pvclib.h"

int xPosition = 0;
int yPosition = 0;

const char CMD_GOTO = 'G';
const char CMD_READ = 'R';
const char CMD_SCAN = 'S';

const int DATA_PIN = A0;

void pvcSetup()
{ 
  //TODO
}

/*
 * The main loop of the firmware. On each iteration, the loop takes the following steps:
 *     * Clear the command cache
 *     * Get the next command to be executed from the serial port
 *     * Print out the command that has been parsed
 *     * Run the command
 */
void pvcLoop()
{
  byte cmd[10];
  
  clearCmd(cmd);

  getCmd(cmd);

  printCmd(cmd);

  runCmd(cmd);
}


/*
 * Cleans up the command variable.
 */
void clearCmd(byte cmd[10])
{
  for (int i = 0; i < 10; i++)
  {
    cmd[i] = '\n';
  }
}


/*
 * Assumes `cmd` has been previously cleaned by `clearCmd`.
 * This function fetches data from the serial port and loads a new
 * command in `cmd` to be executed by the Arduino.
 */
void getCmd(byte cmd[10])
{
  int x = 0;
  while (Serial.available() > 0) {
    cmd[x] = Serial.read();
    x++;
    delay(100);
  }
}


/*
 * Prints out the command to be executed to the serial monitor.
 */
void printCmd(byte cmd[10])
{
  if (cmd[0] != '\n')
  {
    Serial.print("Command to be executed: ");
    for (int i = 0; i < 10; i++)
    {
      if (cmd[i] != '\n')
        Serial.print(char(cmd[i]));
    }
    Serial.println();
  }
}


/*
 * Parses the command to be executed (10 bytes long) and run the appropriate
 * low-level function.
 */
void runCmd(byte cmd[10])
{
  if (cmd[0] != '\n')
  {
    char letter = cmd[0];

    if (letter == CMD_GOTO)
    {
      goTo(cmd);
    }  
    else if (letter == CMD_READ)
    {
      readValue(cmd);
    }
    else
    {
      Serial.println("Invalid command");
    }
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
  
  //gimbalGo(xPosition, yPosition);
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
    int reading = analogRead(DATA_PIN);

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
