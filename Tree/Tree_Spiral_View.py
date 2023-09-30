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


# Spiral View of Tree
def spiral_view(root):
    q = []
    q.append(root)
    is_first  = True
    while q:
        s = []
        c = len(q)
        for i in range(c):
            node = q.pop(0)
            s.append(node.val)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        if is_first:
            print(s)
            is_first = False
        else:
            print(s[::-1])
            is_first = True

print("Printing the Spiral View of the Tree")
spiral_view(root)
