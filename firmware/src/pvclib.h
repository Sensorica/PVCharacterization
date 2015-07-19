#ifndef pvclib_H_
#define pvclib_H_

void pvcSetup();

void pvcLoop();

void getCmd(char cmd[10]);

void runCmd(char cmd[10]);

void printCmd(char cmd[10]);

void clearCmd(char cmd[10]);

void goTo(char cmd[10]);

void readValue(char cmd[10]);

#endif /* pvclib_H_ */
