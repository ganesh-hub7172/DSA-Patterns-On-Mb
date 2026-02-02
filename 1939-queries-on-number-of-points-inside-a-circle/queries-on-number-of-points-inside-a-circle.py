class Solution:
    def countPoints(self, points, queries):
        ans = []
        for x, y, r in queries:
            r2 = r * r
            count = 0
            for px, py in points:
                if (px - x) ** 2 + (py - y) ** 2 <= r2:
                    count += 1
            ans.append(count)
        return ans
