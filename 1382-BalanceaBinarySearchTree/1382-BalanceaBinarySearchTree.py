    
    def construct_bst(self, left, right, path):
        if left > right:
            return None
        middle = (left+right)//2
        path[middle].left = self.construct_bst(left, middle-1, path)
        path[middle].right = self.construct_bst(middle+1, right, path)
        return path[middle]
    
    def balanceBST(self, root: TreeNode) -> TreeNode:
        path = self.inorder_bts(root)
        return self.inorder_bts(root.left) + [root] + self.inorder_bts(root.right)
            return []
        if not root:
    def inorder_bts(self, root):
class Solution:
[
