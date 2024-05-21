from collections.abc import Sequence


class SequenceViewT(Sequence):
    def __init__(self, target):
        if not isinstance(target, Sequence):
            raise TypeError
        self._target = target
    def __getitem__(self, index):
        return self._target[index]
    
    def __len__(self):
        return len(self._target)
    
    def __repr__(self):
        return f'{self.__class__.__name__}({self._target})'
    

    