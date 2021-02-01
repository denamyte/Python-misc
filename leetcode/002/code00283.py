from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        put_ind, zeroes = 0, 0
        while put_ind < size and nums[put_ind]:  # find first zero in nums
            put_ind += 1
        while put_ind + zeroes < size:
            if nums[put_ind + zeroes] == 0:
                zeroes += 1
            else:
                nums[put_ind], nums[put_ind + zeroes] = nums[put_ind + zeroes], 0
                put_ind += 1

    def moveZeroes2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        put_ind = 0
        for take_ind in range(len(nums)):
            if nums[take_ind]:
                nums[put_ind], nums[take_ind] = nums[take_ind], nums[put_ind]
                put_ind += 1


test_i = 0


def test(arr: List[int], res_arr: List[int]):
    global test_i
    test_i += 1
    arr_copy = arr[:]
    Solution().moveZeroes2(arr)
    print(f'''Test #{test_i}:   
initial array: {arr_copy};
 result array: {arr};
result is correct: {arr == res_arr}
''')


test([0, 1, 0, 3, 12], [1, 3, 12, 0, 0])
test([0], [0])
test([1, 2, 3], [1, 2, 3])
test([0, 0, 0, 1], [1, 0, 0, 0])
test([0, 1], [1, 0])
