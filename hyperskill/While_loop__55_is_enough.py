nums = []
n = input()

while n != '55':
    nums.append(n)
    n = input()

length = len(nums)
sum_ = sum(list(map(int, nums)))
print(length, sum_, round(sum_ / length), sep='\n')
