#!/usr/bin/env python3
''' module with FIFOCache class '''

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    ''' FIFO cache implentation '''
    def __init__(self):
        ''' __init__ '''
        super().__init__()

    def put(self, key, item):
        ''' add item to cache and delete if MAX_ITEMS reached
        '''
        if key and item:
            if len(self.cache_data.keys()) >= self.MAX_ITEMS:
                # get the first item in the cache to delete
                first = list(self.cache_data.keys())[0]  # (FIFO)
                del self.cache_data[first]
                print(f"DISCARD: {first}")
            self.cache_data[key] = item

    def get(self, key):
        ''' get item from cache '''
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
