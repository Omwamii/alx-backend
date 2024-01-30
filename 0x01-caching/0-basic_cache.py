#!/usr/bin/env python3
''' module with 'BasicCache class '''

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ implementation of basic caching """

    def put(self, key, item):
        ''' assign to self.cached_data key-item pair
        '''
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        ''' return value of self.cached_data linked to key
        '''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
