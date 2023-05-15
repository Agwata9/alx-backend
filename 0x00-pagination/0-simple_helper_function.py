#!/usri/bin/env python3
"""
0-simple_helper_function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    a  function that returns tuple of start and end page
    """
    final_size: int = page * page_size
    start_size: int = final_size - page_size
    the_range = (start_size, final_size)
    return the_range
