#!/usr/bin/env python3
"""First-In First-Out caching module.
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary
    """

    def __init__(self):
        # Initializes the cache
        super().__init__()

    def put(self, key, item):
        """Adds an item in the cache"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            # Remove the first item in cache (FIFO)
            first_key = next(iter(self.cache_data))
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}\n")

        # Assign the item value for the key
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an item by key.
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
