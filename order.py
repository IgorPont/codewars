# def order(text):
#     lst = text.split()
#     res = list(range(len(lst)))
#     for i in lst:
#         for j in i:
#             if j.isdigit() and int(j) == 1:
#                 res[0] = i
#             elif j.isdigit() and int(j) == 2:
#                 res[1] = i
#             elif j.isdigit() and int(j) == 3:
#                 res[2] = i
#             elif j.isdigit() and int(j) == 4:
#                 res[3] = i
#             elif j.isdigit() and int(j) == 5:
#                 res[4] = i
#             elif j.isdigit() and int(j) == 6:
#                 res[5] = i
#             elif j.isdigit() and int(j) == 7:
#                 res[6] = i
#             elif j.isdigit() and int(j) == 8:
#                 res[7] = i
#             elif j.isdigit() and int(j) == 9:
#                 res[8] = i
#     return res

def order(text):
    return ' '.join(sorted(text.split(), key=lambda w: sorted(w)))


print(order('4of Fo1r pe6ople g3ood th5e the2'))
