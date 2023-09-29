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


#visualization

#               1
#           2      3
#        4     5  6    7


# Sum of Nodes
def sum_of_nodes(root):
    if not root:
        return 0
    return sum_of_nodes(root.left) + sum_of_nodes(root.right) + root.val 


# Execution
print("Sum of nodes of the tree")
print(sum_of_nodes(root))
