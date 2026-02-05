class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x):
        s = 0
        n = x

        while n > 0:
            s += n % 10
            n //= 10

        if x % s == 0:
            return s
        return -1
