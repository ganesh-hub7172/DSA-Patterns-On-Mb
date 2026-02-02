class Solution:
    def subtractProductAndSum(self, n):
        prod = 1
        summ = 0
        for d in str(n):
            prod *= int(d)
            summ += int(d)
        return prod - summ
