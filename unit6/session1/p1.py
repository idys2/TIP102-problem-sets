'''
input: linked list of [A,T,C,G], integers m and n
output: modified linked list

- retain the first m nodes
- remove next n nodes
- repeat until you reach end of the list

edge cases
- m + n nodes
- number of nodes <= m: list is not modified
- number of nodes > m but < n: doesn't delete n nodes
- m = 0: empty
- n = 0: list is not modified

- iterate through list while it's nonempty
- keep two counters for m and n, reset after each cycle
'''

from common import Node, print_linked_list

def edit_dna_sequence(dna_strand, m, n):
    if m == 0:
        return None
    if n == 0:
        return dna_strand
    
    prev = None
    curr = dna_strand

    while curr:
        m_counter = 0
        n_counter = 0

        while m_counter < m and curr:
            m_counter += 1
            prev = curr
            curr = curr.next

        while n_counter < n and curr:
            n_counter += 1
            curr = curr.next
        
        if prev:
            prev.next = curr

    return dna_strand

dna_strand = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10, Node(11, Node(12, Node(13)))))))))))))

#print_linked_list(edit_dna_sequence(dna_strand, 2, 3))
#print_linked_list(edit_dna_sequence(dna_strand, 2, 0)) # unchanged
#print_linked_list(edit_dna_sequence(dna_strand, 100, 0)) # unchanged
#print_linked_list(edit_dna_sequence(dna_strand, 0, 0)) # None
print_linked_list(edit_dna_sequence(dna_strand, 1, 100)) # first node only