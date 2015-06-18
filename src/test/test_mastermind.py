'''
Created on Jun 8, 2015

@author: richard
'''
import unittest

from mastermind import Code, Guess


class TestEvaluateGuess(unittest.TestCase):


    def test1(self):
        code = "RRRR"
        guess = "YYYY"
        g = Guess(guess, code)
        expected_result = (0, 0)
        result = (g.black, g.white)
        self.assertEqual(expected_result, result)

    def test2(self):        
        code = "RRRR"
        guess = "RYYY"
        g = Guess(guess, code)
        expected_result = (1, 0)
        result = (g.black, g.white)
        self.assertEqual(expected_result, result)
 
    def test3(self):        
        code = "RRRR"
        guess = "RYRY"
        g = Guess(guess, code)
        expected_result = (2, 0)
        result = (g.black, g.white)
        self.assertEqual(expected_result, result)
 
    def test4(self):        
        code = "RRRR"
        guess = "RRRR"
        g = Guess(guess, code)
        expected_result = (4, 0)
        result = (g.black, g.white)
        self.assertEqual(expected_result, result)
 
    def test5(self):        
        code = "ABCD"
        guess = "BFFF"
        g = Guess(guess, code)
        expected_result = (0, 1)
        result = (g.black, g.white)
        self.assertEqual(expected_result, result)
 
    def test6(self):        
        code = "ABCD"
        guess = "BFFC"
        g = Guess(guess, code)
        expected_result = (0, 2)
        result = (g.black, g.white)
        self.assertEqual(expected_result, result)
 
    def test7(self):        
        code = "ABCD"
        guess = "DCBA"
        g = Guess(guess, code)
        expected_result = (0, 4)
        result = (g.black, g.white)
        self.assertEqual(expected_result, result)
 
    def test8(self):        
        code = "ABCD"
        guess = "CBFF"
        g = Guess(guess, code)
        expected_result = (1, 1)
        result = (g.black, g.white)
        self.assertEqual(expected_result, result)
 
    def test9(self):        
        code = "ABCD"
        guess = "ABDC"
        g = Guess(guess, code)
        expected_result = (2, 2)
        result = (g.black, g.white)
        self.assertEqual(expected_result, result)


class TestCode(unittest.TestCase):


    def test1(self):
        c = Code()
        print 'code: ', c.code
        result = len(c.code)
        expected_result = 4
        self.assertEqual(expected_result, result)

class TestGuess(unittest.TestCase):


    def test1(self):
        c = Code(code = 'ABCD')
        g = Guess('ACAB', c.code)
        self.assertEqual(1, g.black)
        self.assertEqual(2, g.white)
#         result = len(c.code)
#         expected_result = 4
#         self.assertEqual(expected_result, result)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()