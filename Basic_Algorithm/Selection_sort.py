inp = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9, 14, 0, -12, 48]
for i in range(len(inp) - 1):
    min_value = min(inp[i:])
    index = inp.index(min_value) # python swap doesn't occur at the same time, so we must save index at variable
    inp[i], inp[index] = inp[index], inp[i]
print(inp)
