from common import TreeNode
'''
same as previous, but recursive

base case: right child is null
- 
'''
def helper(path, node):
    path.append(node.val)
    if node.right:
        helper(path, node.right)

def right_vine(root):
    if not root:
        return []
    
    path = []
    helper(path, root)
    return path

"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""
ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

"""
      Root
      /  
    Node1
    /
  Leaf1  
"""
ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

print(right_vine(ivy1))
print(right_vine(ivy2))