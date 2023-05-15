#!/usri/bin/env python3
"""
a function named index_range that takes two integer arguments
"""

def index_range(page: int, page_size: int) -> tuple[int, int]:
   """
   Args:
            page: Current page
            page_size: Total size of the page
    Return:
            tuple with the range start and end size page
   """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
