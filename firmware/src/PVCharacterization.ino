/*
 * PVCharacterization.ino
 * ----------------------
 *
 * This is the top level Arduino sketch. It calls the control libraries and all the
 * components developed for the device firmware.
 */

#include "Arduino.h"

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




