class Solution:
    def sortVowels(self, s):
        vowels = set("aeiouAEIOU")
        v = []

        for c in s:
            if c in vowels:
                v.append(c)

        v.sort()

        res = []
        idx = 0
        for c in s:
            if c in vowels:
                res.append(v[idx])
                idx += 1
            else:
                res.append(c)

        return "".join(res)
