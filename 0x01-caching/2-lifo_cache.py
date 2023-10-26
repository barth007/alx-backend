#!/usr/bin/env python3
"""
2-lifo_cache.py
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    Serves as a cache using the LIFO algorithm
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        sets a key and an item to create a dictionary
        and discard last item if above MAX_ITEMS
        """

        if key is not None and item is not None:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            listed_keys = list(self.cache_data.keys())
            discarded_key = listed_keys[-1]
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """
        fetches a value by using a given key
        """

        return self.cache_data.get(key, None)
