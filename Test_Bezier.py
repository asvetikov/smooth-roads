from Model_Approximation import *
import gtk
import cairo
import math
from itertools import islice

path = list()

def button_press_event(widget, event):
    print "press"
    if event.button == 1:
        print "button1"
        path.append((event.x, event.y))
    if event.button == 2:
        print "button2"
        path.pop()
    print path
    widget.queue_draw()
    return True

def expose_event(widget, event):
    print "expose"
    cr = widget.window.cairo_create()
    cr.set_source_color(gtk.gdk.Color("#000000"))
    cr.set_line_width(3)

    #w = widgetallocation.width; h = self.allocation.height
    
    if(len(path) < 2):
        return True
    
    # polyline
    x, y = path[0]
    cr.move_to(x, y)
    for x, y in islice(path, 1, None):
        cr.line_to(x, y)
    cr.stroke()
    
    curves = bezierApproximation(path, 10)
    print curves
    for curveType, curve  in curves:
        if curveType == "polyline":
            cr.set_source_color(gtk.gdk.Color("#000000"))
            x, y = curve[0]
            cr.move_to(x, y)
            for x, y in islice(curve, 1, None):
                cr.line_to(x, y)
            cr.stroke()
        if curveType == "bezier":
            cr.set_source_color(gtk.gdk.Color("#00AA00"))
            cr.move_to(curve[0][0], curve[0][1] )
            cr.curve_to(curve[1][0], curve[1][1], curve[2][0], curve[2][1], curve[3][0], curve[3][1])
            cr.stroke()
            
def main():
    window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    window.set_name ("Test Bezier")

    window.connect("destroy", lambda w: gtk.main_quit())

    # Create the drawing area
    drawing_area = gtk.DrawingArea()
    drawing_area.set_size_request(600, 400)

    # Signals used to handle backing pixmap
    drawing_area.connect("expose_event", expose_event)
    drawing_area.connect("button_press_event", button_press_event)

    drawing_area.set_events(gtk.gdk.EXPOSURE_MASK
                            | gtk.gdk.LEAVE_NOTIFY_MASK
                            | gtk.gdk.BUTTON_PRESS_MASK
                            | gtk.gdk.POINTER_MOTION_MASK
                            | gtk.gdk.POINTER_MOTION_HINT_MASK)
    window.add(drawing_area)
    window.show_all()

    gtk.main()

    return 0

if __name__ == "__main__":
    main()
