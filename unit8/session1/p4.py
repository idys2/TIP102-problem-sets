from common import TreeNode

'''
input: binary tree
output: sum of values in the tree
'''

def sum_inventory(node):

    # base case: node is None
    if not node:
        return 0
    
    # recursive case: add left subtree + value + right subtree
    else:
        return sum_inventory(node.left) + node.val + sum_inventory(node.right)
    

"""
     40
    /  \
   5   10
  /   /  \
20   1   30
"""

inventory = TreeNode(40, 
                    TreeNode(5, TreeNode(20)),
                            TreeNode(10, TreeNode(1), TreeNode(30)))

print(sum_inventory(inventory))