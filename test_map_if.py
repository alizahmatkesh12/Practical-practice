from unittest import TestCase 
from map_if import map_if


class MapIfTests(TestCase):
    def test_without_func_else(self):
        iterable = list(range(-5 , 5))
        actual = list(map_if(iterable, lambda x: x>3, lambda x: 'toobig'))
        expected = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 'toobig']
        
        self.assertEqual(actual, expected)
        
        
    def test_with_func_else(self):
        iterable = list(range(-5, 5))
        actual = list(map_if(iterable, lambda x: x>=0, lambda x:'notneg', lambda x:'neg'))
        expected = ['neg'] * 5 + ['notneg'] * 5
        
        self.assertEqual(actual, expected)
        
    def test_empty(self):
        actual = list(map_if([], lambda x:len(x)>3, lambda x:None))
        expected = []
        
        self.assertEqual(actual, expected)        
        
        
        