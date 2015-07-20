"""
driver.py
---------
The driver module for the PVCharacterization project.

This module defines the `PVDriver` class that can be instanciated to
communicate with an Arduino loaded with our firmware. Call any of
the public methods on a PVDriver object in order to send a command
to the slave device over the serial port.
"""

import serial
import time


class PVDriver:

    """
    A class used to represent the bridge between a computer and an Arduino
    loaded with our firmware.
    """

    # State constants are defined in a static way
    IDLE = 0
    MOVING = 1
    ERROR = -1

    def __init__(self, port='/dev/ttyACM0', baud_rate=9600, *args, **kwargs):
        print("Hello world")
        self._arduino = serial.Serial(port, baud_rate, timeout=1)

    def close_connexion(self):
        self._arduino.close()

    def get_position(self, unit='degree'):
        """
        Retrieve the current absolute tilt and rotation angles of the device.
        Return a tuple (ti, rot) containing the current state expressed in
        degree by default.
        """
        return (0.0, 0.0)

    def set_position(self, tilt=None, rot=None, unit='degree', relative=False):
        """
        Send a new position setpoint to the device. Both `tilt` and `rot`
        are set as optional parameters to allow rotation on a single axis.

        Unless stated otherwise, angles are expressed in degree.

        Unless stated otherwise, positions are set as absolute. If you want
        to move the device relatively to its current position, set `relative`
        to True in the parameters.
        Example, rotate +2° on the tilt axis and -5° on the rot axis:

            driver = PVDriver()
            driver.set_position(tilt=2, rot=-5, relative=True)

        Example if you want to set the absolute tilt angle and leave the
        rotation angle unchanged:

            driver.set_position(tilt=76.42)

        Calling `set_position` without any argument is useless as it won't
        have any impact on the current setpoint.
        """
        if tilt and rot:
            # We need to call goToTilt and goToRot subsequently
            print("Both a tilt and rotation angles have been provided.")
            if relative:
                cmd_tilt = "GTR," + str(tilt) + ';'
                cmd_rot = "GRR," + str(rot) + ';'
            else:
                cmd_tilt = "GT," + str(tilt) + ';'
                cmd_rot = "GR," + str(rot) + ';'
            self._send_command(cmd_tilt)
            self._send_command(cmd_rot)

        elif tilt:
            print("Only a tilt angle was provided.")
            if relative:
                cmd = "GTR," + str(tilt) + ';'
            else:
                cmd = "GT," + str(tilt) + ';'
            self._send_command(cmd)

        elif rot:
            print("Only a rotation angle was provided")
            if relative:
                cmd = "GRR," + str(rot) + ';'
            else:
                cmd = "GR," + str(rot) + ';'
            self._send_command(cmd)

        else:
            print("You did not provide any angle. Nothing to do here.")
            pass

    def _send_command(self, cmd, fb_required=False, res_pattern=None):
        """
        Takes a string command in parameter and sends it to the Arduino.
        If the provided command requires an answer from the Arduino, then
        lock the process until we receive the response and return it.
        """
        self._arduino.write(bytearray(cmd, 'ascii'))
        if fb_required:
            if not res_pattern:
                raise RuntimeError("You can't use fb_required without"
                                   " providing a response pattern. Usage: "
                                   "_send_command(cmd, "
                                   "             fb_required=True, "
                                   "             res_pattern=<some_string>")
            print("This is a blocking command. Waiting for feedback from the"
                  " Arduino.")
            res = self._arduino.readline().decode('utf-8')
            while res_pattern not in res:
                time.sleep(0.1)
                res = self._arduino.readline().decode('utf-8')
            return res

    def _get_state(self):
        """
        Retrieve the current state of the device. The returned value can be one
        amongst the following list:
            * 0  = IDLE
            * 1  = MOVING
            * -1 = ERROR
        """
        res = self._send_command(
                        "RS;",
                        fb_required=True,
                        res_pattern="STATE:")
        # The received answer is supposed to be something like
        #         STATE:0|1|-1
        state = int(res.split(':')[1])
        return state

    def _get_controller_parameters(self):
        """
        Retrieve the current values of the feedback controller (PID) gains.
        """
        pass

    def _set_controller_parameters(self, P=None, I=None, D=None):
        """
        Update the feedback controller gains.
        """
        pass

if __name__ == '__main__':
    print("Starting tests...")
    driver = PVDriver()
    driver.set_position(rot=2.8)
    driver.set_position(rot=67.8, tilt=28, relative=True)
    driver._get_state()
    driver.close_connexion()
    print("Done.")
