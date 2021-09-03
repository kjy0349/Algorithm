from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs:
            shortest = min(strs, key = len)
            for i in range(len(shortest)):
                if any(word[i] != shortest[i] for word in strs):
                    return shortest[:i]
            return shortest
        return ""