def delete_nth(order, max_e):
    new_order = []

    for n in order:
        if new_order.count(n) >= max_e:
            continue
        else:
            new_order.append(n)
    return new_order

'''
def delete_nth(order,max_e):
    answer = []
    for x in order:
        if answer.count(x) < max_e:
            answer.append(x) 
    return answer
'''

'''
def delete_nth(order,max_e):
    return [o for i,o in enumerate(order) if order[:i].count(o)<max_e]
'''

print(delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3))
