from itertools import chain

def interleave(*iterable):
    
    return chain.from_iterable(zip(*iterable))