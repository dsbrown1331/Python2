def three_times_x(x):
    print("three_times_x({})".format(x))
    if x == 0:
        return 0
    else:
        return 3 + three_times_x(x-1)

def x_times_y(x,y):
    if y == 0:
        return 0
    else:
        return x + x_times_y(x, y-1)

print(three_times_x(7))
print(x_times_y(4,6))
