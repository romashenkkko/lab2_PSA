from random import randint
import matplotlib.pyplot as plt

num_of_sim = int(input("How many simulations?"))
data = {}
for i in range(num_of_sim):
    dice1, dice2, dice3 = randint(1, 6), randint(1, 6), randint(1, 6)
    sum = dice1 + dice2 + dice3
    if sum in data:
        data[sum] += 1
    else:
        data[sum] = 0

output = ["9", "10"]
values = [data[9], data[10]]

fig = plt.figure(figsize=(5, 5))

# creating the bar plot
plt.bar(output, values, color='maroon', width=0.2)

plt.xlabel("Courses offered")
plt.ylabel("No. of students enrolled")
plt.title("Students enrolled in different courses")
plt.show()