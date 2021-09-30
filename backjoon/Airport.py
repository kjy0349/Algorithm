import sys
G = int(sys.stdin.readline())
P = int(sys.stdin.readline())
Gates = [False] * G
count = 0
for i in range(P):
    is_docked = False
    plane = int(sys.stdin.readline())
    if plane - 1 == 0:
        if Gates[0] is True:
            break
        else:
            Gates[0] = True
            count += 1
            continue
    else:
        for j in range(plane-1, -1, -1):
            if Gates[j] is False:
                Gates[j] = True
                count += 1
                is_docked = True
                break
            else:
                pass
    if is_docked is False:
        break
    else:
        pass
print(count)
