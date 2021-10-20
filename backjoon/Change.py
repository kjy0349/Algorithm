import sys
coins = {2: 0, 5: 0}
value = int(sys.stdin.readline())
can_be = False
possible_count = [value // coin if value % coin == 0 else value for coin in list(coins.keys())]
if possible_count.count(value) == len(coins):
    pass
else:
    can_be = True
while value > 0:
    value -= 5
    if value > 0:
        coins[5] += 1
    else:
        break
    if value % 2 == 0:
        mok = value // 2
        value -= mok * 2
        coins[2] += mok
    if all([True if coin > value else False for coin in list(coins.keys())]):
        break

if can_be and value == 0:
    one_count = min(possible_count)
    mix_count = sum(list(coins.values()))
    print(min(one_count, mix_count))
elif not can_be and value == 0:
    print(sum(list(coins.values())))
elif can_be and value != 0:
    print(min(possible_count))
else:
    print(-1)
