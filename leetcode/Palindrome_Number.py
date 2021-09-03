class Solution:
    def isPalindrome(self, x: int) -> bool:
        s_array = list(str(x))
        r_array = list(reversed(s_array))
        if s_array == r_array:
            return True
        else:
            return False
