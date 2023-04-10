def diamond(n):
    if n % 2 == 0 or n < 0:
        return None
    else:
        res = ''
        j = n // 2
        for i in range(1, n + 1, 2):
            res += f"{j * ' ' + i * '*'}\n"
            j -= 1
        j = 0
        for i in range(n - 2, 0, -2):
            j += 1
            res += f"{j * ' ' + i * '*'}\n"

        return res


print(diamond(15))
