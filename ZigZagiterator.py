"""
ZigZagiterator

                [1, 2] [3, 4, 5, 6] => 1,2,3,4,5,6
                [[1, 2], [3, 4, 5, 6]]

"""

class ZigZag():
    
    def __init__(self, L1, L2) -> list:
        self.queue = [L1, L2]
        
    def next(self) -> list:
        v = self.queue.pop(0)
        r = v.pop(0)        
        
        if v:
            self.queue.append(v)
        return r
    
    def has_next(self) -> bool:
        if self.queue:
            return True
        return False   
        
        
l1 = [1, 2]
l2 = [3, 4, 5, 6]
d = ZigZag(l1, l2)
while d.has_next():
    print(d.next(), end=' ')        