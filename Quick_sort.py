# Быстрая сортировка
def quicksort(arr, start, end):
    if end - start > 1:
        p = partition(arr, start, end)
        quicksort(arr, start, p)
        quicksort(arr, p + 1, end)


def partition(alist, start, end):
    pivot = alist[start]
    i = start + 1
    j = end - 1

    while True:
        while (i <= j and alist[i] <= pivot):
            i = i + 1
        while (i <= j and alist[j] >= pivot):
            j = j - 1

        if i <= j:
            alist[i], alist[j] = alist[j], alist[i]
        else:
            alist[start], alist[j] = alist[j], alist[start]
            return j


arr = [9, 3, 6, 1, 2, 4, 0, 8, 7, 5]
quicksort(arr, 0, len(arr))
print(arr)
