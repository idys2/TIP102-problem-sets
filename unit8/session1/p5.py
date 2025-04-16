from common import TreeNode

def calculate_yield(node):
    if not node.val:
        return 0
    
    if node.val == "+":
        return calculate_yield(node.left) + calculate_yield(node.right)
    elif node.val == "-":
        return calculate_yield(node.left) - calculate_yield(node.right)
    elif node.val == "*":
        return calculate_yield(node.left) * calculate_yield(node.right)
    elif node.val == "/":
        return calculate_yield(node.left) // calculate_yield(node.right)
    else:
        return node.val
        
"""
      +
     / \\ 
    /   \\
   -     *
  / \\   / \\
 4   2 10  2
"""

root = TreeNode("+")
root.left = TreeNode("-")
root.right = TreeNode("*")
root.left.left = TreeNode(4)
root.left.right = TreeNode(2)
root.right.left = TreeNode(10)
root.right.right = TreeNode(2)

print(calculate_yield(root))