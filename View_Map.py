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

import gtk
import math
from itertools import islice

class MapView(gtk.DrawingArea):
    def __init__(self):
        super(MapView, self).__init__()
        self.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color("#561f66"))
        self.modify_fg(gtk.STATE_NORMAL, gtk.gdk.Color("#FFFFFF"))
        self.set_events(gtk.gdk.EXPOSURE_MASK
            | gtk.gdk.LEAVE_NOTIFY_MASK
            | gtk.gdk.BUTTON_PRESS_MASK
            | gtk.gdk.BUTTON_RELEASE_MASK
            | gtk.gdk.POINTER_MOTION_MASK
            | gtk.gdk.POINTER_MOTION_HINT_MASK
            | gtk.gdk.SCROLL)
        self.connect("expose-event", self.expose)
        self.data = list()
        
    def exposeOld(self, widget, event):
        print "expose"
        cr = widget.window.cairo_create()
        cr.set_source_color(gtk.gdk.Color("#FFFFFF"))
        cr.set_line_width(4)

        w = self.allocation.width
        h = self.allocation.height
       
        cr.translate(w/2, h/2)
        cr.arc(0, 0, 120, 0, 2*math.pi)
        cr.stroke()
         
        for i in range(36):
            cr.save()
            cr.rotate(i*math.pi/36)
            cr.scale(0.3, 1)
            cr.arc(0, 0, 120, 0, 2*math.pi)
            cr.restore()
            cr.stroke()

    def expose(self, widget, event):
        print "new expose"
        cr = widget.window.cairo_create()
        cr.set_source_color(gtk.gdk.Color("#FFFFFF"))
        cr.set_line_width(3)

        w = self.allocation.width
        h = self.allocation.height
        
        cr.move_to(0, 0)
        cr.move_to(w, 0)
        cr.move_to(w, h)
        cr.move_to(0, h)
        cr.move_to(0, 0)
        cr.stroke()
        
        for curveType, path in self.data:
            if curveType == "polyline":
                x, y = path[0]
                cr.move_to((w - h) / 2.0 + x * h, h - y * h)
                for x, y in islice(path, 1, None):
                    cr.line_to((w - h) / 2.0 + x * h, h - y * h)
                cr.stroke()
            if curveType == "bezier":
                try:
                    x, y = path[0]
                except:
                    print curveType, path
                cr.move_to((w - h) / 2.0 + x * h, h - y * h)
                x1, y1 = path[1]
                x2, y2 = path[2]
                x3, y3 = path[3]
                
                cr.curve_to((w - h) / 2.0 + x1 * h, h - y1 * h,
                          (w - h) / 2.0 + x2 * h, h - y2 * h,
                          (w - h) / 2.0 + x3 * h, h - y3 * h)
                cr.stroke()
