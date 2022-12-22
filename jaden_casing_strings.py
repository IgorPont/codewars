def to_jaden_case(string):
    res = ' '.join(map(lambda word: word.capitalize(), string.split()))

    return res


print(to_jaden_case("How can mirrors be real if our eyes aren't real"))
