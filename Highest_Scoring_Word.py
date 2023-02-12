import string


def high(x):
    alph = string.ascii_lowercase
    high_total = 0
    str_high = ''

    for word in x.split():
        total = 0
        for pos in word:
            if pos in alph:
                total += ord(pos) - 96
        if total > high_total:
            high_total = total
            str_high = word
        elif total == high_total:
            continue

    return str_high


# def high(x):
#     return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))

print(high('man i need a taxi up to ubud'))
