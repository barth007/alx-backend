#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        paginated dataset with deletion reselience
        """

        indexed_data = self.indexed_dataset()

        # Check if the index is in a valid range
        assert index is None or index in indexed_data

        if index is None:
            # If index is not specified, set it to 0
            index = 0

        # Calculate the next_index by adding the page_size to the current index
        next_index = index + page_size

        # Ensure next_index doesn't exceed the length of the dataset
        max_index = max(indexed_data.keys())
        if next_index > max_index:
            next_index = max_index

        # Get the actual page of data
        page_data = [indexed_data[i] for i in range(index, next_index + 1)]

        return {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": page_data
        }
