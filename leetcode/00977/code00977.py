from typing import List


def sortedSquares(nums: List[int]) -> List[int]:
    # Start from both sides of the array and move to the smallest abs(nums[i]) in the center;
    #  always take the biggest square and reduce the index of the side, where the square was taken;
    #  append the squares taken to a new array;
    #  reverse the resulting array
    res: List[int] = []
    cur_ind: List[int] = [0, len(nums) - 1]
    squares: List[int] = [pow(nums[cur_ind[0]], 2), pow(nums[cur_ind[1]], 2)]
    incr: List[int] = [1, -1]

    while cur_ind[0] <= cur_ind[1]:
        index = 0 if squares[0] > squares[1] else 1
        res.append(squares[index])
        cur_ind[index] += incr[index]
        squares[index] = pow(nums[cur_ind[index]], 2)

    cur_ind[0], cur_ind[1] = 0, len(nums) - 1
    while cur_ind[0] <= cur_ind[1]:
        temp = res[cur_ind[0]]
        res[cur_ind[0]] = res[cur_ind[1]]
        res[cur_ind[1]] = temp
        cur_ind[0] += 1
        cur_ind[1] -= 1

    return res


def sortedSquares_2(nums: List[int]) -> List[int]:
    size = len(nums)
    res = [0] * size
    cur_ind: List[int] = [0, size - 1]
    squares: List[int] = [pow(nums[cur_ind[0]], 2), pow(nums[cur_ind[1]], 2)]
    incr: List[int] = [1, -1]
    while size > 0:
        size -= 1
        index = 0 if squares[0] > squares[1] else 1
        res[size] = squares[index]
        cur_ind[index] += incr[index]
        squares[index] = pow(nums[cur_ind[index]], 2)
    return res


def sortedSquares_3(nums: List[int]) -> List[int]:
    res = []
    for x in nums:
        res.append(x ** 2)
    return sorted(res)


def sortedSquares_4(nums: List[int]) -> List[int]:
    return sorted(map(lambda v: v ** 2, nums))


test = [-20, -18, -16, -13, -10, -5, -4, -3, -1, 0, 3, 6, 10, 12, 15, 17, 18, 20]
print(sortedSquares_4(test))
