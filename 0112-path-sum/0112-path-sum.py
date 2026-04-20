class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        
        # Check if it's a leaf node
        if not root.left and not root.right:
            return targetSum == root.val
        
        # Recur for left and right with reduced sum
        new_sum = targetSum - root.val
        
        return (self.hasPathSum(root.left, new_sum) or 
                self.hasPathSum(root.right, new_sum))