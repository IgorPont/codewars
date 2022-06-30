def narcissistic(num):
    n = str(num)
    res = 0
    len_n = len(n)
    for char in n:
        res += pow(int(char), len_n)
    print(res)
    if res == num:
        return True
    else:
        return False


print(narcissistic(371))
