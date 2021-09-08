inp = [1, 10, 5, 8, 7, 6, 4,77, 3, 2, 9, 14, 0, -12, 48]
length = len(inp)
for i in range(1,  length):
    for j in range(i):
        if inp[i] < inp[j]:
            inp[j], inp[i] = inp[i], inp[j]
    print(inp[:i])