#
# Copyright (c) 2012 pinocchio964
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the
# following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN
# NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE
# USE OR OTHER DEALINGS IN THE SOFTWARE.
#

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

