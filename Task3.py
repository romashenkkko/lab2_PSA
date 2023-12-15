from random import uniform


def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


simulations = int(input("Number of simulations: "))
valid = 0

for i in range(simulations):
    break_point = uniform(0, 1)
    stick1 = break_point
    stick2 = 1 - break_point
    if stick1 >= stick2:
        stick3 = uniform(0, stick1)
        stick1 -= stick3
    else:
        stick3 = uniform(0, stick2)
        stick2 -= stick3

    if is_triangle(stick1, stick2, stick3):
        valid += 1

print(str(valid*100/simulations)+"%")