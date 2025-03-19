def arrange_guest_arrival_order(arrival_pattern):
    guest_order = []
    stack = []
    n = len(arrival_pattern)
    
    for i in range(1, n+1):
        stack.append(str(i))
        
        if i == n or arrival_pattern[i-1] == 'I':
            while stack:
                guest_order.append(stack.pop())
    
    return ''.join(guest_order)

print(arrange_guest_arrival_order("IIIDIDDD"))  
print(arrange_guest_arrival_order("DDD"))
