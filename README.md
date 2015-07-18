# PVCharacterization

The aim of the project is to design and create a tool for optical characterization of thin and transparent materials. More details can be found on [the official website](http://www.sensorica.co/home/what-we-do/projects/pv-characterization).

## Dependencies
### Firmware
TODO

### Client
* Python >=3.4
* PySerial

Using `pip` you can install all the requirements with

```console
$ pip install -r requirements.txt
```

## Structure
The repository contains 3 main components:

* The **Arduino firmware** that is in charge of controlling the electro-mechanical system (found under `firmware`)
* The cross-platform **driver** allowing a computer to communicate with the firmware living in the Arduino (found under `driver`)
* The **GUI** of the laptop application (found under `GUI`)

### Arduino firmware
The source code of the Arduino firmware is found under `firmware/src`. You can either use the official IDE to build the binaries and upload them to your Arduino, or you can use the [Ino CLI](http://inotool.org/):

```console
$ ino build # a .build directory is created containing the firmware ready to be uploaded
$ ino upload
```

 If you do use Ino, you may have to edit the configuration file `ino.ini`.
