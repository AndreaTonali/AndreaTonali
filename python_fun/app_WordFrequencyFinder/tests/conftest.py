import pytest
from Word_Frequency_Finder.helper.file_parser import parser

TEXT_FILE="./tests/test_words.txt"

@pytest.fixture(scope='module')
def data_sample():
    data = parser(TEXT_FILE)
    return data