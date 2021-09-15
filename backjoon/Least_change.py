M = int(input())
change = 1000 - M
changes = {500: 0, 100: 0, 50: 0, 10: 0, 5: 0, 1: 0}
keys = list(changes.keys())
compare_list = []
for i, key in enumerate(list(changes.keys())):
    if (change // key) * key == change and change // key > 0:
        compare_list.append(change // key)
compare_change = min(compare_list)
i = 0
while change > 0:
    if change >= keys[i] and change // keys[i] > 0:
        changes[keys[i]] += change // keys[i]
        change -= (change // keys[i]) * keys[i]
    i += 1
print(min(compare_change, sum(list(changes.values()))))