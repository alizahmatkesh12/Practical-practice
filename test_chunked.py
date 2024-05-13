from unittest import TestCase
import chunked


class TakeTests(TestCase):
    def test_smiple_take(self):
        t = chunked.take(range(10), 5)
        self.assertEqual(t,[0,1,2,3,4])
        
    def test_null_take(self):
        t = chunked.take(range(10), 0)
        self.assertEqual(t, [])
        
    def test_negative_take(self):
        self.assertRaises(ValueError, lambda: chunked.take(range(10), -3))       
    
    def test_too_much_take(self):
        t = chunked.take(range(5), 10)
        self.assertEqual(t, [0,1,2,3,4])
        
class ChunkedTests(TestCase):
    def test_even(self):
        self.assertEqual(
            list(chunked.chunked([1,2,3,4,5,6], 3)), [[1,2,3], [4,5,6]]
        )
        
    def test_odd(self):
        self.assertEqual(
            list(chunked.chunked([1,2,3,4,5,6,7,8], 3)), [[1,2,3],[4,5,6],[7,8]]
        )    
        
    def test_None(self):
        self.assertEqual(
            list(chunked.chunked([1,2,3,4,5,6,7], None)), [[1,2,3,4,5,6,7]]
        )
        
    def test_strict_False(self):
        self.assertEqual(
            list(chunked.chunked([1,2,3,4,5,6,7], None, strict=False)), [[1,2,3,4,5,6,7]]
        )    
        
    def test_strict_True(self):
        def f():
            return list(chunked.chunked([1,2,3,4,5], 3, strict=True))
            
        self.assertRaisesRegex(
            ValueError, "iterator is not divisible by n",f
        )
        self.assertEqual(
            list(chunked.chunked([1,2,3,4,5,6,7,8,9], 3, strict=True)),
            [[1,2,3],[4,5,6],[7,8,9]]
        )

    def test_strict_true_size_None(self):
        def f():
            return list(chunked.chunked([1,2,3,4,5], None, strict=True))
        
        self.assertRaisesRegex(
            ValueError, "n cant be None when strict is True", f
        )