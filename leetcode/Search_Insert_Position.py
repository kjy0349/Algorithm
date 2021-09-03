from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) < 1 or len(nums) > 10**4 or target < -(10**4) or target > 10**4:
            return 0
        else:
            start, end = 0, len(nums)-1
            mid = (start + end) // 2
            while start <= end and target != nums[mid]:
                mid = (start + end) // 2
                if nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            if target not in nums:
                return start
            else:
                return mid