statement = input()
numbers = list(statement.split('-'))
for i, sub_statement in enumerate(numbers):
    if '+' in sub_statement:
        r_sub = list(map(int, sub_statement.split('+')))
        numbers[i] = sum(r_sub)
    else:
        numbers[i] = int(sub_statement)
result = numbers[0]
for i in range(1, len(numbers)):
    result -= numbers[i]
print(result)