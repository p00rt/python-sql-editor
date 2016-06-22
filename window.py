from gi.repository import Gtk
import MySQLdb as mysql

class Login(Gtk.Window):


    def __init__(self):

        Gtk.Window.__init__(self, title="sqlconnector")

        #Boxes
        firstbox = Gtk.VBox(spacing=5)
        self.add(firstbox)

        loginbox = Gtk.HBox(spacing = 10)

        hostdbbox = Gtk.HBox(spacing = 10)

        buttonbox = Gtk.HBox(spacing = 10)


        # Labels
        loginlabel = Gtk.Label("login: ")
        passlabel = Gtk.Label("password: ")
        hostlabel = Gtk.Label("host: ")
        dblabel = Gtk.Label("database: ")


        # Input 
        self.loginentry = Gtk.Entry()
        self.loginentry.set_text("login")

        self.passentry = Gtk.Entry()
        self.passentry.set_text("password")
        self.passentry.set_visibility(False)

        self.hostentry = Gtk.Entry()
        self.hostentry.set_text("localhost")

        self.dbentry = Gtk.Entry()
        self.dbentry.set_text("database")


        # Buttons
        connectButton = Gtk.Button.new_with_label(label="Click me!")
        connectButton.connect("clicked", self.request_connection)


        # pack
        loginbox.add(loginlabel)
        loginbox.add(self.loginentry)
        loginbox.add(passlabel)
        loginbox.add(self.passentry)

        hostdbbox.add(hostlabel)
        hostdbbox.add(self.hostentry)
        hostdbbox.add(dblabel)
        hostdbbox.add(self.dbentry)

        buttonbox.add(connectButton)

        firstbox.add(loginbox)
        firstbox.add(hostdbbox)
        firstbox.add(buttonbox)


#    def dbview():
#        self.remove(firstbox)
#        editbox = Gtk.


    def request_connection(self, butt):
        print "Button clicked"
        self.db = mysql.connect(self.hostentry.get_text(),
                    self.loginentry.get_text(), self.passentry.get_text(),
                    self.dbentry.get_text())
        self.cursor = self.db.cursor()
        self.cursor.execute("SELECT VERSION()")
        data = self.cursor.fetchall()
        print data
        self.db.close()


win = Login()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
