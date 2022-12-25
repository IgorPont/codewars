def format_duration(seconds):
    if seconds == 0:
        return "now"
    y = seconds // (3600*24*365)
    d = (seconds % (3600*24*365))//(3600*24)
    h = (seconds % (3600*24)) // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return readable([form(y, "year"), form(d, "day"), form(h, "hour"), form(m, "minute"), form(s, "second")])


def form(n, unit):
    if n == 0:
        return ""
    if n == 1:
        return "1 " + unit
    return str(n) + " " + unit + "s"


def readable(l):
    l = list(filter(None, l))
    result = ""
    if len(l) == 1:
        return l[0]
    for i in range(len(l)-1):
        result = result + ", " + l[i]
    result = result + " and " + l[len(l)-1]
    return result[2:]


print(format_duration(122))

# times = [("year", 365 * 24 * 60 * 60),
#          ("day", 24 * 60 * 60),
#          ("hour", 60 * 60),
#          ("minute", 60),
#          ("second", 1)]

# def format_duration(seconds):

#     if not seconds:
#         return "now"

#     chunks = []
#     for name, secs in times:
#         qty = seconds // secs
#         if qty:
#             if qty > 1:
#                 name += "s"
#             chunks.append(str(qty) + " " + name)

#         seconds = seconds % secs

#     return ', '.join(chunks[:-1]) + ' and ' + chunks[-1] if len(chunks) > 1 else chunks[0]

# year = 31536000
# day = 86400
# hour = 3600
# minute = 60
# second = 1
