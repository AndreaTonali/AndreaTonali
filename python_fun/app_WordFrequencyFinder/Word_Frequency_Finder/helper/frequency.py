from itertools import chain
from collections import Counter
from typing import Dict, List


def frequency(lists_of_str: List[List[str]]) -> Dict:
    return dict(Counter(chain.from_iterable(lists_of_str)))
