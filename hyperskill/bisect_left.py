from bisect import bisect_left

ar = list(range(10))
print(ar)

bisect1 = bisect_left(ar, 1)
print(f'bisect(1) == {bisect1}')

bisect5 = bisect_left(ar, 5)
print(f'bisect(5) == {bisect5}')

bisect_m1 = bisect_left(ar, -1)
print(f'bisect(-1) == {bisect_m1}')

bisect11 = bisect_left(ar, 11)
print(f'bisect(11) == {bisect11}')
