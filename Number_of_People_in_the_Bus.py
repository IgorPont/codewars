def number(bus_stops):
    return sum(i[0] - i[1] for i in bus_stops)


num = [[3, 0], [9, 1], [4, 10], [12, 2], [6, 1], [7, 10]]
print(number(num))
