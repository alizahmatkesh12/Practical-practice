from unittest import TestCase, skipIf
from itertools import accumulate
from difference import difference
from operator import add
from sys import version_info


class DiferenceTests(TestCase):
    def test_normal(self):
        iterable = [10, 20, 30, 40, 50]
        actual = list(difference(iterable))
        expected = [10, 10, 10, 10, 10]
        
        self.assertEqual(actual, expected)
        
        
    def test_custom(self):
        iterable = [10, 20, 30, 40, 50]
        actual = list(difference(iterable, add))
        expected = [10, 30, 50, 70, 90]
        
        
    def test_roundtrip(self):
        original = list(range(10))
        accumulated = accumulate(original)
        actual = list(difference(accumulated))
        
        self.assertEqual(actual, original)
        
    def test_one(self):
        self.assertEqual(list(difference([0])), [0])
        
    def test_empty(self):
        self.assertEqual(list(difference([])), [])
    
    @skipIf(version_info[:2] < (3, 8), 'accumulate with initial needs +3.8')  
    def test_initia(self):
        original = list(range(100))
        accumulated = accumulate(original, initial=100)
        actual = list(difference(accumulated, initial=100))
        self.assertEqual(actual, original)
        
    
        
