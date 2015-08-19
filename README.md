# PVCharacterization

The aim of the project is to design and create a tool for optical characterization of thin and transparent materials. More details can be found on [the official website](http://www.sensorica.co/home/what-we-do/projects/pv-characterization).

## How to run the whole thing
1. Clone the repo
2. Install all the dependencies (see below)
3. Plug the Arduino in (on a USB port of your laptop)
4. Build the firmware and upload it to the board. With `ino` this is as simple as

    ```console
    $ cd PVCharacterization/firmware
    $ ino build   # Build the firmware (may take up to a few seconds)
    $ ino upload  # Upload
    ```

5. Run the driver test suite. On Linux or MacOS this gives:

    ```console
    $ cd PVCharacterization
    $ source venv/bin/activate  # skip this if you are not using a virtualenv
    (venv)$ cd driver
    (venv)$ python driver.py   # if you are not using a virtualenv, make sure you are using python3
    ```


## Dependencies

The way to install the dependencies may vary depending on your machine. Keep in mind that this project is targeting a Debian system.

### Python Client
* Python 3
* PySerial

Using `pip3` you can install all the python requirements with

```console
$ pip3 install -r requirements.txt
```

We strongly recommand to use a [`virtualenv`](https://virtualenv.pypa.io/en/latest/) in order to build an isolate development environment.

### Arduino Firmware
* [Ino](http://inotool.org/) (optional)

## Structure
The repository contains 4 main components:

* The **Arduino firmware** that is in charge of controlling the electro-mechanical system.
* The cross-platform **driver** allowing a Python application to communicate with the firmware living in the Arduino.
* The core **application** that is in charge of defining higher level features and that uses the driver to communicate with the Arduino.
* The **GUI** of the laptop application.

### Arduino firmware
The source code of the Arduino firmware is found under `firmware/src`. You can either use the official IDE to build the binaries and upload them to your Arduino, or you can use the [Ino CLI](http://inotool.org/):

```console
$ ino build # a .build directory is created containing the firmware ready to be uploaded
$ ino upload
```

 If you do use Ino, you may have to edit the configuration file `ino.ini`.
 
### Driver
The driver can be found under [PVCharacterization/driver/driver.py](https://github.com/Sensorica/PVCharacterization/blob/dev/driver/driver.py).
 
### Core application
 TODO
 
### GUI
 TODO
