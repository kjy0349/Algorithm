class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            res = max(res, self.isPalindrome(s, i, i), self.isPalindrome(s, i, i + 1), key=len)
        return res

    def isPalindrome(self, s: str, l: int, r: int) -> str:  # l,r is middle index of s
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]