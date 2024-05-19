from itertools import islice
def split_into(iterable, sizes):
    it = iter(iterable)
    for size in sizes:
        if size is None:
            yield list(it)
            return
        else:
            yield list(islice(it, size))
            
            
            