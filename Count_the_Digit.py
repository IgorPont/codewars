def nb_dig(n, d):
    temp_l = []
    for i in range(n + 1):
        temp_l.append(i)
    k = list(map(lambda i: i ** 2, temp_l))
    count = 0
    for i in k:
        tmp = str(i).count(str(d))
        count += tmp
    return count


# def nb_dig(n, d):
#     return sum(str(i * i).count(str(d)) for i in range(n + 1))


print(nb_dig(25, 1))
