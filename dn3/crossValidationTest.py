'''
Created on Mar 5, 2012

@author: smotko
'''
import unittest


class Test(unittest.TestCase):


    def testIntersect(self):
        from crossValidation import intersect
        self.assertEqual(intersect([1,2,3], [1,2,3]), 3, "Same")
        self.assertEqual(intersect([0,6,4], [2,7]), 0, "None")
        self.assertEqual(intersect([0,6,4], []), 0, "None")
        
    def testFscore(self):
        from crossValidation import f_score
        self.assertEqual(f_score([1,2,3], [2,3]), 4/5.0, 'Basic')
        self.assertEqual(f_score([1,2,3], [1,2,3]), 1.0, '1')
        self.assertEqual(f_score([1,2,3], []), 0, '0')
        self.assertEqual(f_score([13, 40, 44, 59, 62], [50]), 'Should not fail')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testIntersect']
    unittest.main()