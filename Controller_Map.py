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
from View_Map import *
import gtk
import cairo

class MapController:
    def __init__(self, mapView, mapModel):
        self.mapView = mapView
        self.mapModel = mapModel
        #self.mapView.connect("motion_notify_event", self.motion_notify_event)
        self.mapView.connect("button_press_event", self.button_press_event)
        self.mapView.connect("button_release_event", self.button_release_event)
        self.mapView.connect("scroll_event", self.scroll_event)
        x, y, width, height, depth = self.mapView.window.get_geometry()
        self.region = self.mapModel.getOptRegion(width, height)
        print self.region.getWidth(), self.region.getHeight()
        self.mapView.data = self.mapModel.getRegionData(self.region)
        print "count ", len(self.mapView.data)
    
    def scroll_event(self, widget, event):
        if event.direction == gtk.gdk.SCROLL_UP:
            self.region.zoom(0.6180339887498949)
        if event.direction == gtk.gdk.SCROLL_DOWN:
            self.region.zoom(1.6180339887498949)
        
        self.mapView.data = self.mapModel.getRegionData(self.region)
        self.mapView.queue_draw()
        return True
        
    def button_press_event(self, widget, event):
        if event.button == 1:
            self.x = event.x
            self.y = event.y
            
        return True

    def button_release_event(self, widget, event):
        print "release "
        if event.button == 1:
            x, y, width, height, depth = widget.window.get_geometry()
            #print (event.x - self.x) / width, (event.y - self.y) / height
            self.region.relativeShift((event.y - self.y) / height, -(event.x - self.x) / width)
            self.mapView.data = self.mapModel.getRegionData(self.region)
            self.mapView.queue_draw()
        return True

    def motion_notify_event(self, widget, event):
        print "motion "
        if event.is_hint:
            x, y, state = event.window.get_pointer()
        else:
            x = event.x
            y = event.y
            state = event.state
        self.mapView.draw_point(x, y)
        if state & gtk.gdk.BUTTON1_MASK:
            pass
            #draw_brush(widget, x, y)
        
        return True

