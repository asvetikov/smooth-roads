from Model_Map import *
import unittest

class TestOsmMap(unittest.TestCase):

    def setUp(self):
        self.modelMap = OsmMap("map.osm")
    
    def test_node_count(self):
        print "\nNode count = ", self.modelMap.getNodeCount()
        
    def test_way_count(self):
        print "\nWay count = ", self.modelMap.getWayCount()
        
    def test_max_region(self):
        region = self.modelMap.getMaxRegion()
        print "Max region = ", region.west, region.east, region.north, region.south
    
    def test_get_region_data(self):
        region = self.modelMap.getMaxRegion()
        #region.zoom(0.5)
        data = self.modelMap.getRegionData(region)
   
if __name__ == '__main__':
    unittest.main()
