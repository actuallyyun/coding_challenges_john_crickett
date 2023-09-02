import unittest
import subprocess

class Test_word_count(unittest.TestCase):

    def test_bytes_count_success(self):
        
        wc_arg=['wc','-c','test.txt']
        ccwc_arg=['python','ccwc.py','-c','test.txt']

        wc_result=subprocess.run(wc_arg,stdout=subprocess.PIPE)
        wc_output=wc_result.stdout.decode('utf-8').strip()

        ccwc_result=subprocess.run(ccwc_arg,stdout=subprocess.PIPE)
        ccwc_output=ccwc_result.stdout.decode('utf-8').strip()

        self.assertEqual(wc_output,ccwc_output) 
    
    def test_words_count_success(self):

        wc_arg=['wc','-w','test.txt']
        ccwc_arg=['python','ccwc.py','-w','test.txt']

        wc_output=subprocess.run(wc_arg,stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
        ccwc_output=subprocess.run(ccwc_arg,stdout=subprocess.PIPE).stdout.decode('utf-8').strip()

        self.assertEqual(wc_output,ccwc_output) 

    def test_lines_count_success(self):

        wc_arg=['wc','-l','test.txt']
        ccwc_arg=['python','ccwc.py','-l','test.txt']

        wc_output=subprocess.run(wc_arg,stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
        ccwc_output=subprocess.run(ccwc_arg,stdout=subprocess.PIPE).stdout.decode('utf-8').strip()

        self.assertEqual(wc_output,ccwc_output) 

    def test_characters_count_success(self):

        wc_arg=['wc','-m','test.txt']
        ccwc_arg=['python','ccwc.py','-m','test.txt']

        wc_output=subprocess.run(wc_arg,stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
        ccwc_output=subprocess.run(ccwc_arg,stdout=subprocess.PIPE).stdout.decode('utf-8').strip()

        self.assertEqual(wc_output,ccwc_output) 

    def test_default_flag(self):
        wc_arg=['wc','test.txt']
        ccwc_arg=['python','ccwc.py','test.txt']

        wc_output=subprocess.run(wc_arg,stdout=subprocess.PIPE).stdout.decode('utf-8').strip().replace(" ","")
        ccwc_output=subprocess.run(ccwc_arg,stdout=subprocess.PIPE).stdout.decode('utf-8').strip().replace(" ","")

        self.assertEqual(wc_output,ccwc_output) 

if __name__=='__main__':
    unittest.main()
    