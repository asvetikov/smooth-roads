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
