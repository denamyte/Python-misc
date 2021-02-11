from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        """
        https://leetcode.com/problems/height-checker/
        """
        h = sorted(heights)
        moved = 0
        for i in range(len(heights)):
            if heights[i] != h[i]:
                moved += 1
        return moved


index = 0


def test(ar: List[int], expected_moves: int):
    moves = Solution().heightChecker(ar)
    global index
    index += 1
    print(f'''Test #{index}:
         array: {ar};
expected moves: {expected_moves};
  actual moves: {moves}.
''')


test([1, 1, 4, 2, 1, 3], 3)
test([5, 1, 2, 3, 4], 5)
test([1, 2, 3, 4, 5], 0)
