a = int(input())
if a < 3:
    print(-1)
else:
    check_function = lambda x: x if x * 3 == a or x * 5 == a else a
    m_three = check_function(a//3)
    m_five = check_function(a//5)
    compare = min(m_three, m_five)
    share_five = 1
    arrays = []
    while True:
        tmp = a
        tmp -= 5 * share_five
        share_three = tmp // 3
        if share_five * 5 + share_three * 3 == a and share_five > 0 and share_three > 0:
            arrays.append(share_five + share_three)
        if tmp < 0:
            break
        share_five += 1
    if len(arrays) == 0 and compare == a:
        print(-1)
    elif compare == a:
        print(min(arrays))
    elif len(arrays) == 0:
        print(compare)
    else:
        print(min(compare, min(arrays)))