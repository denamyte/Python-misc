from typing import List
from random import shuffle


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max_ar = [nums[0]]
        for v in nums[1:]:
            if v not in max_ar and (v > max_ar[-1] or len(max_ar) < 3):
                max_ar.append(v)
                max_ar.sort(reverse=True)
                max_ar = max_ar[:3]
        return max_ar[0] if len(max_ar) < 3 else max_ar[2]


# ar = []
# print(ar)
# ar = [3, *ar[:3]]
# print(ar)

index = 0


def test(nums: List[int], expected_answer: int):
    global index
    index += 1
    result = Solution().thirdMax(nums)
    print(f'''Test #{index}:
    input array: {nums};
expected answer: {expected_answer};
  actual answer: {result};
 result matches: {expected_answer == result}
''')


test([3, 2, 1], 1)
test([1, 2], 2)
test([2, 2, 3, 1], 1)

complex_shuffled = ([1, 2, 3, 4, 5, 6] * 4)
shuffle(complex_shuffled)
test(complex_shuffled, 4)
