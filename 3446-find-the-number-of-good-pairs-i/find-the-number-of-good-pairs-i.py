class Solution:
    def numberOfPairs(self, nums1, nums2, k):
        from collections import Counter

        cnt = Counter(nums2)
        res = 0

        for x in nums1:
            if x % k != 0:
                continue
            val = x // k
            for d in range(1, int(val ** 0.5) + 1):
                if val % d == 0:
                    res += cnt.get(d, 0)
                    if d != val // d:
                        res += cnt.get(val // d, 0)

        return res
