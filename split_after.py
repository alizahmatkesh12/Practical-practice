def split_after(iterable, pred, max_split = -1):
    if max_split == 1:
        yield list(iterable)
        return
    
    buf = []
    it = iter(iterable)
    for item in it:
        buf.append(item)
        if pred(item) and buf:
            yield buf
            if max_split == 1:
                yield list(it)
                return
            buf = []
            max_split -= 1
            
    if buf:
        yield buf
        
# print(list(split_after('a,b,c,d', lambda c: c != ',', max_split=2)))                