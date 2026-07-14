class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root):
    if not root:          # base case — empty tree
        return 0

    left_depth = maxDepth(root.left)    # depth of left subtree
    right_depth = maxDepth(root.right)  # depth of right subtree

    return 1 + max(left_depth, right_depth)  # current node + deeper side

# Build tree:
#     3
#    / \
#   9  20
#      / \
#     15   7

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(maxDepth(root))  # 3