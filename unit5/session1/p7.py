class Node:
    def __init__(self, fish_name, next=None):
        self.fish_name = fish_name
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.fish_name, end=" -> " if current.next else "\n")
        current = current.next

'''
input: linked list, string name of a fish
output: probability of getting that fish, rounded to the nearest 100th

- iterate through the linked list
- return count of occurrences / n

edge cases:
- empty list: return 0
- empty string can still occur in the list
'''

def fish_chances(head, fish_name):
    curr = head
    n = 0
    count = 0

    # iterate through list
    while curr:
        n += 1
        if curr.fish_name == fish_name:
            count += 1
        curr = curr.next

    return "%.2f" % (count / n)

fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
print(fish_chances(fish_list, "Dace"))
print(fish_chances(fish_list, "Rainbow Trout"))