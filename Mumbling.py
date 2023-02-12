def accum(s):
    tmp = []
    res = []
    for i in s:
        tmp.append(i)
    for i, item in enumerate(tmp):
        res.append((item * (i + 1)).capitalize())
    return "-".join(res)


# def accum(s):
#     return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))

print(accum('abcd'))
