# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: int
        """

        return self.getSum(root, low, high)
        
    def getSum(self, node, low, high):
        if node is None:
            return 0

        val = 0
        if low <= node.val <= high:
            val = node.val

        if node.val <= low:
            return self.getSum(node.right, low, high) + val
        elif node.val >= high:
            return self.getSum(node.left, low, high) + val
        else:
            return self.getSum(node.left, low, high) + self.getSum(node.right, low, high) + val

        
