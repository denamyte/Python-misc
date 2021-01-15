from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        https://leetcode.com/problems/merge-sorted-array/
        Do not return anything, modify nums1 in-place instead.
        """
        # todo: read from both arrays their last numbers and insert them into the end of the nums1
        #  filling nums1 from the end to the start
        while m + n > 0:
            take_left = (m > 0 and n > 0 and nums1[m - 1] > nums2[n - 1]) or (m > 0 and n == 0)
            if take_left:
                m -= 1
                nums1[m + n] = nums1[m]
            else:
                n -= 1
                nums1[m + n] = nums2[n]


# nums1 = [1, 2, 3, 0, 0, 0]
# m = 3
# nums2 = [2, 5, 6]
# n = 3
# Solution().merge(nums1, m, nums2, n)
# print(nums1)

nums1 = [1, 2, 6, 8, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
m = 5
nums2 = [1, 3, 4, 4, 5, 7, 8, 9, 9, 9]
n = 10
Solution().merge(nums1, m, nums2, n)
print(nums1)
