'''
input: binary tree
output: 
'''

from common import TreeNode

def is_balanced(root: TreeNode) -> bool:
    
    def dfs(root):
        if not root:
            return 0
        
        left = dfs(root.left)
        right = dfs(root.right)

        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1

        return max(left, right) + 1

    return dfs(root) != -1

# [3, 9, 20, null, null, 15, 7]
tree1 = TreeNode(3, 
                TreeNode(9),
                TreeNode(20,
                         TreeNode(15),
                         TreeNode(7)))
print(is_balanced(tree1))  # True

# [1, 2, 2, 3, 3, null, null, 4, 4]
tree2 = TreeNode(1,
                TreeNode(2,
                         TreeNode(3,
                                  TreeNode(4),
                                  TreeNode(4)),
                         TreeNode(3)),
                None)
print(is_balanced(tree2))  # False

print("---------------------")

def is_valid(root: TreeNode) -> bool:
    def dfs(root, low, high):
        if not root:
            return True
        
        if root.val <= low or root.val >= high:
            return False
        
        return dfs(root.left, low, root.val) and dfs(root.right, root.val, high)

    return dfs(root, float('-inf'), float('inf'))

# [2, 1, 3]
tree3 = TreeNode(2,
                TreeNode(1),
                TreeNode(3))
print(is_valid(tree3))  # True

# [5, 1, 4, null, null, 3, 6]
tree4 = TreeNode(5,
                TreeNode(1),
                TreeNode(4,
                         TreeNode(3),
                         TreeNode(6)))
print(is_valid(tree4))  # False