#!/usr/bin/env python3
"""
0-basic_cache.py
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    creates a basic dictionary
    """

    def put(self, key, item):
        """
        set a key and item to create a dictionary
        """

        if key is not None and item is not None:
            self.cache_data.update({key: item})

    def get(self, key):
        """
        fetches the value in  a dictionary using the key
        """
        return self.cache_data.get(key, None)
