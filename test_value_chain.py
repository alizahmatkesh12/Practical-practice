from unittest import TestCase
from value_chain import value_chain

class ValueChainTests(TestCase):
    def test_empty(self):
        actual = list(value_chain())
        expected = []
        
        self.assertEqual(actual, expected)
        
    def test_simple(self):
        actual = list(value_chain(1, 2.17, False, 'foo'))
        expected = [1, 2.17, False, 'foo']    
        
        self.assertEqual(actual, expected)
        
    def test_more(self):
        actual =  list(value_chain(b'bar', [1, 2, 3], 4, {'key':1}))
        expected = [b'bar', 1, 2, 3, 4, 'key']
        
        self.assertEqual(actual, expected)
        
        
    def test_empty_lists(self):
        actual =  list(value_chain(1, 2, [], [3, 4]))
        expected = [1, 2, 3, 4] 
        
        self.assertEqual(actual, expected)
        
    def test_complex(self):
        obj = object()
        actual = list(
            value_chain(
                (1, (2, (3,))),
                ['foo', ['bar', ['baz']], 'tic'],
                {'key':{'foo':1}},
                obj,
            )
        )     
        expected = [1, (2, (3,)), 'foo', ['bar',['baz']], 'tic', 'key', obj]    
        
        self.assertEqual(actual, expected)        