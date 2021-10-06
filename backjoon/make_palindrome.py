import sys
name = list(sys.stdin.readline().rstrip())
left = 0
right = len(name) - 1
count = 0
while left < right:
    if name[left] != name[right]:
        try:
            find_index = name[left+1:right].index(name[left])
            name[left + find_index + 1], name[right] = name[right], name[left + find_index + 1]
        except:
            if len(name) % 2 == 1:
                if count > 0:
                    print("I'm Sorry Hansoo")
                    exit()
                else:
                    count += 1
                    name[len(name)//2], name[left] = name[left], name[len(name)//2]
            else:
                print("I'm Sorry Hansoo")
                exit()
        left += 1
        right -= 1
    else:
        left += 1
        right -= 1
print(''.join(name))