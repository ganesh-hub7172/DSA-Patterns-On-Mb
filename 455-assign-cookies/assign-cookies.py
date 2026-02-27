class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        
        child = 0
        cookie = 0
        
        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                child += 1   # child is satisfied
            cookie += 1      # move to next cookie
        
        return child