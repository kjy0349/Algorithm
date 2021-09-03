class Solution:
    def romanToInt(self,s: str) -> int:
        roman_symbol = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        if len(s) < 1 or len(s) > 15:
            return 0
        else:
            result = 0
            for i in range(len(s)):
                try:
                    if roman_symbol[s[i]] < roman_symbol[s[i+1]]:
                        result -= roman_symbol[s[i]]
                    else:
                        result += roman_symbol[s[i]]
                except:
                    result += roman_symbol[s[i]]
        return result