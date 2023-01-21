def move_zeros(data: list) -> list:
    size = len(data)
    left = right = 0
    while right < size:
        if data[right] == 0:
            right += 1
        else:
            data[left], data[right] = data[right], data[left]
            right += 1
            left += 1
    return data

'''
def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))
'''

print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))