class Solution:
    def getTargetCopy(self, original, cloned, target):
        if not original:
            return None
        if original is target:
            return cloned
        left = self.getTargetCopy(original.left, cloned.left, target)
        if left:
            return left
        return self.getTargetCopy(original.right, cloned.right, target)
