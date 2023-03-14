
from typing import List


def parser(file: str) -> List[List[str]]:
    with open(file, "r") as f:
        lists_of_str = [(line.strip()).split() for line in f]
        f.close()
        return lists_of_str
