from unittest import TestCase
from itertools import cycle
import repeat_each

class RepeatEachTests(TestCase):
    
    def test_default(self):
        actual = list(repeat_each.repeat_each('ABC'))
        expected = ['A', 'A', 'B', 'B', 'C', 'C']
        self.assertEqual(actual, expected)
        
    def test_basic(self):
        actual = list(repeat_each.repeat_each('ABC', 3))
        expected = ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C']
        self.assertEqual(actual, expected)
        
    def test_empty(self):
        actual = list(repeat_each.repeat_each(''))
        expected = []
        self.assertEqual(actual, expected)

    def test_no_repeat(self):
        actual = list(repeat_each.repeat_each('ABC', 0))
        expected = []
        self.assertEqual(actual, expected)
        
    def test_negative_repeat(self):
        repeater = repeat_each.repeat_each(cycle('AB'))
        actual = repeat_each.take(repeater, 6)
        expected = ['A', 'A', 'B', 'B', 'A', 'A']
        self.assertEqual(actual, expected)
    






        
        
        
        
        
        
        