#!/usr/bin/env python3
''' module with LRUCache class '''
from datetime import datetime


BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    ''' MRU cache implementation '''
    def __init__(self):
        ''' __init__ '''
        super().__init__()
        self.use_count = {}  # keep track of age of items

    def put(self, key, item):
        ''' put item to cache, delete least frequently used
            if cache is full
        '''
        usage = self.use_count
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS\
                    and key not in self.cache_data:
                # check the least frequently used item
                freq_items = list()
                least = list(usage.keys())[0]
                freq_items.append(least)
                for k, val in usage.items():
                    if val[0] < usage[least][0]:
                        least = k
                        if len(freq_items) > 0:
                            freq_items.clear()
                        freq_items.append(least)
                    elif val[0] == usage[least][0] and least != k:
                        freq_items.append(k)
                # assign def to first for case of only one and many
                least = freq_items[0]
                if len(freq_items) > 1:
                    # use LRU to find least recently used
                    for el in freq_items:
                        if usage[el][1] < usage[least][1]:
                            least = el  # is older hence least used
                del self.cache_data[least]
                del self.use_count[least]
                print(f"DISCARD: {least}")
            if key in self.cache_data:
                freq = self.use_count[key][0]
                self.use_count[key] = ((freq + 1), datetime.now())
            else:
                self.use_count[key] = (0, datetime.now())  # track freq & age
            self.cache_data[key] = item

    def get(self, key):
        ''' get item from cache '''
        if key is None or key not in self.cache_data:
            return None
        freq = self.use_count[key][0]
        self.use_count[key] = (freq + 1, datetime.now())
        return self.cache_data[key]
