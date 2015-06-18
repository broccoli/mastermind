'''
Created on Jun 8, 2015

@author: richard
'''
import unittest

from utils import evaluate_guess, Code, Guess


class TestEvaluateGuess(unittest.TestCase):


    def test1(self):
        code = "RRRR"
        guess = "YYYY"
        expected_result = (0, 0)
        result = evaluate_guess(code, guess)
        self.assertEqual(expected_result, result)

    def test2(self):        
        code = "RRRR"
        guess = "RYYY"
        expected_result = (1, 0)
        result = evaluate_guess(code, guess)
        self.assertEqual(expected_result, result)

    def test3(self):        
        code = "RRRR"
        guess = "RYRY"
        expected_result = (2, 0)
        result = evaluate_guess(code, guess)
        self.assertEqual(expected_result, result)

    def test4(self):        
        code = "RRRR"
        guess = "RRRR"
        expected_result = (4, 0)
        result = evaluate_guess(code, guess)
        self.assertEqual(expected_result, result)

    def test5(self):        
        code = "ABCD"
        guess = "BFFF"
        expected_result = (0, 1)
        result = evaluate_guess(code, guess)
        self.assertEqual(expected_result, result)

    def test6(self):        
        code = "ABCD"
        guess = "BFFC"
        expected_result = (0, 2)
        result = evaluate_guess(code, guess)
        self.assertEqual(expected_result, result)

    def test7(self):        
        code = "ABCD"
        guess = "DCBA"
        expected_result = (0, 4)
        result = evaluate_guess(code, guess)
        self.assertEqual(expected_result, result)

    def test8(self):        
        code = "ABCD"
        guess = "CBFF"
        expected_result = (1, 1)
        result = evaluate_guess(code, guess)
        self.assertEqual(expected_result, result)

    def test9(self):        
        code = "ABCD"
        guess = "ABDC"
        expected_result = (2, 2)
        result = evaluate_guess(code, guess)
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