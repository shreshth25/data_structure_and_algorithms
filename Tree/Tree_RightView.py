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


# visualization
#               1
#           2        3
#        4     5  6    7


# Right View of Tree
def right_view(root):
    q = []
    q.append(root)
    while q:
        c = len(q)
        for i in range(c):
            node = q.pop(0)
            if i == c-1:
                print(node.val, end=' ')
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        print()

print("Printing the Right View of the Tree")
right_view(root)
