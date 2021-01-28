from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        """
        https://leetcode.com/problems/valid-mountain-array/
        """
        index = 0
        last_index = len(arr) - 1
        uphill = True
        while index < last_index:
            index += 1
            if arr[index - 1] == arr[index]:
                return False
            if uphill:
                if arr[index - 1] > arr[index]:
                    if index == 1:
                        return False
                    uphill = False
            elif arr[index - 1] < arr[index]:
                return False
        return not uphill and len(arr) >= 3


test_number = 0


def test(arr: List[int], expected: bool):
    global test_number
    test_number += 1
    actual = Solution().validMountainArray(arr)
    if actual != expected:
        raise RuntimeError(f"Test #{test_number} failed")
    print(f'''
Test #{test_number}
Array: {arr};
Result: {expected}.''')


test([2, 1], False)
test([3, 5, 5], False)
test([0, 3, 2, 1], True)
test([3, 5, 0], True)
test([3, 5, 6, 7, 8, 12, 15, 14, 13, 10, 5, 4], True)
test([3, 5, 5, 7, 8, 12, 15, 14, 13, 10, 5, 4], False)
test([3, 5, 6, 7, 8, 12, 15, 14, 10, 10, 5, 4], False)
test([3, 5, 6, 7, 8, 12, 14, 14, 13, 10, 5, 4], False)
test([3, 5, 0, 7, 8, 12, 15, 14, 13, 10, 5, 4], False)
test([3, 5, 6, 7, 8, 12, 15, 14, 13, 10, 11, 4], False)
