#!/usr/bin/env python3
"""
1-fifo_cache.py
"""
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """
    acts as a first in first out caching algorithm
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        creates a dictionary and discard once greater than
        MAX_ITEMS
        """

        if key is not None and item is not None:
            self.cache_data.update({key: item})

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded_key, discarded_value = next(
                    iter(self.cache_data.items())
                    )
            self.cache_data.pop(discarded_key)
            print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """
        retrieves a value from a dictionary
        """

        return self.cache_data.get(key, None)
