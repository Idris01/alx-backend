#!/usr/bin/env python3
"""This module define a Server class and index_range function
"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """Get the corresponding page range for a given page size and number
    """
    start = (page - 1) * page_size
    return (start, start + page_size)


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
        """Get pages from dataset
        """
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert (page > 0 and page_size > 0)
        start, end = index_range(page, page_size)
        return self.dataset()[start:end]
