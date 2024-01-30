#!/usr/bin/env python3
''' module with LIFOCache '''


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    ''' LIFO cache implementation '''
    def __init__(self):
        ''' __init__ '''
        # keep track of updated values to count as new inserts
        self.updates = list()  # NB: only for when cache near max
        super().__init__()

    def put(self, key, item):
        ''' assigns key to item in cache, deletes last
            item if cache is full
        '''
        if key and item:
            if len(self.cache_data.keys()) >= self.MAX_ITEMS:
                if key in self.cache_data:
                    self.updates.append(key)  # will b next to delete
                else:
                    if len(self.updates) > 0:
                        last = self.updates[0]
                    else:
                        last = sorted(list(self.cache_data.keys()))[-1]
                    del self.cache_data[last]
                    print(f"DISCARD: {last}")
                    if len(self.updates) > 0:
                        self.updates.clear()
            self.cache_data[key] = item

    def get(self, key):
        ''' get data from cache '''
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
