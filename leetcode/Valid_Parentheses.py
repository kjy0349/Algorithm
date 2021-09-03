class Solution:
    def isValid(self, s: str) -> bool:
        c_dic = {'(': ')', '[': ']', '{': '}'}
        c_stack = [s[0]]
        for i in range(1, len(s)):
            if c_stack and c_stack[-1] in c_dic:
                if c_dic[c_stack[-1]] == s[i]:
                    c_stack.pop()
                else:
                    c_stack.append(s[i])
            else:
                c_stack.append(s[i])
        if len(c_stack) == 0:
            return True
        else:
            return False