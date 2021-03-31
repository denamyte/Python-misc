recursive_count = 0


def quick_sort(lst, start, end):
    if start >= end:
        return

    j = partition(lst, start, end)
    quick_sort(lst, start, j - 1)
    quick_sort(lst, j + 1, end)

    global recursive_count
    recursive_count += 2


def partition(lst, start, end):
    j = start

    for i in range(start + 1, end + 1):
        if lst[i] <= lst[start]:
            j += 1
            lst[i], lst[j] = lst[j], lst[i]

    lst[start], lst[j] = lst[j], lst[start]
    return j


lst = [6, 2, 1, 5, 1, 0]
quick_sort(lst, 0, len(lst) - 1)
print(recursive_count)
