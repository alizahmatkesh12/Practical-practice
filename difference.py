from operator import sub
from itertools import chain, tee, starmap


def difference(iterable, func=sub, *, initial=None):
    a, b = tee(iterable)
    
    try:
        first = [next(b)]
    except StopIteration:
        return iter([])
    
    if initial is not None:
        first = []
        
        
    return chain(first, starmap(func, zip(b, a)))    

