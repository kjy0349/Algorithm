class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) < 2 or len(nums) > 10**4 or target < -10**9 or target > 10**9:
                return []
        else:
            i = 0
            while True:
                if nums[i] < -10**9 or nums[i] > 10**9:
                    return []
                else:
                    if i >= len(nums):
                        break
                    else:
                        res1 = target - nums[i]
                        if res1 in nums and nums.index(res1) != i:
                            return [nums.index(res1), i]
                        i += 1
