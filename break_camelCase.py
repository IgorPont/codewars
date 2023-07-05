def solution(s):
    res = ''
    temp = 0
    for i in s:
        if i.isupper():
            res += f' {i}'
        else:
            res += i
    return res

# def solution(s):
#     return ''.join(' ' + c if c.isupper() else c for c in s)


s = 'helloWorld'
print(solution(s))
