class Solution:
    def convert(self, s: str, numRows: int) -> str:
        tmp_array = []
        if len(s) < 1 or len(s) > 1000:
            return ""
        else:
            for i in range(numRows):
                tmp_array.append('')
            reach_max = False
            j = 0
            i = 0
            while j < len(s):
                tmp_array[i] += s[j]
                if reach_max and i > 0:
                    i -= 1
                elif reach_max is False and i < numRows-1:
                    i += 1
                if i == 0:
                    reach_max = False
                if i == numRows-1:
                    reach_max = True
                j += 1
        return ''.join(tmp_array)