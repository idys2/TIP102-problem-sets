from common import build_tree, TreeNode

'''
input: BST
output: list of (key,val) pairs sorted from least to greatest

- res list
- helper function to inorder traversal

edge cases:
- empty tree: return []
- duplicate rarites: assume no duplicates
'''

def sort_plants(collection: TreeNode):
    result = []

    def inorder(node):
        if node is not None:
          inorder(node.left)
          result.append((node.key, node.val))
          inorder(node.right)

    inorder(collection)
    return result

"""
         (3, "Monstera")
        /               \
   (1, "Pothos")     (5, "Witchcraft Orchid")
        \                 /
  (2, "Spider Plant")   (4, "Hoya Motoskei")
"""

# Using build_tree() function at the top of page
values = [(3, "Monstera"), (1, "Pothos"), (5, "Witchcraft Orchid"), None, (2, "Spider Plant"), (4, "Hoya Motoskei")]
collection = build_tree(values)

print(sort_plants(collection))