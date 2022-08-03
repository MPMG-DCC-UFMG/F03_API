from fastapi import HTTPException

from warnings import warn

class Pageable:
    def __init__(self, page: int, per_page: int):
        self._page = page
        self._per_page = per_page

    def get_page(self):
        return self._page

    def get_per_page(self):
        return self._per_page

    def get_limit(self):
        return self._per_page

    def get_offset(self):
        return (self._page)*self._per_page


    def __str__(self):
        return str({
            "page": self._page,
            "per_page": self._per_page
        })
