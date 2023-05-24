def unique_in_order(sequence):
    if len(sequence) == 0:
        return []
    res = [sequence[0]]
    i = 0
    while i != len(sequence) - 1:
        if sequence[i] != sequence[i + 1]:
            res.append(sequence[i + 1])
        i += 1
    return res


# def unique_in_order(iterable):
#     result = []
#     prev = None
#     for char in iterable[0:]:
#         if char != prev:
#             result.append(char)
#             prev = char
#     return result


if __name__ == '__main__':
    print(unique_in_order(""))
