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


class PVDriver:

    """
    A class used to represent the bridge between a computer and an Arduino
    loaded with our firmware.
    """

    def __init__(self, port='/dev/ttyACM0', baud_rate=9600, *args, **kwargs):
        print("Hello world")
        self._arduino = serial.Serial(port, baud_rate, timeout=1)

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
        print("Set position to ({}, {})".format(tilt, rot))

    def _get_state(self):
        """
        Retrieve the current state of the device. The returned value can be one
        amongst the following list:
            * IDLE
            * MOVING
            * ERROR
        """
        pass

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
    driver.set_position(tilt=42.5)
    driver._arduino.write(bytearray("Sensorica", 'ascii'))
    print("Done.")
