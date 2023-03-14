from __future__ import print_function

import sys

# Return expected key presses for a multi-press keypad
#
# https://en.wikipedia.org/wiki/Telephone_keypad#/media/File:Telephone-keypad2.svg
#
#   -------------------------
#   |       |  ABC  |  DEF  |
#   |   1   |   2   |   3   |
#   -------------------------
#   |  GHI  |  JKL  |  MNO  |
#   |   4   |   5   |   6   |
#   -------------------------
#   | PQRS  |  TUV  | WXYZ  |
#   |   7   |   8   |   9   |
#   -------------------------
#   |       |       |       |
#   |   *   |   0   |   #   |
#   -------------------------
#
# For a user to input a word into the STB, they must press a sequence of keys.
#
#   a -> 2
#   b -> 22
#   go -> 4666
#
# In order to insert two characters in sequence from the same key, the user
# must pause before pressing the key a second time. The space character ' '
# indicates this.
#
#   a -> 2
#   aa -> 2 2
#   ab -> 2 22
#
#   go -> 4666
#   no -> 66 666
#
# Question:
#
#   Given a string to input, calculate the keys to be pressed.
#
# Test cases are included.  Run all test cases as:
#
#   python keys.py
#
# or particular example as:
#
#   python keys.py <word>

digit_keys = {
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz",
    0: " ",
}

text = "Hello"


def keys_to_press(text: str):
    output = ""
    last_key = None
    for i in text:
        for k, v in digit_keys.items():
            if i in v:
                if last_key is not None and last_key == k:
                    output += " "
                p = list(v).index(i)
                for n in range(0, p + 1):
                    output += str(k)
                last_key = k

    return output


TESTS = {
    "go": "4666",
    "go go": "466604666",
    "no": "66 666",
    "yes": "999337777",
    "hi": "44 444",
    "hello world": "4433555 555666096667775553",
    "youview": "99966688 888444339",
    " ": "0",
    "  ": "0 0",
    "   ": "0 0 0",
    "a a a ": "202020",
    " a a a": "020202",
    "a  a  a": "20 020 02",
    "a  bb  ccc": "20 022 220 0222 222 222",
}


def run_test(input_text):
    """Test harness for `keys_to_press`.

    :param input_text str: Input to function
    """
    expected_output = TESTS.get(input_text)
    print('Input :          "{}"'.format(input_text))
    print('Expected Output: "{}"'.format(expected_output))
    output = keys_to_press(input_text)
    print('Output:          "{}"'.format(output))
    passed = output == expected_output
    if passed:
        print("PASS")
    else:
        print("!!! ERROR")
    return passed


if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_test(sys.argv[1])
    else:
        passed_count = 0
        for input_text in TESTS:
            print("=" * 10)
            if run_test(input_text):
                passed_count += 1
        print("{} of {} tests passed".format(passed_count, len(TESTS)))