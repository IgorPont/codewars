def square_digits(num):
    tmp = list(str(num))
    res = []
    for i in tmp:
        res.append(str(int(i) ** 2))
    return int("".join(res))

# def square_digits(num):
#     ret = ""
#     for x in str(num):
#         ret += str(int(x)**2)
#     return int(ret)


print(square_digits(9119))
