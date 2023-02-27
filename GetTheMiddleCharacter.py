def get_middle(s):
    if len(s) % 2 == 0:
        return s[len(s) // 2 - 1] + s[len(s) // 2]
    else:
        return s[len(s) // 2]

# def get_middle(s):
#     while len(s) > 2:
#         s = s[1:-1]
#     return s


print(get_middle("testing"))
