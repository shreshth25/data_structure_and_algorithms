# Class Tree Node
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Creating Tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

root.left.left.left = TreeNode(8)

#visualization

#               1
#           2      3
#        4     5  6    7
#       8


# Level Order Traversal of Tree
def level_order_traversal(root):
    q = []
    q.append(root)
    while q:
        node = q.pop(0)
        print(node.val, end =' ')
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)

level_order_traversal(root)
