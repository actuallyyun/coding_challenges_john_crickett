import unittest
import ccwc
import sys
from unittest.mock import patch
import os
import subprocess


class Test_word_count(unittest.TestCase):

    def test3(self):
        
        wc_arg=['wc','-c','test.txt']
        ccwc_arg=['python','ccwc.py','-c','test.txt']

        wc_result=subprocess.run(wc_arg,stdout=subprocess.PIPE)
        wc_output=wc_result.stdout.decode('utf-8')

        ccwc_result=subprocess.run(ccwc_arg,stdout=subprocess.PIPE)
        ccwc_output=ccwc_result.stdout.decode('utf-8')

        
        self.assertEqual(wc_output,ccwc_output) 
    
if __name__=='__main__':
    unittest.main()
    