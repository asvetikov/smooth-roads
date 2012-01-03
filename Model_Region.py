
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
        
    def getWidth(self):
        return self.east - self.west
    
    def getHeight(self):
        return self.north - self.south
