#!/usr/bin/env python3
""" module with index_range fn """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ return tuple (2) with start and end index correspoding
        to range of indexes to return in a list based on the
        pagination parameters
    """
    end: int = page_size * page
    start: int = end - page_size
    return start, end
