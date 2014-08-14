
import random
import unittest
import lsystem

class TestLSystem(unittest.TestCase):
    #TODO rewrite tests
    def setUp(self):
        self.pcgen = lsystem.Lsystem(lsystem.Lsystem.KOCH_CURVE)

    def test_rewrite(self):
        seed = ['A']
        expected = ['A','B']
        rules = {'A':'AB', 'B':'A'}
        self.pcgen.rules = rules
        result = self.pcgen.rewrite_system(seed)
        self.assertEqual("".join(expected),"".join(result))

    def test_rewrite2(self):
        seed = list('AB')
        expected = list('ABA')
        rules = {'A':'AB', 'B':'A'}
        self.pcgen.rules = rules
        result = self.pcgen.rewrite_system(seed,[])
        self.assertEqual("".join(expected),"".join(result))

    def test_koch_curve(self):
        axiom = list('F')
        rules = {'F':'F-F+F+F-F'}
        steps = 1
        expected = "F+F-F-F+F"
        result = self.pcgen.compute_system(steps,axiom)
        self.assertEqual(expected,result)
    
    def test_koch_curve2(self):
        axiom = list('F')
        rules = {'F':' F+F-F-F+F'}
        steps = 3
        expected = "F+F-F-F+F+F+F-F-F+F-F+F-F-F+F-F+F-F-F+F+F+F-F-F+F+F+F-F-F+F+F+F-F-F+F-F+F-F-F+F-F+F-F-F+F+F+F-F-F+F-F+F-F-F+F+F+F-F-F+F-F+F-F-F+F-F+F-F-F+F+F+F-F-F+F-F+F-F-F+F+F+F-F-F+F-F+F-F-F+F-F+F-F-F+F+F+F-F-F+F+F+F-F-F+F+F+F-F-F+F-F+F-F-F+F-F+F-F-F+F+F+F-F-F+F"
        result = self.pcgen.compute_system(steps,axiom)
        self.assertEqual(expected,result)
        

    def test_lsystem1(self):
        expected = "ABA"
        initiator = list('A')
        rules = {'A':'AB', 'B':'A'}
        self.pcgen.rules = rules
        steps = 2
        result = self.pcgen.compute_system(steps,initiator)
        self.assertEqual(expected, result)

    def test_lsystem2(self):
        expected = "ABAABABAABAABABAABABAABAABABAABAAB"
        initiator = list('A')
        rules = {'A':'AB', 'B':'A'}
        self.pcgen.rules = rules
        steps = 7
        result = self.pcgen.compute_system(steps,initiator)
        self.assertEqual(expected, result)

    def test_lsystem3(self):
        expected = "ABAAB"
        initiator = list('A')
        rules = {'A':'AB', 'B':'A'}
        self.pcgen.rules = rules
        steps = 3
        result = self.pcgen.compute_system(steps,initiator)
        self.assertEqual(expected, result)
    
    def test_lsystem4(self):
        expected = "ABAABABA"
        initiator = list('A')
        rules = {'A':'AB', 'B':'A'}
        self.pcgen.rules = rules
        steps = 4
        result = self.pcgen.compute_system(steps,initiator)
        self.assertEqual(expected, result)

    def test_lsystem5(self):
        expected = "ABAABABAABAAB"
        initiator = list('A')
        rules = {'A':'AB', 'B':'A'}
        self.pcgen.rules = rules
        steps = 5
        result = self.pcgen.compute_system(steps,initiator)
        self.assertEqual(expected, result)

    def test_lsystem6(self):
        expected = "ABAABABAABAABABAABABA"
        initiator = list('A')
        rules = {'A':'AB', 'B':'A'}
        self.pcgen.rules = rules
        steps = 6
        result = self.pcgen.compute_system(steps,initiator)
        self.assertEqual(expected, result)

    def test_lsystem7(self):
        expected = "A"
        initiator = list('A')
        rules = {'A':'AB', 'B':'A'}
        self.pcgen.rules = rules
        steps = 0
        result = self.pcgen.compute_system(steps,initiator)
        self.assertEqual(expected, result)

    def test_lsystem8(self):
        expected = "AB"
        initiator = list('A')
        rules = {'A':'AB', 'B':'A'}
        self.pcgen.rules = rules
        steps = 1
        result = self.pcgen.compute_system(steps,initiator)
        self.assertEqual(expected, result)
    
    def test_recursion_limit(self):
        testls = lsystem.Lsystem(lsystem.Lsystem.DRAGON)
        steps = 10
        result = testls.compute_system(steps)
        
        

if __name__ == '__main__':
    unittest.main()
