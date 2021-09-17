import sys; r = sys.stdin.readline
S = list(map(int, list(r().rstrip())))
zero_count = S.count(0)
one_count = S.count(1)
result = 0
min_count = min(zero_count, one_count)
if len(S) == 0:
    print(0)
if min_count == zero_count:
    while S.count(0) > 0:
        left_index = S.index(0)
        right_index = left_index + 1
        for number in S[left_index+1:]:
            if number == 1:
                break
            else:
                right_index += 1
        S[left_index:right_index+1] = [1] * (right_index-left_index +1)
        result += 1
else:
    while S.count(1) > 0:
        left_index = S.index(1)
        right_index = left_index + 1
        for number in S[left_index+1:]:
            if number == 0:
                break
            else:
                right_index += 1
        S[left_index:right_index+1] = [0] * (right_index-left_index + 1)
        result += 1
print(result)
