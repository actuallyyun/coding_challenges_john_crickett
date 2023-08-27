import unittest
import ccwc
import sys
from unittest.mock import patch


class Test_word_count(unittest.TestCase):
    
    def test1(self):
        arg1=['-c','test.txt']
        with patch.object(sys,'argv',arg1):
            self.assertEqual('-c',sys.argv[0]) 
        
        


    
if __name__=='__main__':
    unittest.main()
    