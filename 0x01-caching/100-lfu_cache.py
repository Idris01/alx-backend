#!/usr/bin/python3
""" LFUCache module
"""
from datetime import datetime
from base_caching import BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """ LFUCache defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    def __init__(self):
        super().__init__()
        self.__durations = {}
        self.__hits = defaultdict(lambda: 0)

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            cache_data = self.cache_data
            durations = self.__durations
            hits = self.__hits

            if len(cache_data) == self.MAX_ITEMS and key not in cache_data:
                duration_list = list(durations.values())
                hit_list = list(hits.values())
                min_hit = min(hit_list)
                min_hit_index = [
                        index for index, val in enumerate(hit_list)
                        if val == min_hit]
                last_key = list(hits.keys())[min_hit_index[0]]
                if len(min_hit_index) > 1:
                    new_list = [
                            (itm, duration_list[itm])
                            for itm in min_hit_index]
                    lru_index = min(new_list, key=lambda x: x[1])[0]
                    last_key = list(hits.keys())[lru_index]

                del durations[last_key]
                del cache_data[last_key]
                del hits[last_key]
                print(f"DISCARD: {last_key}")
            cache_data[key] = item
            hits[key] += 1
            durations[key] = f"{datetime.now().timestamp()}".replace(".", "")

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            value = self.cache_data.get(key)
            self.__durations[key] = (
                    f"{datetime.now().timestamp()}".replace(".", ""))
            self.__hits[key] += 1
            return value
        return None
