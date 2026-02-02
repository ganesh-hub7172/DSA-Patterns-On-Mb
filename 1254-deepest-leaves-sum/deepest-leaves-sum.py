class Solution:
    def deepestLeavesSum(self, root):
        self.max_depth = -1
        self.total = 0

        def dfs(node, depth):
            if not node:
                return
            if depth > self.max_depth:
                self.max_depth = depth
                self.total = node.val
            elif depth == self.max_depth:
                self.total += node.val
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return self.total
