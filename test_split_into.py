from unittest import TestCase
from split_into import split_into


class SplitIntoTests(TestCase):
    def test_iterable_just_right(self):
        actual = list(
            split_into(
            iterable=[1, 2, 3, 4, 5, 6, 7, 8, 9],
            sizes=[2, 3, 4]
        ))
        expected = [[1, 2], [3, 4, 5], [6, 7, 8, 9]]
        
        self.assertEqual(actual, expected)
    
    def test_iterable_too_small(self):
        actual = list(
            split_into(
            iterable=[1, 2, 3, 4, 5, 6, 7],
            sizes=[2, 3, 4]
        ))
        expected = [[1, 2], [3, 4, 5], [6, 7]]     
        
        self.assertEqual(actual, expected)
        
    def test_iterable_too_small_extra(self):
        actual = list(
            split_into(
            iterable=[1, 2, 3, 4, 5, 6, 7],
            sizes=[2, 3, 4, 5]
        ))
        expected = [[1, 2], [3, 4, 5], [6, 7], []]
        
        self.assertEqual(actual, expected)
        
    def test_iterable_too_large(self):
        actual = list(
            split_into(
            iterable=[1, 2, 3, 4, 5, 6, 7, 8, 9],
            sizes=[2, 3, 2]
        ))                
        expected = [[1, 2], [3, 4, 5], [6, 7]]
        
        self.assertEqual(actual, expected)
    
    def test_using_none_with_leftover(self):
        actual = list(
            split_into(
            iterable=[1, 2, 3, 4, 5, 6, 7, 8, 9],
            sizes=[2, 3, None]
        ))                
        expected = [[1, 2], [3, 4, 5], [6, 7, 8, 9]]
        
        self.assertEqual(actual, expected)
        
    def test_using_none_without_leftover(self):
        actual = list(
            split_into(
            iterable=[1, 2, 3, 4, 5, 6, 7, 8, 9],
            sizes=[2, 3, 4, None]
        ))
        expected = [[1, 2], [3, 4, 5], [6, 7, 8, 9], []]
        
        self.assertEqual(actual, expected)
        
    def test_using_none_mid_sizes(self):
        actual = list(
            split_into(
            iterable=[1, 2, 3, 4, 5, 6, 7, 8, 9],
            sizes=[2, 3, None, 4]
        ))            
        expected = [[1, 2], [3, 4, 5], [6, 7, 8, 9]]
        
        self.assertEqual(actual, expected)
        
    def test_iterable_empty(self):
        actual = list(
            split_into(
            iterable=[],
            sizes=[2, 4, 2]
        ))
        expected = [[], [], []]            
        
        self.assertEqual(actual, expected)
        
    def test_iterable_empty_using_none(self):  
        actual = list(
            split_into(
            iterable=[],
            sizes=[2, 4, None, 2]
        ))       
        expected = [[], [], []]   
        
        self.assertEqual(actual, expected) 
        
    def test_sizes_empty(self): 
        actual = list(
            split_into(
            iterable=[1, 2, 3, 4, 5, 6, 7, 8, 9],
            sizes=[]
        ))
        expected = []                           
        
        self.assertEqual(actual, expected) 
        
    def test_test_both_empty(self):
        actual = list(
            split_into(
            iterable=[],
            sizes=[]
        ))
        expected = []                           
        
        self.assertEqual(actual, expected)
                         
    def test_test_bool_in_sizes(self):
        actual = list(
            split_into(
            iterable=[1, 2, 3, 4, 5, 6, 7, 8, 9],
            sizes=[3, True, 2, False]
        ))
        expected = [[1, 2, 3], [4], [5, 6], []]                           
        
        self.assertEqual(actual, expected)                 
        
    def test_test_invalid_in_sizes(self):
        with self.assertRaises(ValueError):
            list(split_into(
                iterable=[1, 2, 3, 4, 5, 6, 7, 8, 9],
                sizes=[1, [], 3]
            ))
        
    def test_invalid_in_sizes_after_none(self):
        actual = list(
            split_into(
            iterable=[1, 2, 3, 4, 5, 6, 7, 8, 9],
            sizes=[3, 4, None, []]
        ))
        expected = [[1, 2, 3], [4, 5, 6, 7], [8, 9]]                           
        
        self.assertEqual(actual, expected)
    
    def test_generator_iterable_integrity(self):
        iterable = (i for i in range(10))
        sizes=[2, 3]
        actual = list(split_into(iterable, sizes))
        expected = [[0, 1], [2, 3, 4]]                           
                                                  
        self.assertEqual(actual, expected)
        
        iterable_actual = list(iterable)   
        iterable_expected = [5, 6, 7, 8, 9]
        self.assertEqual(iterable_actual, iterable_expected)
        
    def test_generator_sizes_integrity(self):
        iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        sizes=(i for i in [1, 2, None, 3, 4])
        actual = list(split_into(iterable, sizes))
        expected = [[1], [2, 3], [4, 5, 6, 7, 8, 9]]       

        self.assertEqual(actual, expected)
        
        sizes_expected = [3, 4]
        sizes_actual = list(sizes)  
        
        self.assertEqual(sizes_actual, sizes_expected)                       