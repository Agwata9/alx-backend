#!/usr/bin/python3

"""
This module defines the BasicCache class, which is a caching system that inherits from BaseCaching.
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class that inherits from BaseCaching and implements a caching system.
    """

    def put(self, key, item):
        """
        Store an item in the cache.

        Args:
            key: The key to store the item.
            item: The item to be stored.

        Returns:
            None.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache based on the provided key.

        Args:
            key: The key to retrieve the item.

        Returns:
            The item associated with the key if it exists in the cache, else None.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
