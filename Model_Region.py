from math import atan, sqrt, cos, sin, pi

f = 1.0/298.257839303
eps = sqrt(2.0 * f * (1.0 - f))

class Region:
    def __init__(self, west = 0, east = 0, south = 0, north = 0):
        self.west = west
        self.east = east
        self.north = north
        self.south = south
    
    def shift(self, lat, lon):
        self.west = self.west + lon
        self.east = self.east + lon
        self.north = self.north + lat
        self.south = self.south + lat
    
    def zoom(self, zoom):
        lat, lon = self.getCenter()
        width = self.getWidth() * zoom
        height = self.getHeight() * zoom
        self.west = lon - width / 2.0
        self.east = lon + width / 2.0
        self.north = lat + height / 2.0
        self.south = lat - height / 2.0
    
    def relativeShift(self, x, y):
        self.shift(self.getWidth() * x, self.getHeight() * y)
        
    def getCenter(self):
        lon = (self.west + self.east) / 2.0
        lat = (self.north + self.south) / 2.0
        return lat, lon
    
    def isInclude(self, lat, lon):
        if not self.west < lon < self.east:
            return False
        
        if not self.south < lat < self.north:
            return False

        return True
    
    def getRelativePosition(self, lat, lon):
        x = float(lon - self.west) / self.getWidth()
        y = float(lat - self.south) / self.getHeight()
        return (x, y)
    
    def getRelativeProjectedPosition(self, lat, lon):
        x = float(lon - self.west) / self.getWidth()
        hmax = self.getHeight() / 90.0
        hmin = - hmax
        h = 2 * float(lat - (self.south + self.north) / 2.0) / 90.0
        y = (h - hmin) / (hmax - hmin) 
        return (x, y)

    def calcY(self, lat):
        theta = float(lat - (self.south + self.north) / 2.0) * pi / 180.0
        return atan(sin(theta) - eps * atan(eps * sin(theta))) / pi
    
    def getRelativeMercatorPosition(self, lat, lon):
        #print self.getWidth(), self.getHeight()
        x = float(lon - self.west) / self.getWidth()
        ymin = self.calcY(self.south)
        ymax = self.calcY(self.north)
        y0 = (ymin + ymax) / 2.0 
        y = self.calcY(lat) - y0 + 0.5
        #y = (y - ymin) / (ymax - ymin)
        return (x, y)
        
    def getWidth(self):
        return self.east - self.west
    
    def getHeight(self):
        return self.north - self.south
    
    def pack(self):
        return (self.west, self.east, self.south, self.north)
