from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        https://leetcode.com/problems/duplicate-zeros/
        """
        copy = arr.copy()
        arr.clear()
        length = len(copy)
        for v in copy:
            if length == 0:
                break
            arr.append(v)
            length -= 1
            if v == 0 and length > 0:
                arr.append(0)
                length -= 1


arr = [1, 0, 2, 1, 0, 0, 2, 1, 2, 0, 0, 0, 1, 2, 1, 2, 1, 2]
print(arr)
print(len(arr))
Solution().duplicateZeros(arr)
print(arr)
print(len(arr))
