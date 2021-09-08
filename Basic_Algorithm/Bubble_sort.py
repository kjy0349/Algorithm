numbers = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9, 14, 0, -12, 48]
for i in range(len(numbers) - 1):
    for j in range(len(numbers) - 1 - i):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
print(numbers)

# O(n^2)

# 1. 정렬된 데이터 : 비교만하고 실제적인 교환은 일어나지 않음.
# 2. 역순으로 정렬된 데이터 : 앞에있는 큰 수들을 뒤로 옮기려면 n-1번의 교환이 매 순환마다 일어나므로 비효율적임
# 3. 랜덤 데이터 : 평균적인 정렬