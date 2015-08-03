#ifndef pvclib_H_
#define pvclib_H_

void pvcSetup();

void pvcLoop();

void getCmd(byte cmd[10]);

void runCmd(byte cmd[10]);

void printCmd(byte cmd[10]);

void clearCmd(byte cmd[10]);

void identify();

void goTo(byte cmd[10]);

void increase(byte cmd[10]);

void decrease(byte cmd[10]);

void readValue(byte cmd[10]);

void gimbalGo(int x, int y);

#endif /* pvclib_H_ */
