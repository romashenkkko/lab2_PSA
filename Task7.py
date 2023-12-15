import random
import matplotlib.pyplot as plt

heads_up = []

for side in range(1000):
    heads = 0
    for side in range(100):
        coin = random.randint(0, 1)
        if coin == 1:
            heads += 1

    heads_up.append(heads)

head_counts = []
for number in range(35, 66):
    head_counts.append(heads_up.count(number))

total_experiments = len(heads_up)
proportion = []
for count in head_counts:
    proportion.append(count / total_experiments)

plt.bar(range(35, 66), proportion, align='center')
plt.xlabel('Number of Heads')
plt.ylabel('Proportion')
plt.title('Proportion of Experiments with Number of Heads in Range [35, 65]')
plt.show()