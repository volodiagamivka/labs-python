import math

step = 0.2
x = -1
while x <= 1:
    k = 2
    delta = 0.001
    y = 0
    while True:
        sum = (((-1) ** k) * k / (k**2 - 1)) * math.sin(k * x)

        print("", x, k, sum)
        if abs(sum) < delta:
            break
        y += sum
        k += 1
    print(round(x, 8), k, sum)
    x += step

