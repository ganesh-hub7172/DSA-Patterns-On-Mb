class Solution:
    def subarraySum(self, nums):
        total = 0
        for i in range(len(nums)):
            start = max(0, i - nums[i])
            total += sum(nums[start:i + 1])
        return total
