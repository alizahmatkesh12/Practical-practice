from unittest import TestCase
from SequenceViewT import SequenceViewT


class SequenceViewTests(TestCase):
    def test_init(self):
        view = SequenceViewT((1, 2, 3))
        self.assertEqual(repr(view), "SequenceViewT((1, 2, 3))")
        self.assertRaises(TypeError, lambda: SequenceViewT({}))
        
    def test_update(self):
        seq = [1, 2, 3]
        view = SequenceViewT(seq)
        self.assertEqual(len(view), 3)
        self.assertEqual(repr(view), "SequenceViewT([1, 2, 3])")
        
        seq.pop()
        self.assertEqual(len(view), 2)
        self.assertEqual(repr(view), "SequenceViewT([1, 2])")
        
    def test_indxeing(self):
        seq = ('a', 'b', 'c', 'd', 'e', 'f')
        view = SequenceViewT(seq)
        for i in range(-len(seq), len(seq)):
            self.assertEqual(view[i], seq[i])
    
    def test_abc_method(self):
        seq = ('a', 'b', 'c', 'd', 'e', 'f', 'f')   
        view = SequenceViewT(seq) 
        
        self.assertIn('b', view)
        self.assertNotIn('g', view)
        self.assertEqual(list(iter(view)), list(seq))
        self.assertEqual(list(reversed(view)), list(reversed(seq)))
        self.assertEqual(seq.index('b'), 1)
        self.assertEqual(view.count('f'), 2)    
        