
import random
import unittest
import app

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)

    def test_rewrite(self):
        seed = ['A']
        expected = ['A','B']
        rules = {'A':'AB', 'B':'A'}
        result = app.proc(seed,[],rules)
        self.assertEqual("".join(expected),"".join(result))

    def test_rewrite2(self):
        seed = list('AB')
        expected = list('ABA')
        rules = {'A':'AB', 'B':'A'}
        result = app.proc(seed,[],rules)
        self.assertEqual("".join(expected),"".join(result))

    def test_koch_curve(self):
        axiom = list('F')
        rules = {'F':'F-F+F+F-F'}
        steps = 1
        expected = "F-F+F+F-F"
        result = app.lsystem(steps,axiom,rules)
        self.assertEqual(expected,result)
    
    def test_koch_curve2(self):
        axiom = list('F')
        rules = {'F':'F-F+F+F-F'}
        steps = 3
        expected = "F-F+F+F-F - F-F+F+F-F + F-F+F+F-F + F-F+F+F-F - F-F+F+F-F - F-F+F+F-F - F-F+F+F-F + F-F+F+F-F + F-F+F+F-F - F-F+F+F-F + F-F+F+F-F - F-F+F+F-F + F-F+F+F-F + F-F+F+F-F - F-F+F+F-F + F-F+F+F-F - F-F+F+F-F + F-F+F+F-F + F-F+F+F-F - F-F+F+F-F - F-F+F+F-F - F-F+F+F-F + F-F+F+F-F + F-F+F+F-F - F-F+F+F-F"
        result = app.lsystem(steps,axiom,rules)
        self.assertEqual(expected,result)
        

    def test_lsystem1(self):
        expected = "ABA"
        initiator = list('A')
        rules = {'A':'AB', 'B':'A'}
        steps = 2
        result = app.lsystem(steps,initiator,rules)
        self.assertEqual(expected, result)

    def test_lsystem2(self):
        expected = "ABAABABAABAABABAABABAABAABABAABAAB"
        initiator = list('A')
        rules = {'A':'AB', 'B':'A'}
        steps = 7
        result = app.lsystem(steps,initiator,rules)
        self.assertEqual(expected, result)

    def test_lsystem3(self):
        expected = "ABAAB"
        initiator = list('A')
        rules = {'A':'AB', 'B':'A'}
        steps = 3
        result = app.lsystem(steps,initiator,rules)
        self.assertEqual(expected, result)
    
    def test_lsystem4(self):
        expected = "ABAABABA"
        initiator = list('A')
        rules = {'A':'AB', 'B':'A'}
        steps = 4
        result = app.lsystem(steps,initiator,rules)
        self.assertEqual(expected, result)

    def test_lsystem5(self):
        expected = "ABAABABAABAAB"
        initiator = list('A')
        rules = {'A':'AB', 'B':'A'}
        steps = 5
        result = app.lsystem(steps,initiator,rules)
        self.assertEqual(expected, result)

    def test_lsystem6(self):
        expected = "ABAABABAABAABABAABABA"
        initiator = list('A')
        rules = {'A':'AB', 'B':'A'}
        steps = 6
        result = app.lsystem(steps,initiator,rules)
        self.assertEqual(expected, result)

    def test_lsystem7(self):
        expected = "A"
        initiator = list('A')
        rules = {'A':'AB', 'B':'A'}
        steps = 0
        result = app.lsystem(steps,initiator,rules)
        self.assertEqual(expected, result)

    def test_lsystem8(self):
        expected = "AB"
        initiator = list('A')
        rules = {'A':'AB', 'B':'A'}
        steps = 1
        result = app.lsystem(steps,initiator,rules)
        self.assertEqual(expected, result)
    


        

if __name__ == '__main__':
    unittest.main()
