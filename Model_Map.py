import xml.sax
import xml.sax.handler

from Model_Region import *

class OsmMap(xml.sax.handler.ContentHandler):
    def __init__(self, fileName):
        self.nodes = dict()
        self.ways = dict()
        xml.sax.parse(fileName, self)
        return

    def startElement(self, name, attrs):
        if(name == "node"):
            self.node = dict({"id": int(attrs["id"]), "lat": float(attrs["lat"]), "lon": float(attrs["lon"]) });
        if(name == "way"):
            self.way = dict({"id": int(attrs["id"]), "nodes": list()});
        if(name == "nd"):
            self.way["nodes"].append(int(attrs["ref"]))
    
    def endElement(self, name):
        if(name == "node"):
            nodeId = self.node["id"]
            self.nodes[nodeId] = self.node
        if(name == "way"):
            wayId = self.way["id"]
            self.ways[wayId] = self.way
        
    def getNodeCount(self):
        return len(self.nodes)
    
    def getWayCount(self):
        return len(self.ways)
    
    def getMapData(self):
        return dict({"nodes" : self.nodes, "ways": self.ways})
    
    def getMaxRegion(self):
        nodeId = iter(self.nodes).next()
        node = self.nodes[nodeId]
        lat = node["lat"]
        lon = node["lon"]
        region = Region(lon, lon, lat, lat)
        for nodeId in self.nodes:
            node = self.nodes[nodeId]
            lat = node["lat"]; lon = node["lon"]
            region.west = min(lon, region.west)
            region.east = max(lon, region.east)
            region.north = max(lat, region.north)
            region.south = min(lat, region.south)
        return region
    
    def getRegionData(self, region):
        paths = list()
        for wayId in self.ways:
            way = self.ways[wayId]
            if self.testWay(region, way):
                path = self.getPath(region, way)
                paths.append(path)
        return paths
        
    def testWay(self, region, way):
        for ref in way["nodes"]:
            node = self.nodes[ref]
            if region.isInclude(node["lat"], node["lon"]):
                return True
        return False
    
    def getPath(self, region, way):
        path = list()
        for ref in way["nodes"]:
            node = self.nodes[ref]
            position = region.getRelativePosition(node["lat"], node["lon"]) 
            path.append(position)
        return path
