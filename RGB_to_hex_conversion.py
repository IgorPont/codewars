# The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.
# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.
# The following are examples of expected output values:
# rgb(255, 255, 255) # returns FFFFFF
# rgb(255, 255, 300) # returns FFFFFF
# rgb(0,0,0) # returns 000000
# rgb(148, 0, 211) # returns 9400D3


def rgb(r, g, b):
    arr = [r, g, b]
    for i in range(len(arr)):
        if arr[i] > 255:
            arr[i] = 255
        elif arr[i] < 0:
            arr[i] = 0

    arr = [f'{arr[0]:x}'.upper(), f'{arr[1]:x}'.upper(),
           f'{arr[2]:x}'.upper()]

    for i in range(len(arr)):
        if len(arr[i]) == 1:
            arr[i] = f'0{arr[i]}'
    return "".join(arr)


# def rgb(r, g, b):
#     round = lambda x: min(255, max(x, 0))
#     return ("{:02X}" * 3).format(round(r), round(g), round(b))


print(rgb(-20, 275, 125))
