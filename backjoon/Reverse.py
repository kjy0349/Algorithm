import sys; r = sys.stdin.readline
S = list(map(int, list(r().rstrip())))
zero_block_count = 0
one_block_count = 0

if len(S) == 0:
    print(0)
else:
    compare = S[0]
    if compare == 1:
        one_block_count += 1
    else:
        zero_block_count += 1
    for number in S:
        if number == compare:
            pass
        else:
            compare = number
            if compare == 0:
                zero_block_count += 1
            else:
                one_block_count += 1
print(min(zero_block_count, one_block_count))