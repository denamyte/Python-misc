import math
from typing import List


def sortedSquares(nums: List[int]) -> List[int]:
    pass
    # todo: Start from both sides of the array and move to the smallest abs(nums[i]) in the center;
    #  always take the biggest square and reduce the index of the side, where the square was taken;
    #  append the squares taken to a new array;
    #  reverse the resulting array

nums = [-20, -18, -16, -13, -10, -5, -4, -3, -1, 0, 3, 6, 10, 12, 15, 17, 18, 20]
print(sortedSquares(nums))
