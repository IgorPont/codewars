def get_age(age):
    x, *_ = age.split()
    return int(x)


# def get_age(age):
#     return int(age[0])


print(get_age("2 years old"))
