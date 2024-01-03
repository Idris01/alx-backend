#!/usr/bin/python3
""" LRUCache module
"""
from datetime import datetime
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    def __init__(self):
        super().__init__()
        self.__durations = {}

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            cache_data = self.cache_data
            durations = self.__durations

            if len(cache_data) == self.MAX_ITEMS and key not in cache_data:
                duration_list = list(durations.values())
                indx = duration_list.index(min(duration_list))
                last_key = list(durations.keys())[indx]

                del durations[last_key]
                del cache_data[last_key]
                print(f"DISCARD: {last_key}")
            cache_data[key] = item
            durations[key] = f"{datetime.now().timestamp()}".replace(".", "")

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            value = self.cache_data.get(key)
            self.__durations[key] = (
                    f"{datetime.now().timestamp()}".replace(".", ""))
            return value
        return None
