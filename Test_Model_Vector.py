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


import Model_Vector as vector
import unittest

class TestOsmMap(unittest.TestCase):

    #def setUp(self):
    #   pass
    
    def test_length(self):
        self.assertEqual(vector.length((0, 1)), 1)
        self.assertEqual(vector.length((3, 4)), 5)
        self.assertEqual(vector.length((0, 0)), 0)
    
    def test_streighten(self):
        self.assertEqual(
            vector.streighten((1, 0), (-1, 0)),
            ((1, 0), (-1, 0)))
        
        self.assertEqual(
            vector.streighten((1, 1), (-1, 1)),
            ((1, 0), (-1, 0)))
        
        self.assertEqual(
            vector.streighten((1, 0.5), (-1, 0.5)),
            ((1, 0), (-1, 0)))
        
if __name__ == '__main__':
    unittest.main()
