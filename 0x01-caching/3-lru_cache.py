#!/usr/bin/env python3
''' module with LRUCache class '''
from datetime import datetime


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    ''' LRU cache implementation '''
    def __init__(self):
        ''' __init__ '''
        super().__init__()
        self.use_count = {}  # keep track of age of items

    def put(self, key, item):
        ''' put item to cache, delete least recently used
            if cache is full

            ---------------------Description---------------

            To keep track of least used items,a timestamp is used.
            for each item accessed or changed, the time of the
            change made is stored in `self.use_count` and used in
            comparing the 'ages' of the items to determine those
            least frequently used
        '''
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS\
                    and key not in self.cache_data:
                # check the least recently used item
                for idx, k in enumerate(self.use_count):
                    if idx == 0:
                        least = k
                    else:
                        if self.use_count[k] < self.use_count[least]:
                            least = k
                del self.cache_data[least]
                del self.use_count[least]
                print(f"DISCARD: {least}")
            self.use_count[key] = datetime.now()  # keep track of age
            self.cache_data[key] = item

    def get(self, key):
        ''' get item from cache '''
        if key is None or key not in self.cache_data:
            return None
        self.use_count[key] = datetime.now()
        return self.cache_data[key]
