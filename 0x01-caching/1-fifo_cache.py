#!/usr/bin/python3
""" FIFOCache module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            cache_data = self.cache_data
            if len(cache_data) == self.MAX_ITEMS:
                first_key = list(cache_data.keys())[0]
                if key not in cache_data:
                    del cache_data[first_key]
                    print(f"DISCARD: {first_key}")
            cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
