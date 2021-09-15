import sys
S = int(sys.stdin.readline().rstrip())
count = 0
compare_number = 0
for i in range(S):
    count += 1
    compare_number += count
    if compare_number == S:
        print(i+1)
        break
    elif compare_number > S:
        print(i)
        break
