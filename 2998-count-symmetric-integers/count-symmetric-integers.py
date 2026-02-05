class Solution:
    def countSymmetricIntegers(self, low, high):
        count = 0

        for x in range(low, high + 1):
            s = str(x)
            n = len(s)

            if n % 2 == 1:
                continue

            half = n // 2
            left = 0
            right = 0

            for i in range(half):
                left += ord(s[i]) - ord('0')
                right += ord(s[i + half]) - ord('0')

            if left == right:
                count += 1

        return count
