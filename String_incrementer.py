def increment_string(s):
    tmp = list(s)
    sum = ''
    for i in tmp[::-1]:
        if i.isdigit():
            sum += i
        else:
            res = "".join(tmp[:tmp.index(i) + 1])
            break
    if not sum:
        return s + '1'
    else:
        rev = sum[::-1]
        return res + str(int(rev) + 1).zfill(len(rev))


# def increment_string(strng):
#     head = strng.rstrip('0123456789')
#     tail = strng[len(head):]
#     if tail == "": return strng + "1"
#     return head + str(int(tail) + 1).zfill(len(tail))


print(increment_string("foobar001"))
