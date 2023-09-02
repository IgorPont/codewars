def flatten_and_sort(array):
    res = []
    for i in array:
        for j in i:
            if len(i) > 0:
                res.append(j)
    res.sort()
    return res

# def flatten_and_sort(array):
#     return sorted([j for i in array for j in i])


print(flatten_and_sort([[3, 2, 1], [7, 9, 8], [6, 4, 5]]))
