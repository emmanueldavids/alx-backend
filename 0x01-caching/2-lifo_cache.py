#!/usr/bin/env python3

""" Create a class LIFOCache that inherits from BaseCaching
    and is a caching system.
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ Create a class LIFOCache that inherits from BaseCaching
        and is a caching system.
    """

    def __init__(self):
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """ If key or item is None, this method should not do
            anything.
        """

        if key is None or item is None:
            return

        cache_data = list(self.cache_data.items())
        if len(cache_data) >= BaseCaching.MAX_ITEMS:
            last_item = cache_data[-1]
            del self.cache_data[last_item[0]]
            print(f"DISCARD: {last_item[0]}")

        self.cache_data[key] = item

    def get(self, key):
        """ This method must return the value in self.cache_data
            linked to key.
        """

        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
