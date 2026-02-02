class Solution:
    def minOperations(self, nums, k):
        nums.sort()
        count = 0
        for x in nums:
            if x < k:
                count += 1
            else:
                break
        return count
