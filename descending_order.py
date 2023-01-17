def descending_order(num):
    l_num = list(str(num))
    l_num.sort(reverse=True)
    return int(''.join(l_num))


print(descending_order(12345))
