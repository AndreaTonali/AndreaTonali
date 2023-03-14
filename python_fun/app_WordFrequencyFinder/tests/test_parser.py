from typing import List
from Word_Frequency_Finder.helper import parser

TEXT_FILE = "./tests/test_words.txt"

EXPECTED_DATA = [
    ['badger', 'badger',  'mushroom',  'mushroom',  'snake',  'badger',  'badger',  'badger'],
    ['xyz', 'xyz', 'yxz', 'yxz', 'xzy', 'xyz', 'xyz', 'xyz']
]


def test_parser():
    data = parser(TEXT_FILE)

    assert type(data) == list 
    assert data == EXPECTED_DATA
