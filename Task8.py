import random

def table(n):
    people = list(range(0, n))
    random.shuffle(people)
    return people

def check_arrangements(n):
    lunch = table(n)
    dinner = table(n)
    count = 1
    for i in range(10):
        if lunch[i] == dinner[(i + 1) % 10] or lunch[i] == dinner[(i - 1) % 10]:
            count = 0
            break
    return count


true = 0
for i in range(100000):
    fav = check_arrangements(10)
    true += fav

print("The probability that no two people sit next to each other at both lunch and dinner")
print("For 10 participants: ")
favorable = round(true / 100000, 3)
print(favorable)

print("For 50 participants: ")
true = 0
for i in range(100):
    fav = check_arrangements(50)
    true += fav

favorable = round(true / 100000, 3)
print(favorable)

print("For 200 participants: ")
true = 0
for i in range(100000):
    fav = check_arrangements(200)
    true += fav

favorable = round(true / 100000, 3)
print(favorable)

