class Solution:
    def isValidBST(self, root):
        
        def validate(node, low, high):
            if not node:
                return True
            
            # Check current node value in range
            if not (low < node.val < high):
                return False
            
            # Check left and right subtree
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))
        
        return validate(root, float('-inf'), float('inf'))