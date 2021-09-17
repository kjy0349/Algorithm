import sys; r = sys.stdin.readline
N = int(r().rstrip())
words = []
number = 9
result = 0
for _ in range(N):
    words.append(r().rstrip())
word_dict = {}

for word in words:
    square_root = len(word) - 1
    for alphabet in word:
        if alphabet in word_dict:
            word_dict[alphabet] += pow(10, square_root)
        else:
            word_dict[alphabet] = pow(10, square_root)
        square_root -= 1
word_dict = sorted(word_dict.values(), reverse=True)
for value in word_dict:
    result += value * number
    number -= 1
print(result)
