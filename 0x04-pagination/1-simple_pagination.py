#!/usr/bin/env python3
"""Implement a method named get_page that takes two integer
arguments page with default value 1 and page_size with default value 10
"""
import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    Parameters
    ----------
    page : int
        page number
    page_size : int
        size of page

    Returns
    -------
    tuple
        a tuple of size two containing a start
        index and an end index corresponding to
        the range of indexes to return in a list
        for those particular pagination parameters.
    """
    if page <= 1:
        return (0, page_size)
    return ((page * page_size) - page_size, (page * page_size))


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Constructor."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get page from csv dataset"""
        try:
            assert page > 0
            assert page_size > 0
        except Exception:
            raise AssertionError

        dataset = self.dataset()

        if page > len(dataset) or page_size > len(dataset):
            return []
        indexes = index_range(page, page_size)
        return dataset[indexes[0] : indexes[1]]
