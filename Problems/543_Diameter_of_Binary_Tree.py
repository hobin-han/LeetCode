# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def __init__(self):
        self.result = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.result = 0
        self.longestLenght(root)
        return self.result
        

    def longestLenght(self, node):
        if node is None:
            return None
        if node.left is None and node.right is None:
            return 0

        leftLength = self.longestLenght(node.left)
        rightLength = self.longestLenght(node.right)

        left = 0 if leftLength is None else leftLength + 1
        right = 0 if rightLength is None else rightLength + 1
        
        total = left + right
        if self.result < total:
            self.result = total

        return left if left > right else right
