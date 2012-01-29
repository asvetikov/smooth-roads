from Model_Map import *
from View_MainWindow import *
from View_Map import *
from Controller_Map import *

class Application:
    def __init__(self):
        # Models initialization
        #self.mapModel = OsmMap("small_test.osm")
        #self.mapModel = OsmMap("cairo.osm")
        self.mapModel = OsmMap("tromso.osm")
        
        # Views initialization
        self.mainWindowView = MainWindowView()
        self.mapView = MapView()
        self.mainWindowView.add(self.mapView)
        self.mainWindowView.show_all()
    
        # Controllers initialization
        self.mapController = MapController(self.mapView, self.mapModel)
    
    def execute(self):
        gtk.main()

