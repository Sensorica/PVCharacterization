#include "Arduino.h"

#define PVCSERVO 1
#define PVCSTEPPER 2

#define HWTYPE PVCSERVO // Specify hardware type here (PVCSERVO or PVCSTEPPER)

#if HWTYPE == PVCSERVO
 #include <Servo.h>
 #include "pvcservo.h"
#endif

#if HWTYPE == PVCSTEPPER
// TODO: Add stepper includes
#endif

#include "pvclib.h"

void setup()
{
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }
  
  pvcSetup();
}

void loop()
{
  pvcLoop();

}




