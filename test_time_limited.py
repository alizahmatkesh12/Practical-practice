from unittest import TestCase
from time_limited import time_limited
from itertools import count
from time import sleep

class TimeLimitedTests(TestCase):
    def test_basic(self):
        def generator():
            yield 1
            yield 2
            sleep(0.2)
            yield 3
            
        iterable = time_limited(0.1, generator())
        actual = list(iterable)
        expected = [1, 2]
        
        self.assertEqual(actual, expected)
        self.assertTrue(iterable.timed_out)
        
        
    def test_complete(self):
        iterable = time_limited(2, iter(range(10)))
        actual = list(iterable)
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        self.assertEqual(actual, expected)
        self.assertFalse(iterable.timed_out)
        
    def test_zero_limit(self):
        iterable = time_limited(0, count())
        actual = list(iterable)
        expected = []
        
        self.assertEqual(actual, expected)
        self.assertTrue(iterable.timed_out)
    
    def test_invalid_limit(self):
        with self.assertRaises(ValueError):
            list(time_limited(-1, count()))
    