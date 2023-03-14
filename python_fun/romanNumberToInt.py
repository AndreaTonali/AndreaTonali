"""
Roman numerals are a numeral system that originated in ancient Rome and remained the usual
way of writing numbers throughout Europe well into the Late Middle Ages.
Roman numerals are based on seven symbols:

Symbol,Value
I,1
V,5
X,10
L,50
C,100
D,500
M,1000

The most basic rule is that you add the value of all the symbols: so II is 2, LXVI is 66, etc.
The exception is that there may not be more than three of the same characters in a row. Instead, you switch to subtraction.
So instead of writing IIII for 4, you write IV (for 5 minus 1); and instead of writing LXXXX for 90, you write XC.

Examples:
2018 = MMXVIII
1999 = MCMXCIX

Write a python function (with your IDE of choice), that takes as input a string representing a Roman numeral
and returns an integer representing the equivalent decimal number.
You can assume that the string given as input is a correctly formatted Roman numeral.
"""

import pytest

MAPPER = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

TEST = "MCMXCIX"


def roman_numerals_converter(num: str = TEST) -> int:
    roman_numer = 0
    for i in range(len(num)):
        value = MAPPER[num[i]]
        if i + 1 < len(num) and MAPPER[num[i + 1]] > value:
            roman_numer -= value
        else:
            roman_numer += value
    return roman_numer


@pytest.mark.parametrize("arg", [{"MCMXCIX": 1999, "MCMXCV": 1995, "MCMXCIV": 1994}])
def test_roman_numerals_converter(arg):
    
    assert arg["MCMXCIX"] == roman_numerals_converter("MCMXCIX")
    assert arg["MCMXCV"] == roman_numerals_converter("MCMXCV")
    assert arg["MCMXCIV"] == roman_numerals_converter("MCMXCIV")
