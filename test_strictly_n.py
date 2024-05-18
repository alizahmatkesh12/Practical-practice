from unittest import TestCase
from strictly_n import strictly_n, raise_


class TestStrictlyN(TestCase):
    def test_too_short(self):
        with self.assertRaises(ValueError) as cm:
            list(strictly_n([1, 2], 3))
        self.assertEqual(str(cm.exception), "Too few items in iterable (got 2)")
        
    def test_too_long(self):
        with self.assertRaises(ValueError) as cm:
            list(strictly_n([1, 2, 3, 4], 3))
        self.assertEqual(str(cm.exception), "Too many items in iterable (got 4)")
    
    def test_exact(self):
        result = list(strictly_n([1, 2, 3], 3))
        self.assertEqual(result, [1, 2, 3])
        
    def test_custom_too_short(self):
        custom_message = "Custom too short message"
        with self.assertRaises(ValueError) as cm:
            list(strictly_n([1, 2], 3, too_short=lambda count: raise_(ValueError, custom_message)))
        self.assertEqual(str(cm.exception), custom_message)
        
    def test_custom_too_long(self):
        custom_message = "Custom too long message"
        with self.assertRaises(ValueError) as cm:
            list(strictly_n([1, 2, 3, 4], 3, too_long=lambda count: raise_(ValueError, custom_message)))
        self.assertEqual(str(cm.exception), custom_message)
