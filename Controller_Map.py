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
        self.region = self.mapModel.getMaxRegion()
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

