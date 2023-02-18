def find_uniq(arr):
    tmp = sorted(arr)
    if tmp[0] < tmp[1]:
        return tmp[0]
    else:
        return tmp[len(tmp) - 1]


print(find_uniq([1, 1, 1, 2, 1, 1]))
