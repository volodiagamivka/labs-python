import math

x = 3

while 3 <= x <= 6:
    x = x + 0.2
    if x < 4:
        a = math.log(x) - math.cos(x)
        print(x, a)
    elif 4 <= x < 5:
        b = 1 / math.tan(math.radians(math.exp(x) + 3))
        print(x, b)
    else:
        c = (5 * x) ** x
        print(x, c)


