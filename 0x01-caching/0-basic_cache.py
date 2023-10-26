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
        create a set key and item to create a dictionary
        """

        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        fetchs the value in  a dictionary using the key
        """
        if key in self.cache_data:
            return self.cache_data.get(key)
        return None
