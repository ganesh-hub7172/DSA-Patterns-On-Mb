class Solution:
    def numTilePossibilities(self, tiles):
        freq = {}
        for c in tiles:
            freq[c] = freq.get(c, 0) + 1

        def dfs():
            count = 0
            for c in freq:
                if freq[c] > 0:
                    count += 1
                    freq[c] -= 1
                    count += dfs()
                    freq[c] += 1
            return count

        return dfs()
