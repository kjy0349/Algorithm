import sys
document = sys.stdin.readline().rstrip()
word = sys.stdin.readline().rstrip()
index = 0
i = 0
count = 0
while i < len(document):
    if document[i] == word[index]:
        if index == len(word)-1:
            index = 0
            count += 1
        else:
            index += 1
    else:
        if index > 0:
            i -= index
            index = 0
        else:
            index = 0
    i += 1
print(count)
