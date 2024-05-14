from unittest import TestCase
import nth_or_last
import traceback


class NthOrLastTests(TestCase):
    
    def test_basic(self):
        self.assertEqual(nth_or_last.nth_or_last(range(3), 1), 1)
        self.assertEqual(nth_or_last.nth_or_last(range(3), 3), 2)
        
    def test_defualt_value(self):
        default = 10
        self.assertEqual(nth_or_last.nth_or_last(range(0), 3, default), default)
        
    def test_iterable_no_defualt(self):
        self.assertRaises(ValueError, lambda: nth_or_last.nth_or_last(range(0), 0))               
        
