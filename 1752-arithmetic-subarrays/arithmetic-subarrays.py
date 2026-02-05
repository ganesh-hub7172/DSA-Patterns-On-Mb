class Solution:
    def checkArithmeticSubarrays(self, nums, l, r):
        ans = []

        for i in range(len(l)):
            sub = nums[l[i]:r[i] + 1]
            n = len(sub)

            if n < 2:
                ans.append(False)
                continue

            mn = min(sub)
            mx = max(sub)

            if (mx - mn) % (n - 1) != 0:
                ans.append(False)
                continue

            d = (mx - mn) // (n - 1)
            seen = set(sub)

            ok = True
            for k in range(n):
                if mn + k * d not in seen:
                    ok = False
                    break

            ans.append(ok)

        return ans
