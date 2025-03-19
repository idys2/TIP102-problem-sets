from collections import deque
'''
- sort attendees in order
- create deque
    - pop first number, add to front of deque
    - pop next number, add to back of deque
    - repeat until attendees stack is empty

ex:
    [2,3,5,7,11,13,17
'''

def reveal_attendee_list_in_order(attendees):
    attendees.sort()
    #attendees = attendees[::-1]
    queue = deque()
    
    while attendees:
        queue.appendleft(attendees.pop())
        
        if attendees:
            queue.append(attendees.pop())
    
    return list(queue)
    


print(reveal_attendee_list_in_order([17,13,11,2,3,5,7])) 
print(reveal_attendee_list_in_order([1,1000]))
