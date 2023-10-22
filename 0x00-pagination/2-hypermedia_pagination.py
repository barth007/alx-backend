#!/usr/bin/env python3
"""
1-simple_pagination.py
"""
import csv
import math
from typing import List, Dict, Tuple, Union


def index_range(page: int, page_size: int) -> Tuple[int]:
    """
    This checks and returns the start and end indexes in a tuple
    """
    # calculating for offset (page -1)*page_size
    start_index = (page - 1) * page_size
    end_index = page * page_size
    result: Tuple[int] = (start_index, end_index)
    return result


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
        """
        This get a specify required number of content as a list
        """

        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        index_value = index_range(page, page_size)
        data = self.dataset()
        # using slice
        start_index = index_value[0]
        end_index = index_value[1]

        if start_index >= len(data) or end_index > len(data):
            return []
        list_content = data[start_index:end_index]
        return list_content

    def get_hyper(self,
                  page: int = 1,
                  page_size: int = 10) -> Dict[str, Union[List[List], int]]:
        """
        This function returns a hyper link to next and prev pages
        making use of the HATEOAS principle
        """

        data = self.get_page(page, page_size)
        hyper_linked = {}
        if len(data) > 0:
            hyper_linked['page_size'] = page_size
            hyper_linked['page'] = page
            hyper_linked['data'] = data
            all_dataset = self.dataset()
            count = 0
            for data_s in all_dataset:
                count += 1
            all_pages = math.ceil(count / page_size)
            hyper_linked['next_page'] = page + 1 if page < all_pages else None
            hyper_linked['prev_page'] = page - 1 if page > 1 else None
            hyper_linked['total_pages'] = all_pages
            return hyper_linked
        return hyper_linked
