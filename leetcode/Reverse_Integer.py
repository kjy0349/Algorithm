class Solution:
    def reverse(self, x: int) -> int:
        if x < -2**31 or x > 2**31 -1:
            return 0
        else:
            s = str(x)
            i = 0
            result = []
            symbol = ''
            while True:
                if i >= len(s):
                    break
                else:
                    if s[i].isdecimal():
                        result.append(s[i])
                    else:
                        symbol = s[i]
                    i += 1
            result.reverse()
            res = int(symbol + ''.join(result))
            if res < -2**31 or res > 2**31 -1:
                return 0
            else:
                return res