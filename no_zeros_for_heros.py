def no_boring_zeros(n):
    invert = str(n)[::-1]
    temp = 0
    for i in invert:
        if i == '0':
            continue
        else:
            temp = invert.index(i)
            break
    res = invert[temp:][::-1]
    if res[0] == '-':
        return int(res[1:]) * -1
    return int(res)


# def no_boring_zeros(n):
#     try:
#         return int(str(n).rstrip('0'))
#     except ValueError:
#         return 0


if __name__ == '__main__':
    print(no_boring_zeros(960000))
