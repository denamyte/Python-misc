import math
from typing import List


class Solution:
    def __init__(self):
        self.lengths: List[int] = [0]  # contains the arrays lengths
        self.arrays: List[List[int]] = []  # both arrays are put here, if the arrays have
        self.search_ind_ranges: List[List[int]] = []  # the index ranges in the arrays where the median can be found
        # different length, the shorter one should come first

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        https://leetcode.com/problems/median-of-two-sorted-arrays/
        :param nums1: A sorted array
        :param nums2: A sorted array
        :return: The median of the two sorted arrays
        """

        if len(nums1) == 0:
            # Find out the median from the nums2 array
            pass
        elif len(nums2) == 0:
            # Find out the median from the nums1 array
            pass

    def prepare_arrays(self, nums1: List[int], nums2: List[int]):
        self.lengths = sorted([len(nums1), len(nums2)])
        self.arrays = [nums1, nums2] if len(nums1) == self.lengths[0] else [nums2, nums1]
        median_ind = math.ceil(sum(self.lengths) / 2)
        self.search_ind_ranges = [[0, self.lengths[0] - 1], [median_ind - self.lengths[0] + 1, median_ind]]

    def binary_search_for_median_indices(self):
            pass
