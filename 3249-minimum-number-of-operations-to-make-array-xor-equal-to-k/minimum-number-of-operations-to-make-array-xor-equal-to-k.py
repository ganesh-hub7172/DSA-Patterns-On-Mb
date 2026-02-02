class Solution:
    def minOperations(self, nums, k):
        x = 0
        for n in nums:
            x ^= n
        diff = x ^ k
        return bin(diff).count("1")
