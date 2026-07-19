from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root):
    if not root:
        return []

    result = []
    queue = deque([root])   # start with root in queue

    while queue:
        level_size = len(queue)   # how many nodes at this level
        level = []                # collect this level's values

        for _ in range(level_size):
            node = queue.popleft()        # process front node
            level.append(node.val)        # add value to level

            if node.left:                 # add left child
                queue.append(node.left)
            if node.right:                # add right child
                queue.append(node.right)

        result.append(level)   # add completed level to result

    return result

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

print(levelOrder(root))  # [[3], [9, 20], [15, 7]]