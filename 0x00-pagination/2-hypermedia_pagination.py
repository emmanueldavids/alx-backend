import csv
import math
from typing import List

class Server:
    DATA_FILE = "data/Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.load_dataset()

    def load_dataset(self):
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

    def dataset(self) -> List[List]:
        self.load_dataset()
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int) and isinstance(page_size, int) and page > 0 and page_size > 0

        start, end = self.index_range(page, page_size)
        if start >= len(self.__dataset):
            return []

        return self.__dataset[start:end]

    def index_range(self, page: int, page_size: int) -> tuple:
        start_index = (page - 1) * page_size
        end_index = page * page_size
        return start_index, end_index

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        data = self.get_page(page, page_size)
        next_page = page + 1 if self.index_range(page + 1, page_size)[0] < len(self.__dataset) else None
        prev_page = page - 1 if page > 1 else None
        total_pages = math.ceil(len(self.__dataset) / page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }

# Test the Server class
if __name__ == "__main__":
    server = Server()

    print(server.get_hyper(1, 2))
    print("---")
    print(server.get_hyper(2, 2))
    print("---")
    print(server.get_hyper(100, 3))
    print("---")
    print(server.get_hyper(3000, 100))
