from typing import List


class Solution:
    # noinspection PyPep8Naming
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        """
        Sorting in place
        """
        even_i, odd_i = 0, len(A) - 1,
        while even_i < odd_i:
            if A[even_i] % 2:
                A[even_i], A[odd_i] = A[odd_i], A[even_i]
                odd_i -= 1
            else:
                even_i += 1
        return A

    def sortArrayByParity2(self, A: List[int]) -> List[int]:
        """
        Returning a new array with sorted values
        """
        res = [0] * len(A)
        even_i, odd_i = 0, -1
        for v in A:
            if v % 2:
                res[odd_i] = v
                odd_i -= 1
            else:
                res[even_i] = v
                even_i += 1
        return res


test_i = 0


def test(ar: List[int]):
    global test_i
    test_i += 1
    res = Solution().sortArrayByParity2(ar)
    print(f'''Test #{test_i}:
initial array: {ar};
 sorted array: {res}
 ''')


test([3, 1, 2, 4])
test([2, 0, 4, 1, 1, 1, 10])
test([2])
test([1])
