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

from Model_Region import *
import unittest
import copy

class TestOsmMap(unittest.TestCase):

    def setUp(self):
        self.region = Region(-10, 10, -10, 10)
    
    def test_init(self):
        self.assertEqual(self.region.west, -10)
        self.assertEqual(self.region.east, 10)
        self.assertEqual(self.region.north, 10)
        self.assertEqual(self.region.south, -10)
         
    def test_shift(self):
        region = copy.copy(self.region)
        region.shift(10, 10)
        
        self.assertEqual(region.west, 0)
        self.assertEqual(region.east, 20)
        self.assertEqual(region.north, 20)
        self.assertEqual(region.south, 0)
    
    def test_relativeShift(self):
        region = copy.copy(self.region)
        region.relativeShift(0.5, 0.5)
        
        self.assertEqual(region.west, 0)
        self.assertEqual(region.east, 20)
        self.assertEqual(region.north, 20)
        self.assertEqual(region.south, 0)
    
    def test_getCenter(self):
        lat, lon = self.region.getCenter()
        
        self.assertEqual(lat, 0)
        self.assertEqual(lon, 0)
    
    def test_isInclude(self):
        self.assertTrue(self.region.isInclude(0, 0))
        self.assertTrue(self.region.isInclude(5, 0))
        self.assertTrue(self.region.isInclude(0, 5))
        self.assertTrue(self.region.isInclude(-5, 0))
        self.assertTrue(self.region.isInclude(0, -5))
        self.assertTrue(self.region.isInclude(5, 5))
        self.assertTrue(self.region.isInclude(5, 5))
        self.assertTrue(self.region.isInclude(-5, 5))
        self.assertTrue(self.region.isInclude(5, -5))
        
        self.assertFalse(self.region.isInclude(15, 0))
        self.assertFalse(self.region.isInclude(0, 15))
        self.assertFalse(self.region.isInclude(-15, 0))
        self.assertFalse(self.region.isInclude(0, -15))
        self.assertFalse(self.region.isInclude(15, 15))
        self.assertFalse(self.region.isInclude(15, -15))
        self.assertFalse(self.region.isInclude(-15, 15))
        self.assertFalse(self.region.isInclude(-15, -15))
        
    
    def test_getRelativePosition(self):
        x, y = self.region.getRelativePosition(5, 5)
        self.assertEqual(x, 0.75)
        self.assertEqual(y, 0.75)
        
    def test_getWidth(self):
        self.assertEqual(self.region.getWidth(), 20)
        
    def test_getHeight(self):
        self.assertEqual(self.region.getHeight(), 20)
        
if __name__ == '__main__':
    unittest.main()
