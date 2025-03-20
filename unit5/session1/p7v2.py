from common import Node

'''
- iterate to the end of the list
- return the last player
'''
def last_place(head):
	if not head:
		return None

	curr = head
	while curr.next:
		curr = curr.next
	return curr.player_name

racers1 = Node("Mario", Node("Peach", Node("Luigi", Node("Daisy"))))
racers2 = Node("Mario")

print(last_place(racers1)) 
print(last_place(racers2)) 
print(last_place(None))