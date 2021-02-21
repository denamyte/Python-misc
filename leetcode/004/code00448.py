from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
        """
        for i in range(len(nums)):
            while nums[i] != i + 1 and nums[nums[i] - 1] != nums[i]:
                n_i, n_n_i = nums[i], nums[nums[i] - 1]
                nums[i], nums[n_i - 1] = n_n_i, n_i
        res = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                res.append(i + 1)
        return res


index = 0


def test(ar: List[int], exp_res: List[int]):
    global index
    index += 1
    initial_ar = ar[:]
    actual_res = Solution().findDisappearedNumbers(ar)
    sorted_ar = ar
    print(f'''Test #{index}:
  initial array: {initial_ar};
   sorted array: {sorted_ar};
expected result: {exp_res};
  results match: {exp_res == actual_res}
''')


test([4, 3, 2, 7, 8, 2, 3, 1], [5, 6])
test([1, 1], [2])
test([1], [])
test([3, 3, 3], [1, 2])
