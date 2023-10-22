#!/usr/bin/env python3
"""
0-simple_helper_function.py
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int]:
    """
    This a simple pagination function that evaluate offset
    """
    # calculating for offset (page -1)*page_size
    start_index = (page - 1) * page_size
    end_index = page * page_size
    result: Tuple[int] = (start_index, end_index)
    return result
