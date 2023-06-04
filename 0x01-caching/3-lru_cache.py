#!/usr/bin/env python3
"""
a class LRUCache that inherits from BaseCaching and is a caching system.
"""


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class represents a caching system that uses the LRU (Least Recently Used) algorithm.

    It inherits from the BaseCaching class and implements the put and get methods.

    Attributes:
        cache_data (dict): A dictionary to store the key-value pairs representing the cache data.

    Methods:
        __init__(): Initializes the LRUCache object by calling the parent class's init method.
        put(key, item): Assigns the item value for the given key in the cache_data dictionary.
                        If key or item is None, this method does nothing.
                        If the number of items in the cache exceeds the maximum allowed,
                        it removes the least recently used item from the cache.
        get(key): Retrieves the value associated with the given key from the cache.
                  If key is None or doesn't exist in the cache_data dictionary, None is returned.
                  Otherwise, it moves the accessed key-value pair to the end of the cache_data dictionary
                  to reflect its most recent usage.
    """

    def __init__(self):
        """
        Initializes a new instance of the LRUCache class.
        Calls the init method of the parent class (BaseCaching).
        """
        super().__init__()

    def put(self, key, item):
        """
        Adds an item to the cache.

        Args:
            key: The key of the item.
            item: The value of the item.

        If key or item is None, this method does nothing.
        If the number of items in the cache exceeds the maximum allowed,
        it removes the least recently used item from the cache.
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            # Remove the least recently used item (LRU)
            lru_key = next(iter(self.cache_data))
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}\n")

        # Assign the item value for the key
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves the value associated with the given key from the cache.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The value associated with the key if it exists in the cache,
            otherwise returns None.

        If key is None or doesn't exist in the cache_data dictionary, None is returned.
        Otherwise, it moves the accessed key-value pair to the end of the cache_data dictionary
        to reflect its most recent usage.
        """
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed key-value pair to the end of the cache_data dictionary
        value = self.cache_data.pop(key)
        self.cache_data[key] = value

        return value
