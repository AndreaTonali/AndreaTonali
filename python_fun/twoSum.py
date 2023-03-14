from typing import List, Tuple


def two_sum(nums: List[int], target: int) -> Tuple[int, int]:
    """
    Given an array of integers nums and an integer target, return indices
    of the two numbers such that they add up to target.
    :param nums: List of integers
    :param target: int
    :return: two int
    """
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                return i, j

