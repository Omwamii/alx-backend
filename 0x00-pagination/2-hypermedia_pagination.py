#!/usr/bin/env python3
''' module with Server class '''
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ return tuple (2) with start and end index correspoding
        to range of indexes to return in a list based on the
        pagination parameters
    """
    end: int = page_size * page
    start: int = end - page_size
    return start, end


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ method to return a list of pages from dataset """
        assert (isinstance(page, int) and page > 0)
        assert (isinstance(page_size, int) and page_size > 0)
        start, end = index_range(page, page_size)
        # print(f"Start: {start}, End: {end}")
        if start > len(self.dataset()) or end > len(self.dataset()):
            return []
        return self.dataset()[start: end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ returns a dictionary rep of data """
        p_data = self.get_page(page, page_size)
        p_size = len(p_data)
        p_number = page
        p_next = page + 1 if len(p_data) > 0 else None
        p_prev = page - 1 if page - 1 > 0 else None
        p_total = len(self.dataset())
        data = {'page_size': p_size, 'page': p_number, 'data': p_data,
                'next_page': p_next, 'prev_page': p_prev,
                'total_pages': p_total}
        return data
