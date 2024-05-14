from _collections_abc import Sequence   
from collections import deque   

_marker = object()

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
    
    
#print(Last([]))    

