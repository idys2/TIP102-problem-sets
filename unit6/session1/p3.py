'''
- go through list in one pass
- add 1st node to 1st list, 2nd node to 2nd list...
    - use modulus to wrap around to 1st list 
'''

from common import Node, print_linked_list

def split_protein_chain(protein, k):
    res = []

    curr = protein
    while curr:
        curr = curr.next
    

protein1 = Node('Ala', Node('Gly', Node('Leu', Node('Val', Node('Pro', Node('Ser', Node('Thr', Node('Cys'))))))))
protein2 = Node('Ala', Node('Gly', Node('Leu', Node('Val'))))

parts = split_protein_chain(protein1, 3)
for part in parts:
    print_linked_list(part)

parts = split_protein_chain(protein2, 5)
for part in parts:
    print_linked_list(part)