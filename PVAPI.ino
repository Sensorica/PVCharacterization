char goToCmd = 'G';
char readCmd = 'R';
char scanCmd = 'S';

void setup()
{
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }
}

void loop()
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

  char buffer[3];

  char axis = char(cmd[1]);

  buffer[0] = cmd[2];
  buffer[1] = cmd[3];
  buffer[2] = cmd[4];
  int xVal = atoi(buffer);

  Serial.print("Axis:");
  Serial.println(axis);
  Serial.print("Degrees:");
  Serial.println(xVal);
}

void readValue(byte cmd[10])
{
   Serial.println("Reading value...");
}

