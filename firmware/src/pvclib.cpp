#include "Arduino.h"
#include "pvclib.h"

#define CMD_MAX_LENGTH 20

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
  char cmd[CMD_MAX_LENGTH];
  
  clearCmd(cmd);

  getCmd(cmd);

  // printCmd(cmd);

  runCmd(cmd);
}


/*
 * Cleans up the command variable.
 */
void clearCmd(char cmd[CMD_MAX_LENGTH])
{
  for (int i = 0; i < CMD_MAX_LENGTH; i++)
  {
    cmd[i] = '\n';
  }
}


/*
 * Assumes `cmd` has been previously cleaned by `clearCmd`.
 * This function fetches data from the serial buffer and loads a new
 * command in `cmd` to be executed by the Arduino.
 *
 * Incoming commands have the following syntax:
 *       <operand>[,<arg>];
 * The semi-colon (';') marking the end of the command.
 */
void getCmd(char cmd[CMD_MAX_LENGTH])
{
  int x = 0;
  while (Serial.available() > 0) {
    cmd[x] = Serial.read();
    if (char(cmd[x]) == ';') {
      // We have reached the end of the command and previous calls
      // to Serial.read() have removed the command from the serial buffer.
      cmd[x] = '\0';
      break;
    }
    x++;
    delay(100);
  }
}


/*
 * Prints out the command to be executed to the serial output.
 * Useful for debugging but should not be used in production.
 */
void printCmd(char cmd[CMD_MAX_LENGTH])
{
  if (cmd[0] != '\n')
  {
    Serial.print("CMD: ");
    for (int i = 0; i < CMD_MAX_LENGTH; i++)
    {
      if (cmd[i] != '\n')
        Serial.print(char(cmd[i]));
    }
    Serial.println();
  }
}


/*
 * Parses the command to be executed (CMD_MAX_LENGTH char long) and run the appropriate
 * low-level function.
 */
void runCmd(char cmd[CMD_MAX_LENGTH])
{
  char operand[6];
  float argument;

  if (cmd[0] != '\n')
  {
    char cmd_copy[CMD_MAX_LENGTH];
    char* parsed;
    strcpy(cmd_copy, cmd);
    char* delimiters = ",";

    parsed = strtok(cmd_copy, delimiters);
    if (parsed != NULL) {
      strcpy(operand, parsed);
      parsed = strtok(NULL, delimiters);
      if (parsed != NULL) {
        argument = atof(parsed);
      }
    }

    // At this point, operand and argument are populated.
    // Start interpreting.
    
    // READ STATE
    if (strcmp(operand, "RS") == 0) {
      Serial.println("STATE:1");
    }

    if (strcmp(operand, "GT") == 0) {
      // do some stuff...
    }
  }

}


void goTo(char cmd[CMD_MAX_LENGTH])
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

void readValue(char cmd[CMD_MAX_LENGTH])
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
