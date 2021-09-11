# N = int(input())
# P = list(map(int, input().split(" ")))
# P_dict = {i: P[i-1] for i in range(1, N+1)}
# result_time = 0
# tmp_P = P[:]
# result = []
# for i in range(N):
#     min_time = min(tmp_P)
#     result.append(tmp_P.index(min_time)+1)
#     tmp_P[tmp_P.index(min_time)] = max(tmp_P) + 1
# for i in range(N):
#     for j in range(i+1):
#         result_time += P_dict[result[j]]
# print(result_time)

N = int(input())
P = list(map(int, input().split()))
P.sort()
count = 0
result = 0
for i in P:
    count += i
    result += count
print(result)