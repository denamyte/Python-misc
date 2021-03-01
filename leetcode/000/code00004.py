import math
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        https://leetcode.com/problems/median-of-two-sorted-arrays/
        :param nums1: A sorted array
        :param nums2: Another sorted array
        :return: The median of the two sorted arrays
        """
        a_len, b_len = sorted([len(nums1), len(nums2)])
        a, b = (nums1, nums2) if len(nums1) == a_len else (nums2, nums1)
        left_half_len: int = (a_len + b_len + 1) // 2

        a_min_count = 0
        a_max_count = a_len
        while a_min_count <= a_max_count:
            a_count = a_min_count + ((a_max_count - a_min_count) // 2)
            b_count = left_half_len - a_count

            if a_count > 0 and a[a_count - 1] > b[b_count]:
                a_max_count = a_count - 1
            elif a_count < a_len and b[b_count - 1] > a[a_count]:
                a_min_count = a_count + 1
            else:
                left_half_end = b[b_count - 1] if a_count == 0\
                    else a[a_count - 1] if b_count == 0\
                    else max(a[a_count - 1], b[b_count - 1])

                if (a_len + b_len) & 1:
                    return left_half_end

                right_half_start = b[b_count] if a_count == a_len\
                    else a[a_count] if b_count == b_len\
                    else min(a[a_count], b[b_count])

                return (left_half_end + right_half_start) / 2


index = 0


def test(nums1: List[int], nums2: List[int], exp_median: float):
    global index
    index += 1
    median = Solution().findMedianSortedArrays(nums1, nums2)
    print(f'''Test #{index}
        nums1: {nums1};
        nums2: {nums2};
       merged: {sorted([*nums1, *nums2])};
 found median: {median};
medians equal: {median == exp_median}
''')


test([1, 3], [2], 2)
test([1, 2], [3, 4], 2.5)
test([0, 0], [0, 0], 0)
test([], [1], 1)
test([2], [], 2)
