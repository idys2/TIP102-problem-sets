from common import Node

def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

list1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
list2 = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
             
print(find_middle(list1).value)  # 3
print(find_middle(list2).value)  # 4