# Class Tree Node
from builtins import sorted


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


# Top View of Tree
def top_view(root):
    q = []
    q1 = []
    mp = {}
    q.append(root)
    q1.append(0)
    while q:
        node = q.pop(0)
        s = q1.pop(0)
        if not mp.get(s):
            mp[s] = node.val


        if node.left is not None:
            q.append(node.left)
            q1.append(s-1)
        if node.right is not None:
            q.append(node.right)
            q1.append(s+1)
    
    # Now MP variable is the top view of the tree
    print(mp)        

print("Printing the Top View of the Tree")
top_view(root)
