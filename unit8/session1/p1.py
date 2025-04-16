from common import TreeNode

'''
input: binary tree
output: path from root to rightmost leaf: list

- iterate to right child every time until we reach null
- keep a running list of the path
'''

def right_vine(root):
    curr = root
    path = []

    while curr:
        path.append(curr.val)
        curr = curr.right

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