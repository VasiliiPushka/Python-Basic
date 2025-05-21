import os
from typing import Any


class File(object):
    def __init__(self, file_name: str, method: str) -> None:
        self.file_name = file_name
        self.method = method
        self.file_obj = None

    def __enter__(self) -> Any:
        try:
            self.file_obj = open(self.file_name, self.method)
        except:
            self.file_obj = open(self.file_name, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()
        return True


with File('1.txt', 'r') as test_file:
    pass
