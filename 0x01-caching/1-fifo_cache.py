#!/usr/bin/env python3

""" Create a class FIFOCache that inherits from BaseCaching
    and is a caching system.
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ This class FIFOCache that inherits from BaseCaching and
        is a caching system.
    """

    def __init__(self):
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """ This method Must assign to the dictionary self.cache_data
            the item value for the key key.
        """

        if key is None or item is None:
            return

        if key not in self.cache_data:
            self.cache_data[key] = item
            return

        if len(self.cache_data[key]) >= BaseCaching.MAX_ITEMS:
            removed_key = next((iter(self.cache_data)))
            del self.cache_data[removed_key]
            print(f"DISCARD: {removed_key}")

        self.cache_data[key] = item

    def get(self, key):
        """ This method must return the value in self.cache_data linked
            to key.
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
