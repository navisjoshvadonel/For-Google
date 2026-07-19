class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):
    if not root:            # base case — empty node
        return None

    # swap left and right children
    root.left, root.right = root.right, root.left

    # recursively invert both subtrees
    invertTree(root.left)
    invertTree(root.right)

    return root

# Build tree:
#     2
#    / \
#   1   3
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

# Invert
invertTree(root)

# Print (should be 3 2 1 level by level)
print(root.val)        # 2
print(root.left.val)   # 3
print(root.right.val)  # 1