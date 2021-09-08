from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = []
        left, right = 0, len(height)-1
        m_area = -1
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            m_area = max(m_area, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return m_area