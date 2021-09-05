class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        output = 0
        for r in range(len(s)):
            if s[r] not in seen:
                seen[s[r]] = r # seen[s[r]] = r을 넣는다고 해서 r, left값에 영향 없음
                output = max(output, r-left+1)
            else:
                if seen[s[r]] < left:
                    seen[s[r]] = r
                    output = max(output, r-left+1)
                else:
                    left = seen[s[r]] + 1 # 여기서는 left가 바뀌기 때문에 실제 연산에 영향을 끼침. sliding window안에 공통인 수가 있으므로, left는 포함되면 안되기 때문에 left를 최근에 발견된 위치에서 1을 더해줘야함
                    seen[s[r]] = r
        return output