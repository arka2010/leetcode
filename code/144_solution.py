# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def preorder_iterative(self, root):
        results = []
        stack = [root] if root else []
        while stack:
            node = stack.pop()
            results.append(node.val)
            for child in [node.right, node.left]:
                if not child: continue
                stack.append(child)
        return results

    def preorder_iterative_with_set(self, root):
        results = []
        stack, visited = [root], set()
        while stack:
            node = stack.pop()
            if not node: continue
            if node in visited: results.append(node.val)
            else:
                visited.add(node)
                # stack.extend([node.right, node, node.left])  # inorder
                # stack.extend([node, node.right, node.left])  # postorder
                stack.extend([node.right, node.left, node])  # preorder

    def preorder_recursive(self, root):
        results = []

        def dfs(node):
            if not node: return 
            results.append(node.val)
            if node.left: dfs(node.left)
            if node.right: dfs(node.right)

        dfs(root)
        return results

    preorderTraversal = preorder_recursive # preorder_iterative # preorder_iterative_with_set