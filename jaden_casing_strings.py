def to_jaden_case(string):
    res = ' '.join(map(lambda word: word.capitalize(), string.split()))

    return res

# def to_jaden_case(string):
#     list = string.split()
#     new_list = [i.capitalize() for i in list]
#     return ' '.join(new_list)


print(to_jaden_case("How can mirrors be real if our eyes aren't real"))
