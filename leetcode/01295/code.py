from typing import List
# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

def find_numbers(nums: List[int]) -> int:
    count = 0
    for num in nums:
        digits = 0
        while num > 0:
            num //= 10
            digits += 1
        if digits % 2 == 0:
            count += 1
    return count


def find_numbers_2(nums: List[int]) -> int:
    odds = 0
    for num in nums:
        odds += len(str(num)) % 2
    return len(nums) - odds


print(find_numbers_2([1, 2, 333, 45655, 223, 5]))
print(find_numbers_2([12, 2, 3334, 45655, 22, 5]))
