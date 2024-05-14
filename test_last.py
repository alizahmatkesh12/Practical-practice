from unittest import TestCase
import last
import traceback


class LastTests(TestCase):
    
    def test_many(self):
        self.assertEqual(last.Last([x for x in range(5)]), 4)
     
        
    def test_default_value(self):
        self.assertEqual(last.Last([],"a"), "a")  
       
          
    def test_empty_valueError(self):
        try:
            last.Last([])
        except ValueError:
            format_exec = traceback.format_exc()
            self.assertIn("last() was called on an emtpy iterable and  no default provided", format_exec)   
            
            
    def test_basic(self):
        cases = [
            (range(5), 4),
            (iter(range(4)), 3),
            (iter(range(1)), 0),
            (range(1), 0),
            ({n: str(n) for n in range(5)}, 4),
        ]        
        
        for iterable, excepted in cases:
            with self.subTest(iterable = iterable):
                self.assertEqual(last.Last(iterable), excepted)    
                

    def test_default(self):
        cases = [
            (range(1),None, 0),
            ([], None, None),
            ({}, None, None),
            (iter([]), None, None),
        ]                
                
        for iterable, default, excepted in cases:
            with self.subTest(args =(iterable, default)):
                self.assertEqual(last.Last(iterable, default), excepted)
                
                
    def test_empty(self):
        for iterable in ([], iter(range(0))):
            with self.subTest(iterable = iterable):
                with self.assertRaises(ValueError):
                    last.Last(iterable)                
                            
                