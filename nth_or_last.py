from itertools import islice 
from _collections_abc import Sequence   
from collections import deque


_marker = object()
# a= [0,1,2]


def Last(iterable, default = _marker):
    try:
        if isinstance(iterable, Sequence):
            return iterable[-1]
        elif hasattr(iterable, '__reverse__'):
            return next(reversed(iterable))
        else:
            return deque(iterable, maxlen=1)[-1]
        
    except (IndexError , TypeError, StopIteration) as e:
        if default is _marker:
            raise ValueError(
                "last() was called on an emtpy iterable and  no default provided"
            ) from e
            
        return default  
    
    
def nth_or_last(iterable, n, default = _marker):
    return Last(islice(iterable, n + 1), default = default) 


# print(nth_or_last(a, 3))