from common import TreeNode

def helper(res, node):
    if not node:
        return
    helper(res, node.left)
    helper(res, node.right)
    res.append(node.val)

def survey_tree(root):
    if not root:
        return 

    res = []
    helper(res, root)
    return res

"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""

magnolia = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")), TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))
print(survey_tree(magnolia))