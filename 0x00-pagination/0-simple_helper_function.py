#!/usri/bin/env python3
"""
a function named index_range that takes two integer arguments
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    index range function
    """
    final_size: int = page * page_size
    start_size: int = final_size - page_size

    return (start_size, final_size)
