class Solution:
    def constructMaximumBinaryTree(self, nums):
        def build(arr):
            if not arr:
                return None
            mx = max(arr)
            i = arr.index(mx)
            node = TreeNode(mx)
            node.left = build(arr[:i])
            node.right = build(arr[i + 1:])
            return node

        return build(nums)
