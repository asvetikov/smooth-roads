import gtk

class MainWindowView(gtk.Window):
    def __init__(self):
        super(MainWindowView, self).__init__()
        
        self.set_title("Smooth Roads")
        self.set_size_request(400, 300)
        self.set_opacity(0.8)
        self.set_position(gtk.WIN_POS_CENTER)

        self.connect("destroy", gtk.main_quit)
    

