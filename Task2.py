from random import randint

repu = int(input("Republic: "))
demo = 100 - repu
n = int(input("Number of simulations: "))

results = {"Republic": 0, "Democratic": 0}

for i in range(n):
    num = randint(1, 100)
    is_repu = num <= repu
    if is_repu:
        results["Republic"] += 1
    else:
        results["Democratic"] += 1

print("Republic: ", results["Republic"]/n, "%, Democratic: ", results["Democratic"]/n, "%")