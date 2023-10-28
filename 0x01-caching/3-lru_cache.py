#!/usr/bin/env python3
"""
3-lru_cache.py
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    implements the LRU cache algorithm
    """

    def __init__(self):
        super().__init__()
        # self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        set a key to a value
        """
        if key is None and item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            least_used = next(iter(self.cache_data))
            del self.cache_data[least_used]
            print(f"Discard: {least_used}")
        self.cache_data[key] = item
        # self.cache_data.move_to_end(key, last=False)

    def get(self, key):
        """
        fetches a values in a dict with a given key
        """

        if key is None:
            return None
        return self.cache_data.get(key, None)
