from collections import deque

def compare_count(a, b):
    sen = zip(a,b)
    count = 0
    for i,j in sen: # 문자열 2개를 비교해서, 다른 문자의 개수를 return 해줌
        if i != j: count += 1
    return count

def solution(begin, target, words):
    if target not in words:
        return 0
    queue = deque()
    queue.append([begin, []])

    while queue:
        n, l = queue.popleft() # n = word, l = possible indices
        for word in words:
            if word not in l and compare_count(word, n) == 1:
                if word == target:
                    return len(l) + 1
                temp = l[:]
                temp.append(word)
                queue.append([word, l[:]])
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))