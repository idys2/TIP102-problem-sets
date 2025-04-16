from common import build_tree, print_tree

'''
- perform binary search on the strings
'''

def find_flower(inventory, name):
    current = inventory
    while current:
        if name == current.val:
            return True
        elif name < current.val:
            current = current.left
        else:
            current = current.right
    return False

"""
         Rose
        /    \\
      Lily   Tulip
     /  \\       \\
  Daisy  Lilac  Violet
"""

# using build_tree() function at top of page
values = ["Rose", "Lily", "Tulip", "Daisy", "Lilac", None, "Violet"]
garden = build_tree(values)
print_tree(garden)

print(find_flower(garden, "Lilac"))  
print(find_flower(garden, "Sunflower")) 