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


# Count Nodes of the Tree
def count_nodes_of_tree(root):
    if not root:
        return 0
    return count_nodes_of_tree(root.left) +  count_nodes_of_tree(root.right) + 1


# Execution
print("Nodes of the tree")
print(count_nodes_of_tree(root))
