#!/usr/bin/python3

from gi.repository import Gtk as gtk, Gdk as gdk
import time
import serial
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)

class PV:

    def statusbar_error(self, message):
        self.status_count += 1
        self.statusbar.push(self.context_id, "Error: {0}".format(message))
        time.sleep(1)

    def serial_read_x(self, current_x):
        string = ("par angleOffsetPitch")
        ser.write(bytearray(string, 'ascii'))
        time.sleep(1)
        ser.flushInput()
        time.sleep(0.1)
        incoming = ser.readline().decode('utf-8')
        incoming = incoming.strip()
        incoming = incoming.split(" ")
        current_x = incoming[1]
        current_x = int(current_x)
        return current_x

    def serial_read_y(self, current_y):
        string = ("par angleOffsetRoll")
        ser.write(bytearray(string, 'ascii'))
        time.sleep(1)
        ser.flushInput()
        time.sleep(0.1)
        incoming = ser.readline().decode('utf-8')
        incoming = incoming.strip()
        incoming = incoming.split(" ")
        current_y = incoming[1]
        current_y = int(current_y)
        return current_y

    def serial_push_x(self, x):
        string = ("par angleOffsetPitch {0}".format(x))
        ser.write(bytearray(string, 'ascii'))
        print("par angleOffsetPitch {0}".format(x))

    def serial_push_y(self, y):
        string = ("par angleOffsetRoll {0}".format(y))
        ser.write(bytearray(string, 'ascii'))
        print("par angleOffsetRoll {0}".format(y))

    def statusbar_update(self, x, y):
        self.status_count += 1
        self.statusbar.push(self.context_id, "Pitch(X): {0}  Roll(Y): {1}".format(x,y))

    def close_connection(self):
        ser.close()

    def on_window1_destroy(self, object, data=None):
        print ("quit with cancel")
        gtk.main_quit()

    def on_gtk_quit_activate(self, meunuitem, data=None):
        print ("quit from menu")
        gtk.main_quit()

    def on_gtk_about_activate(self, menuitem, data=None):
        print ("help about selected")
        self.response = self.aboutdialog.run()
        self.aboutdialog.hide()

    def on_goto_button_clicked(self, button, data=None):
        self.x_entry = self.builder.get_object("x_entry")
        self.x = (self.x_entry.get_text())
        xGoTo = (self.x)
        xGoTo = float(xGoTo)
        self.y_entry = self.builder.get_object("y_entry")
        self.y = (self.y_entry.get_text())
        yGoTo = (self.y)
        yGoTo = float(yGoTo)
        xGoTo = xGoTo*100
        yGoTo = yGoTo*100
        xGoTo = int(xGoTo)
        yGoTo = int(yGoTo)
        current_x = 0
        current_y = 0
        xStart = self.serial_read_x(current_x)
        print(xStart)
        yStart = self.serial_read_y(current_y)
        print(yStart)
        if xGoTo > 8000 or xGoTo < -8000 or yGoTo > 8000 or yGoTo < -8000:
            self.statusbar_error("Not in range")
        else:
            if xStart == xGoTo and yStart == yGoTo:
                self.statusbar_error("Already there!")
                while gtk.events_pending():
                    gtk.main_iteration()
            else:
                if xStart > xGoTo:
                    for x in range(xStart, xGoTo-10, -10):
                        self.statusbar_update(x, yStart)
                        self.serial_push_x(x)
                        time.sleep(0.1)
                        while gtk.events_pending():
                            gtk.main_iteration()
                elif xStart < xGoTo:
                    for x in range(xStart, xGoTo+10, 10):
                        self.statusbar_update(x, yStart)
                        self.serial_push_x(x)
                        time.sleep(0.1)
                        while gtk.events_pending():
                            gtk.main_iteration()
                else:
                    self.statusbar_update(xStart, yStart)
                    time.sleep(0.1)
                    while gtk.events_pending():
                        gtk.main_iteration()
                    x = xStart

                if yStart > yGoTo:
                    for y in range(yStart, yGoTo-10, -10):
                        self.statusbar_update(x, y)
                        self.serial_push_y(y)
                        time.sleep(0.1)
                        while gtk.events_pending():
                            gtk.main_iteration()
                elif yStart < yGoTo:
                    for y in range(yStart, yGoTo+10, 10):
                        self.statusbar_update(x, y)
                        self.serial_push_y(y)
                        time.sleep(0.1)
                        while gtk.events_pending():
                            gtk.main_iteration()
                else:
                    self.statusbar_update(x, yStart)
                    time.sleep(0.1)
                    while gtk.events_pending():
                        gtk.main_iteration()

    def on_move_button_clicked(self, button, data=None):
        self.x_entry = self.builder.get_object("x_entry")
        self.x = (self.x_entry.get_text())
        xMove = (self.x)
        xMove = float(xMove)
        self.y_entry = self.builder.get_object("y_entry")
        self.y = (self.y_entry.get_text())
        yMove = (self.y)
        yMove = float(yMove)
        xMove = xMove*100
        yMove = yMove*100
        xMove = int(xMove)
        yMove = int(yMove)
        current_x = 0
        current_y = 0
        xStart = self.serial_read_x(current_x)
        yStart = self.serial_read_y(current_y)
        xGoTo = xStart + xMove
        yGoTo = yStart + yMove
        print(xGoTo)
        print(yGoTo)
        if xGoTo > 8000 or xGoTo < -8000 or yGoTo > 8000 or yGoTo < -8000:
            self.statusbar_error("Exceeding range")
        else:
            if xGoTo == xStart and yGoTo == yStart:
                self.statusbar_error("Already there!")
                while gtk.events_pending():
                    gtk.main_iteration()
            else:
                if xStart > xGoTo:
                    for x in range(xStart, xGoTo-10, -10):
                        self.statusbar_update(x, yStart)
                        self.serial_push_x(x)
                        time.sleep(0.1)
                        while gtk.events_pending():
                            gtk.main_iteration()
                elif xStart < xGoTo:
                    for x in range(xStart, xGoTo+10, 10):
                        self.statusbar_update(x, yStart)
                        self.serial_push_x(x)
                        time.sleep(0.1)
                        while gtk.events_pending():
                            gtk.main_iteration()
                else:
                    self.statusbar_update(xStart, yStart)
                    time.sleep(0.1)
                    while gtk.events_pending():
                        gtk.main_iteration()
                    x = xStart

                if yStart > yGoTo:
                    for y in range(yStart, yGoTo-10, -10):
                        self.statusbar_update(x, y)
                        self.serial_push_y(y)
                        time.sleep(0.1)
                        while gtk.events_pending():
                            gtk.main_iteration()
                elif yStart < yGoTo:
                    for y in range(yStart, yGoTo+10, 10):
                        self.statusbar_update(x, y)
                        self.serial_push_y(y)
                        time.sleep(0.1)
                        while gtk.events_pending():
                            gtk.main_iteration()
                else:
                    self.statusbar_update(x, yStart)
                    time.sleep(0.1)
                    while gtk.events_pending():
                        gtk.main_iteration()

    def on_scan_button_clicked(self, button, data=None):
        self.scan_entry = self.builder.get_object("scan_entry")
        self.scan = (self.scan_entry.get_text())
        string = self.scan
        string = string.split(",")

        xStart = float(string[0])
        xStart = xStart*100
        xStart = int(xStart)

        xGoTo = float(string[1])
        xGoTo = xGoTo*100
        xGoTo = int(xGoTo)

        yStart = float(string[2])
        yStart = yStart*100
        yStart = int(yStart)

        yGoTo = float(string[3])
        yGoTo = yGoTo*100
        yGoTo = int(yGoTo)

        delay = int(string[4])

        steps = int(string[5])

        current_x = 0
        current_y = 0

        xStart = self.serial_read_x(current_x)
        yStart = self.serial_read_y(current_y)

        if xGoTo > 8000 or xGoTo < -8000 or yGoTo > 8000 or yGoTo < -8000 or xStart > 8000 or xStart < -8000 or yStart > 8000 or yStart < -8000:
            self.statusbar_error("Exceeding range")
        else:
            if xGoTo == xStart and yGoTo == yStart:
                self.statusbar_error("Already there!")
                while gtk.events_pending():
                    gtk.main_iteration()
            else:
                if current_x > xStart:
                    for x in range(current_x, xStart-10, -10):
                        self.statusbar_update(x, current_y)
                        self.serial_push_x(x)
                        time.sleep(0.1)
                        while gtk.events_pending():
                            gtk.main_iteration()
                elif current_x < xStart:
                    for x in range(current_x, xStart+10, 10):
                        self.statusbar_update(x, current_y)
                        self.serial_push_x(x)
                        time.sleep(0.1)
                        while gtk.events_pending():
                            gtk.main_iteration()
                else:
                    self.statusbar_update(current_x, current_y)
                    time.sleep(0.1)
                    while gtk.events_pending():
                        gtk.main_iteration()
                    x = current_x

                if current_y > yStart:
                    for y in range(current_y, yStart-10, -10):
                        self.statusbar_update(x, y)
                        self.serial_push_y(y)
                        time.sleep(0.1)
                        while gtk.events_pending():
                            gtk.main_iteration()
                elif current_x < yStart:
                    for y in range(current_y, yStart+10, 10):
                        self.statusbar_update(x, y)
                        self.serial_push_y(y)
                        time.sleep(0.1)
                        while gtk.events_pending():
                            gtk.main_iteration()
                else:
                    self.statusbar_update(x, current_y)
                    time.sleep(0.1)
                    while gtk.events_pending():
                        gtk.main_iteration()


                """if xStart > xGoTo:
                    for x in range(xStart, xGoTo-10, -10):
                        self.statusbar_update(x, yStart)
                        self.serial_push_x(x)
                        time.sleep(0.1)
                        while gtk.events_pending():
                            gtk.main_iteration()
                elif xStart < xGoTo:
                    for x in range(xStart, xGoTo+10, 10):
                        self.statusbar_update(x, yStart)
                        self.serial_push_x(x)
                        time.sleep(0.1)
                        while gtk.events_pending():
                            gtk.main_iteration()
                else:
                    self.statusbar_update(xStart, yStart)
                    time.sleep(0.1)
                    while gtk.events_pending():
                        gtk.main_iteration()
                    x = xStart

                if yStart > yGoTo:
                    for y in range(yStart, yGoTo-10, -10):
                        self.statusbar_update(x, y)
                        self.serial_push_y(y)
                        time.sleep(0.1)
                        while gtk.events_pending():
                            gtk.main_iteration()
                elif yStart < yGoTo:
                    for y in range(yStart, yGoTo+10, 10):
                        self.statusbar_update(x, y)
                        self.serial_push_y(y)
                        time.sleep(0.1)
                        while gtk.events_pending():
                            gtk.main_iteration()
                else:
                    self.statusbar_update(x, yStart)
                    time.sleep(0.1)
                    while gtk.events_pending():
                        gtk.main_iteration()



        self.x_entry = self.builder.get_object("x_move")
        self.y_entry = self.builder.get_object("y_move")
"""
    def on_stop_button_clicked(self, button, data=None):
        self.x_entry = self.builder.get_object("x_move")
        self.y_entry = self.builder.get_object("y_move")

    def __init__(self):
        cssProvider = gtk.CssProvider()
        cssProvider.load_from_path('pv.css')
        screen = gdk.Screen.get_default()
        styleContext = gtk.StyleContext()
        styleContext.add_provider_for_screen(screen, cssProvider, gtk.STYLE_PROVIDER_PRIORITY_USER)
        self.gladefile = "pv2.glade"
        self.builder = gtk.Builder()
        self.builder.add_from_file(self.gladefile)
        self.builder.connect_signals(self)
        self.window = self.builder.get_object("window1")
        self.aboutdialog = self.builder.get_object("aboutdialog1")
        self.warning = self.builder.get_object("messagedialog1")
        self.statusbar = self.builder.get_object("statusbar1")
        self.context_id = self.statusbar.get_context_id("status")
        self.status_count = 0
        self.window.show()
        #ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
        #serial.Serial('/dev/ttyUSB0', 115200, timeout=1)


if __name__ == "__main__":
    main = PV()
    gtk.main()



