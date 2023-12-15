import random

def Boy():
    gender = random.randint(0, 1)
    g = 0
    while gender == 1:
        gender = random.randint(0, 1)
        g += 1
    return g + 1

def Boy_and_Girl():
    gender = random.randint(0, 1)
    g = 0
    b = 0
    if gender > 0.5:
        kid = "GIRL"
        g = 1
    else:
        kid = "BOY"
        b = 1
    kids = [kid]
    while "BOY" not in kids or "GIRL" not in kids:
        gender = random.randint(0, 1)
        if gender == 1:
            kid = "GIRL"
            g += 1
        else:
            kid = "BOY"
            b += 1
        kids.append(kid)
    children = g + b
    return children


tries = 0
for child in range(1000000):
    tries += Boy()
average = tries / 1000000
print(f"{round(average)} children")

case2 = 0
for child in range(1000000):
    case2 += Boy_and_Girl()
average2 = case2 / 1000000
print(f"\n{round(average2)} children")
