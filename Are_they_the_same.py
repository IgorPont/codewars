def comp(a1, a2):
    a3 = list(map(lambda x: x ** 0.5, a2))
    if len(set(a3) - set(a1)) == 0:
        return True
    else:
        return False


b1 = [121, 144, 19, 161, 19, 144, 19, 11]
b2 = [11 * 11, 121 * 121, 144 * 144, 190 * 190, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
print(comp(b1, b2))
