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
#     8


# Height of the Tree
def height_of_tree(root):
    if not root:
        return 0
    return max(height_of_tree(root.left), height_of_tree(root.right)) + 1


# Execution
print("height of the tree")
print(height_of_tree(root))