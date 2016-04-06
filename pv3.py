#!/usr/bin/python3

from gi.repository import Gtk as gtk, Gdk as gdk
import time
import serial

class PV:

    def close_connection(self):
        serial.Serial.close()

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
        for x in range(0, xGoTo, 10):
            print("par angleOffsetPitch %d" % x)
            time.sleep(0.5) 
 #  print("par angleOffsetRoll %d" % yGoTo)
        self.response =  self.warning.run()
        self.warning.hide()
    def on_move_button_clicked(self, button, data=None):
        self.x_entry = self.builder.get_object("x_move")
        self.y_entry = self.builder.get_object("y_move")

    def on_script_button_clicked(self, button, data=None):
        self.x_entry = self.builder.get_object("x_move")
        self.y_entry = self.builder.get_object("y_move")

    def on_run_button_clicked(self, button, data=None):
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
        self.window.show()
#        serial.Serial('/dev/ttyUSB0', 115200, timeout=1)


if __name__ == "__main__":
    main = PV()
    gtk.main()


