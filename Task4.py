import random
import math

simulations = int(input("Input number of simulations: "))
count_acute_triangles = 0


def find_y(x):
    return math.sqrt(1 - x ** 2)


def generate_pos():
    x = random.uniform(-1, 1)
    y = find_y(x)
    y = random.uniform(-y, y)
    return x, y


def is_acute(a1, a2, a3):
    return a1 < 90 and a2 < 90 and a3 < 90


for index in range(simulations):

    (point1_x, point1_y) = generate_pos()
    (point2_x, point2_y) = generate_pos()
    (point3_x, point3_y) = generate_pos()

    line1 = [point2_x - point1_x, point2_y - point1_y]
    line2 = [point3_x - point2_x, point3_y - point2_y]
    line3 = [point1_x - point3_x, point1_y - point3_y]

    len_line1 = math.sqrt(line1[0] ** 2 + line1[1] ** 2)
    len_line2 = math.sqrt(line2[0] ** 2 + line2[1] ** 2)
    len_line3 = math.sqrt(line3[0] ** 2 + line3[1] ** 2)

    angle1 = math.degrees(math.acos((len_line1 ** 2 + len_line3 ** 2 - len_line2 ** 2) / (2 * len_line1 * len_line3)))
    angle2 = math.degrees(math.acos((len_line1 ** 2 + len_line2 ** 2 - len_line3 ** 2) / (2 * len_line1 * len_line2)))
    angle3 = math.degrees(math.acos((len_line2 ** 2 + len_line3 ** 2 - len_line1 ** 2) / (2 * len_line3 * len_line2)))

    if angle1 < 90 and angle2 < 90 and angle3 < 90:
        count_acute_triangles += 1

probability = count_acute_triangles / simulations * 100
print(f"The probability of forming a triangle with three acute angles is approximately: {probability:.2f}%")
