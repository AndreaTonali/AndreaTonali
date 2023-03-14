"""
Write a function that returns the elements on odd positions (0 based) in a list
"""

def solution(input: list):
    output = input[1::2]
    return output


assert solution([0, 1, 2, 3, 4, 5]) == [1, 3, 5]
assert solution([1, -1, 2, -2]) == [-1, -2]

"""
Write a function that returns the cumulative sum of elements in a list
"""

def solution(input: list):
    from itertools import accumulate
    output = list(accumulate(input))
    return output


assert solution([1, 1, 1]) == [1, 2, 3]
assert solution([1, -1, 3]) == [1, 0, 3]

"""
Write a function that takes a number and returns a list of its digits
"""

def solution(input: int):
    output = [int(x) for x in str(input)]
    return output


assert solution(123) == [1, 2, 3]
assert solution(400) == [4, 0, 0]

"""
From: http://codingbat.com/prob/p126968
Return the "centered" average of an array of ints, which we'll say is 
the mean average of the values, except ignoring the largest and 
smallest values in the array. If there are multiple copies of the 
smallest value, ignore just one copy, and likewise for the largest 
value. Use int division to produce the final average. You may assume 
that the array is length 3 or more.
"""

def solution(input: list):

    input.pop(input.index(max(input)))
    input.pop(input.index(min(input)))

    output = round(sum(input)/len(input))

    return output


assert solution([1, 2, 3, 4, 100]) == 3
assert solution([1, 1, 5, 5, 10, 8, 7]) == 5
assert solution([-10, -4, -2, -4, -2, 0]) == -3
