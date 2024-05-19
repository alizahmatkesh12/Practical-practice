from unittest import TestCase
from always_iterable import always_iterable

class AlwaysIterableTests(TestCase):
    def test_single(self):
        self.assertEqual(list(always_iterable(1)), [1])
        
    def test_string(self):
        for obj in ['foo', b'bar', 'baz']:
            actual = list(always_iterable(obj))
            expected = [obj]
            self.assertEqual(actual, expected)
            
    def test_base_type(self):
        dict_obj = {'a':1, 'b':2}
        str_obj = '123'
        
        defualt_actual = list(always_iterable(dict_obj))    
        defualt_expected = list(dict_obj)
        self.assertEqual(defualt_actual, defualt_expected)
        
        custom_actual = list(always_iterable(dict_obj, base_tpye=dict))
        custom_expected = [dict_obj]
        self.assertEqual(custom_actual, custom_expected)
        
    def test_iterables(self):
        self.assertEqual(list(always_iterable([0, 1])), [0, 1])
        self.assertEqual(list(always_iterable([0, 1], base_tpye=list)), [[0, 1]])
        self.assertEqual(list(always_iterable(iter('foo'))), ['f', 'o', 'o'])
        self.assertEqual(list(always_iterable([])), [])
        
        
    def test_none(self):
        self.assertEqual(list(always_iterable(None)), [])
        
    
    def test_generator(self):
        def _get():
            yield 0
            yield 1
            
        self.assertEqual(list(always_iterable(_get())), [0, 1])        
    