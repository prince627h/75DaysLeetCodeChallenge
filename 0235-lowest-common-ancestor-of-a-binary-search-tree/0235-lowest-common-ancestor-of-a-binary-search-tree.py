class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        
        # Both nodes in left subtree
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        # Both nodes in right subtree
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        # Split point → this is LCA
        return root