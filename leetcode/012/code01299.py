from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
        https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
        """
        max_el, last_el = -1, -1
        for i in range(len(arr) - 1, -1, -1):
            max_el = max(max_el, last_el)
            last_el = arr[i]
            arr[i] = max_el
        return arr


test_i = 0


def test(arr: List[int], expected_arr: List[int]):
    global test_i
    test_i += 1
    ini_arr = arr[:]
    Solution().replaceElements(arr)
    print(f'''
==== Test #{test_i} ====
Array before: {ini_arr};
 Array after: {arr}
 Array match: {arr == expected_arr}''')


test([17, 18, 5, 4, 6, 1], [18, 6, 6, 6, 1, -1])
test([400], [-1])
test([5, 4, 3, 2, 1, 0], [4, 3, 2, 1, 0, -1])
test([18, 20, 15, 0, 7, 6, 10, 2, 3, 4, 2, 5, 1, 1], [20, 15, 10, 10, 10, 10, 5, 5, 5, 5, 5, 1, 1, -1])
