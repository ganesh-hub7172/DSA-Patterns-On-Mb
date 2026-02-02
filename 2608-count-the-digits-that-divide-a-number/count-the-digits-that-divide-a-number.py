class Solution:
    def countDigits(self, num):
        count = 0
        for d in str(num):
            if int(d) != 0 and num % int(d) == 0:
                count += 1
        return count
