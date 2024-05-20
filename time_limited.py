from time import monotonic


class time_limited:
    def __init__(self, limit_seconds, iterable):
        if limit_seconds < 0:
            raise ValueError('limit_seconds must be positive')
        self.limit_seconds = limit_seconds
        self._iterable = iter(iterable)
        self._start_time = monotonic()
        self.timed_out = False

    def __iter__(self):
        return self

    def __next__(self):
        if self.limit_seconds == 0:
            self.timed_out = True
            raise StopIteration
        item = next(self._iterable)
        if monotonic() - self._start_time > self.limit_seconds:
            self.timed_out = True
            raise StopIteration

        return item
    
    
    
    
# def __init__(self, limit_seconds, iterable):
#     if limit_seconds < 0:
#         raise ValueError('limit_seconds must be positive')
#     self.limit_seconds = limit_seconds
#     self._iterable = iter(iterable)
#     self._start_time = monotonic()
#     self.timed_out = False
    
# def __iter__(self):
#     return self

# def __next__(self):
#     item = next(self._iterable)
#     if monotonic() - self._start_time > self.limit_seconds:
#         self.timed_out = True
#         raise StopIteration
    # return item      