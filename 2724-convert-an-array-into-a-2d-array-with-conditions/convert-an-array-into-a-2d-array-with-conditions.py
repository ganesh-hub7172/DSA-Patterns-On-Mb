class Solution:
    def findMatrix(self, nums):
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        res = []
        while freq:
            row = []
            for n in list(freq.keys()):
                row.append(n)
                freq[n] -= 1
                if freq[n] == 0:
                    del freq[n]
            res.append(row)

        return res
