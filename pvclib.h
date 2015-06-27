#ifndef pvclib_H_
#define pvclib_H_

void pvcSetup();

void pvcLoop();

void getCmd(byte cmd[10]);

void runCmd(byte cmd[10]);

void printCmd(byte cmd[10]);

void clearCmd(byte cmd[10]);

void goTo(byte cmd[10]);

void readValue(byte cmd[10]);

#endif /* pvclib_H_ */
