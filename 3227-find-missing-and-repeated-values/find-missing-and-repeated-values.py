class Solution:
    def findMissingAndRepeatedValues(self, grid):
        n = len(grid)
        freq = [0] * (n * n + 1)

        for row in grid:
            for x in row:
                freq[x] += 1

        repeat = missing = -1
        for i in range(1, n * n + 1):
            if freq[i] == 2:
                repeat = i
            elif freq[i] == 0:
                missing = i

        return [repeat, missing]
