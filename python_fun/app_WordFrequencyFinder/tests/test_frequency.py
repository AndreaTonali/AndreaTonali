from typing import Dict
from Word_Frequency_Finder.helper import frequency

EXPECTED_RESULT = {

    'badger': 5,
    'mushroom': 2,
    'snake': 1,
    'xyz': 5,
    'xzy': 1,
    'yxz': 2

}


def test_frequency(data_sample):
    data = frequency(data_sample)
    
    assert type(data) == dict
    assert data == EXPECTED_RESULT
