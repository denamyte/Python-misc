def selection_sort(ar):
    length = len(ar)
    count = 0
    for i in range(length - 1):
        index = i

        for j in range(i + 1, length):
            if ar[j] < ar[index]:
                count += 1
                index = j

        ar[i], ar[index] = ar[index], ar[i]

    return count


ar = [3, 1, 2, 2, 4, 5]
count = selection_sort(ar)
print(ar)
print(count)
