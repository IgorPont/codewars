# Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.


integers = dict(I=1, IV=4, V=5, X=10, L=50, C=100, D=500, M=1000)


def to_roman(arabic):
    romans = list(integers)
    str_arabic = arabic[::-1]
    str_arabic_len = len(str_arabic)
    result = str()
    romans_pointer = 0
    for i in range(str_arabic_len):
        if str_arabic[i] in ['0', '1', '2', '3']:
            result = romans[romans_pointer] * int(str_arabic[i]) + result
        elif str_arabic[i] in ['4']:
            result = romans[romans_pointer] + \
                romans[romans_pointer + 1] + result
        elif str_arabic[i] in ['5', '6', '7', '8']:
            result = romans[romans_pointer + 1] + \
                romans[romans_pointer] * (int(str_arabic[i]) - 5) + result
        elif str_arabic[i] in ['9']:
            result = romans[romans_pointer] + \
                romans[romans_pointer + 2] + result
        romans_pointer += 2
    return result


def from_roman(roman):
    result = 0
    for i, c in enumerate(roman):
        if i+1 < len(roman) and integers[roman[i]] < integers[roman[i+1]]:
            result -= integers[roman[i]]
        else:
            result += integers[roman[i]]
    return str(result)


print(to_roman('12'))
