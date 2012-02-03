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

from Model_Approximation import *
import unittest
import copy

class TestBezierApproximation(unittest.TestCase):

    def setUp(self):
        pass
        
    def test_bezierApproximation(self):
        #path = [(0, 1), ()]
        pass
        
    def test_getPrimitive(self):
        test0 = getPrimitive(t = 0.0, b1 = 1.0, b0 = 1.0, a3 = 1.0, a2 = 1.0, a1 = 1.0, a0 = 1.0)
        self.assertEqual(0.0, test0)
        test1 = getPrimitive(t = 1.0, b1 = 0.0, b0 = 1.0, a3 = 1.0, a2 = 0.0, a1 = 0.0, a0 = 0.0)
        self.assertEqual(1.0/4.0, test1)
        test2 = getPrimitive(t = 1.0, b1 = 0.0, b0 = 1.0, a3 = 0.0, a2 = 1.0, a1 = 0.0, a0 = 0.0)
        self.assertEqual(1.0/3.0, test2)
        test2 = getPrimitive(t = 1.0, b1 = 1.0, b0 = 0.0, a3 = 0.0, a2 = 0.0, a1 = 1.0, a0 = 0.0)
        self.assertEqual(1.0/3.0, test2)

    def test_getLength(self):
        path = list([(0, 0), (0, 1), (1, 1), (1, 0), (0, 0)])
        self.assertEqual(4.0, getLength(path))
    
    def test_getApproximateBezier(self):
        path = list([(0.0, 0.0), (1.0, 0.0)])
        coeff =  getApproximateBezier(path)
        x, y =  coeff[0]
        self.assertAlmostEqual(0.0, x, 7)
        self.assertAlmostEqual(0.0, y, 7)
        x, y =  coeff[3]
        self.assertAlmostEqual(1.0, x, 7)
        self.assertAlmostEqual(0.0, y, 7)
        
        path = list([(0, 0), (1, 1), (2, 2), (3, 2), (4, 1)])
        print getApproximateBezier(path)
        
    def test_getIntegral(self):
        result = getIntegral(0, 1, 1, 1, 0, 0, 0, 1)
        self.assertEqual(1.0, result)
        result = getIntegral(0.0, 1.0, 0.0, 0.0, 1.0, -3.0, 3.0, -1.0)
        self.assertEqual(0.0, result)
        result = getIntegral(0.0, 1.0, 0.0, 1.00, -1.0, 3.0, -3.0, 1.0)
        self.assertAlmostEqual(1.0/20.0, result, 7)
    
    def test_getBezier(self):
        bezier = [(0, 0), (1, 1),  (1, 1),  (1, 1)]
        x, y = getBezier(bezier, 0.0)
        self.assertAlmostEqual(0.0, x, 7)
        self.assertAlmostEqual(0.0, y, 7)
        x, y = getBezier(bezier, 1.0)
        self.assertAlmostEqual(1.0, x, 7)
        self.assertAlmostEqual(1.0, y, 7)
    
    def test_getMaxDeviation(self):
        path = [(0.0, 0.0), (0.25, 0.25),  (0.5, 0.5),  (0.75, 0.75), (1.0, 1.0)]
        bezier = getApproximateBezier(path)
        print bezier
        deviation = getMaxDeviation(bezier, path)
        self.assertAlmostEqual(0.0, deviation, 7)
        
if __name__ == '__main__':
    unittest.main()
