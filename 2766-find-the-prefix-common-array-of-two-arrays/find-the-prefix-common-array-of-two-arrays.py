class Solution:
    def findThePrefixCommonArray(self, A, B):
        seenA = set()
        seenB = set()
        res = []
        count = 0

        for i in range(len(A)):
            a, b = A[i], B[i]

            seenA.add(a)
            seenB.add(b)

            if a in seenB:
                count += 1
            if b in seenA and a != b:
                count += 1

            res.append(count)

        return res
