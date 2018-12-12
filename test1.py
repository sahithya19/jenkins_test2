import unittest
from add import sub, div
  
class SimpleTest(unittest.TestCase): 
  
    # Returns True or False.  
    def test_div(self):
        a = div(5,2)
        self.assertEqual(2.5,a)

    def test_sub(self):
        a = sub(5,2)
        self.assertEqual(3,a)
  
if __name__ == '__main__': 
    unittest.main() 
