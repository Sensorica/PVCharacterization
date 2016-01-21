from gi.repository import Gtk as gtk, Gdk as gdk

class PV:

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
        self.x_entry = self.builder.get_object("x_goto")
        self.y_entry = self.builder.get_object("y_goto")

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
        self.window.show()

if __name__ == "__main__":
    main = PV()
    gtk.main()
