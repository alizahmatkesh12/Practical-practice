from unittest import TestCase
from only import only


class OnlyTests(TestCase):
    def test_defualts(self):
        self.assertEqual(only([]), None)
        self.assertEqual(only([1]), 1)
        self.assertRaises(ValueError, lambda: only([1, 2]))
        
    def test_custom_value(self):
        self.assertEqual(only([], defualt='!'), '!')
        self.assertEqual(only([1], defualt='!'), 1)
        self.assertRaises(ValueError, lambda: only([1, 2], defualt='!'))
        
        
    def test_custom_exception(self):
        self.assertEqual(only([], too_long=RuntimeError), None)
        self.assertEqual(only([1], too_long=RuntimeError), 1)
        self.assertRaises(RuntimeError, lambda: only([1,2,3], too_long=RuntimeError))
        
        
    def test_defualt_exception_message(self):
        self.assertRaisesRegex(
            ValueError,
            "Expected exactly one item in iterable, but got foo, bar, and perhaps more",
            lambda: only(["foo", "bar", "baz"])
        )    