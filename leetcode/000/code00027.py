from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        https://leetcode.com/problems/remove-element/
        """
        if val > 50:
            return len(nums)
        length = len(nums)
        start_index, end_index = 0, len(nums) - 1,
        while start_index <= end_index:
            # find the next val index increasing start_index until it reaches end_index
            while start_index <= end_index and start_index < length and nums[start_index] != val:
                start_index += 1
            # find the previous non-val index
            while end_index >= 0 and nums[end_index] == val:
                end_index -= 1
                length -= 1
            if start_index < end_index:
                nums[start_index] = nums[end_index]
                end_index -= 1
                length -= 1
        return length

    def removeElement2(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[i], nums[index] = nums[index], nums[i]
                index += 1
        return index


def test(solution: Solution, arr: List[int], value: int, exp_arr: List[int], exp_length: int):
    start_array = arr[:]
    actual_length = solution.removeElement(arr, value)
    print(f'''
======================================
Test: removeElement ==================
    start array: {start_array}
  value to find: {value} 
 expected array: {exp_arr}
   actual array: {arr[:actual_length]}
expected length: {exp_length}
  actual length: {exp_length}''')


sol = Solution()
test(sol, [3, 2, 2, 3], 3, [2, 2], 2)

test(sol, [0, 1, 2, 2, 3, 0, 4, 2], 2, [0, 1, 4, 0, 3], 5)

test(sol, [], 10, [], 0)

test(sol, [1], 1, [], 0)
