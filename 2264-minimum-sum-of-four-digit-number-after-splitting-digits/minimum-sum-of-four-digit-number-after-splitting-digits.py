class Solution:
    def minimumSum(self, num):
        digits = sorted(str(num))
        a = digits[0] + digits[2]
        b = digits[1] + digits[3]
        return int(a) + int(b)
