N, K = tuple(map(int,input().split()))
coins = []
for i in range(N):
    temp = int(input())
    if temp <= K:
        coins.append(temp)
coins.reverse()
counts = []
count = 0
K_dup = K
for i, value in enumerate(coins):
    if K // value > 0:
        share = K // value
        K_dup -= share * value
        count += share
    for j in range(i+1, len(coins)):
        sub_share = K_dup // coins[j]
        if K_dup == 0:
            break
        elif sub_share > 0 and sub_share * coins[j] <= K_dup:
            sub_share = K_dup // coins[j]
            K_dup -= sub_share * coins[j]
            count += sub_share
    K_dup = K
    counts.append(count)
    count = 0
print(min(counts))

