#!/usr/bin/env python3

""" Create a class BasicCache that inherits from BaseCaching and is a caching system: """

BaseCaching = __import__('base_caching').BaseCaching

class BasicCache(BaseCaching):
    """ Create a class BasicCache that inherits from BaseCaching and is a caching system: """

    def __init__(self):
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """ This method must assign to the dictionary self.cache_data the item value for
            the key key.
        """
        # self.cache_data = {}
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ This method must return the value in self.cache_data linked to key."""

        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]