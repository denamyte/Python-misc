from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        """
        https://leetcode.com/problems/check-if-n-and-its-double-exist/
        Given an array arr of integers, check if there exists
        two integers N and M such that N is the double of M ( i.e. N = 2 * M).

        2 <= arr.length <= 500
        -10^3 <= arr[i] <= 10^3

        todo: Maybe sort first and then binary search?
        """
        arr.sort()
        length = len(arr)
        for i in range(length):
            value = arr[i] * 2
            if value == 0:
                if i + 1 < length and arr[i + 1] == 0:
                    return True
                continue
            if abs(value) > 1000 or value < arr[0] or value > arr[length - 1]:
                continue
            if (value < 0 and self.binary_search(arr, value, 0, i - 1) >= 0) \
                    or self.binary_search(arr, value, i + 1, length - 1) >= 0:
                return True
        return False

    def binary_search(self, arr: List[int], value: int, left: int, right: int) -> int:
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == value:
                return mid
            if value < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1


def test(index: int, arr: List[int], expected_output: bool):
    print(f'''Test #{index}:
array: {arr};
expected output: {expected_output};
actual output:   {Solution().checkIfExist(arr)}''')


# test(1, [10, 2, 5, 3], True)
# test(2, [7, 1, 14, 11], True)
# test(3, [3, 1, 7, 11], False)
# test(4, [-7, -14, -16, 16, 17, 3, 5, 19, -13, -23, -21, 21, 23], True)
test(5, [-2, 0, 10, -19, 4, 6, -8], False)
test(6, [-2, 0, 10, 0, 0, 6, -8], True)
