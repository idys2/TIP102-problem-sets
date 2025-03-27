from common import Node

def cycle_length(protein: Node) -> list[str]:
    fast = slow = protein
    res = []

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    if not slow:
        return res
    
    res.append(slow.value)
    slow = slow.next
    while slow != fast:
        res.append(slow.value)
        slow = slow.next
    
    return res
    
protein_head = Node('Ala', Node('Gly', Node('Leu', Node('Val'))))
protein_head.next.next.next.next = protein_head.next 

print(cycle_length(protein_head))