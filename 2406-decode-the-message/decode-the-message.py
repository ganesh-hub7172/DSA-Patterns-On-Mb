class Solution:
    def decodeMessage(self, key, message):
        mp = {}
        curr = ord('a')

        for ch in key:
            if ch != ' ' and ch not in mp:
                mp[ch] = chr(curr)
                curr += 1

        res = []
        for ch in message:
            if ch == ' ':
                res.append(' ')
            else:
                res.append(mp[ch])

        return "".join(res)
