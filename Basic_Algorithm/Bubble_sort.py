numbers = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9, 14, 0, -12, -36]
for i in range(len(numbers) - 1):
    for j in range(i+1, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

print(numbers)