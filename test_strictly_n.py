from unittest import TestCase
from strictly_n import strictly_n, raise_

class StriclyNTests(TestCase):
    
    def test_basic(self):
        iterable = ['a', 'b', 'c', 'd']
        n = 4
        actual = list(strictly_n(iterable, n))
        expected = iterable
        self.assertEqual(actual, expected)
        
    def test_too_short_defualt(self):
        iterable = ['a', 'b', 'c', 'd']
        n = 5
        with self.assertRaises(ValueError) as exe:
            list(strictly_n(iterable, n))
        self.assertEqual(
            "Too few items in iterable (got 4)", exe.exception.args[0]
        )
        
    def test_too_long_defualt(self):
        iterable = ['a', 'b', 'c', 'd']
        n = 3
        with self.assertRaises(ValueError) as exec:
            list(strictly_n(iterable,n))
            
        self.assertEqual(
            "Too many items in iterable (got at least 4)", exec.exception.args[0]
        )    
    
    def test_too_short_custom(self):
        call_count = 0
        def too_short(item_count):
            nonlocal call_count
            call_count += 1
            
        iterable = ['a', 'b', 'c', 'd']
        n = 6
        actual = []
        
        for item in strictly_n(iterable, n, too_short=too_short):
            actual.append(item)
            
        expected = ['a', 'b', 'c', 'd']
        self.assertEqual(actual, expected)
        self.assertEqual(call_count, 1) 
        
    
    def test_too_long_custom(self):    
        import logging
           
        iterable = ['a', 'b', 'c', 'd']
        n = 2
        too_long = lambda item_count: logging.warning(
            f'Picked the first {n} items'
        )   

        with self.assertLogs(level="WARNING") as exec:
            actual = list(strictly_n(iterable, n, too_long=too_long))
            
        self.assertEqual(actual, ['a', 'b'])
        self.assertIn('Picked the first 2 items', exec.output[0])           


# class TestStrictlyN(TestCase):
#     def test_too_short(self):
#         with self.assertRaises(ValueError) as cm:
#             list(strictly_n([1, 2], 3))
#         self.assertEqual(str(cm.exception), "Too few items in iterable (got 2)")
        
#     def test_too_long(self):
#         with self.assertRaises(ValueError) as cm:
#             list(strictly_n([1, 2, 3, 4], 3))
#         self.assertEqual(str(cm.exception), "Too many items in iterable (got 4)")
    
#     def test_exact(self):
#         result = list(strictly_n([1, 2, 3], 3))
#         self.assertEqual(result, [1, 2, 3])
        
#     def test_custom_too_short(self):
#         custom_message = "Custom too short message"
#         with self.assertRaises(ValueError) as cm:
#             list(strictly_n([1, 2], 3, too_short=lambda count: raise_(ValueError, custom_message)))
#         self.assertEqual(str(cm.exception), custom_message)
        
#     def test_custom_too_long(self):
#         custom_message = "Custom too long message"
#         with self.assertRaises(ValueError) as cm:
#             list(strictly_n([1, 2, 3, 4], 3, too_long=lambda count: raise_(ValueError, custom_message)))
#         self.assertEqual(str(cm.exception), custom_message)
