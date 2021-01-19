from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Given a sorted array, remove the duplicates in-place, return the new length of the array.
        https://leetcode.com/problems/remove-duplicates-from-sorted-array
        """
        put_ind, take_ind = 0, 1
        while take_ind < len(nums):
            if nums[put_ind] != nums[take_ind]:
                put_ind += 1
                nums[put_ind] = nums[take_ind]
            take_ind += 1
        return len(nums) and put_ind + 1


def test(test_num: int, nums: List[int], expected_length: int, expected_nums: List[int]):
    actual_nums = nums[:]
    actual_length = Solution().removeDuplicates(actual_nums)
    print(f'Test #{test_num}: lengths are equal: {expected_length == actual_length};'
          f' arrays are equal: {expected_nums == actual_nums[:actual_length]}')


test(1, [1, 1, 2],
     2, [1, 2])

test(2, [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
     5, [0, 1, 2, 3, 4])

test(3, [5, 5, 5, 5, 5],
     1, [5])

test(4, [0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 9],
     3, [0, 5, 9])

test(5, [],
     0, [])

test(6, [0],
     1, [0])

