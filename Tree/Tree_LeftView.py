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


# Left View of Tree
def left_view(root):
    q = []
    q.append(root)
    while q:
        c = len(q)
        is_first = False
        for i in range(c):
            node = q.pop(0)
            if not is_first:
                print(node.val, end=' ')
                is_first = True
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        print()

print("Printing the Left View of the Tree")
left_view(root)
