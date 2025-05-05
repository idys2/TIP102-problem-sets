'''
input: dict of tuples, start string, dest string
output: total cost of any flight path from start to dest

- bfs
'''
from collections import deque
'''def calculate_cost(flights, start, dest):
    visited = set([start])
    queue = deque([start])
    total_cost = 0

    while queue:
        current = queue.popleft()

        if current == dest:
            break

        for neighbor in flights[current]:
            
            if current == start:
                total_cost += neighbor[1]

            print(neighbor, total_cost)

            if neighbor[0] not in visited:
                visited.add(neighbor[0])
                queue.append(neighbor[0])
    

    if dest not in visited:
        return -1
    else:
        return total_cost'''

def calculate_cost(flights: dict, start: str, dest: str):
    visited = set()
    queue = deque([(start, 0)])  # (current node, current cost)

    while queue:
        current, cost = queue.popleft()

        if current == dest:
            return cost

        for neighbor, price in flights.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, cost + price))

    return -1  # If destination is not reachable


flights = {
    'LAX': [('SFO', 50)],
    'SFO': [('LAX', 50), ('ORD', 100), ('ERW', 210)],
    'ERW': [('SFO', 210), ('ORD', 300)],
    'ORD': [('ERW', 300), ('SFO', 100), ('MIA', 400)],
    'MIA': [('ORD', 400)]
}

print(calculate_cost(flights, 'LAX', 'MIA'))
print(calculate_cost(flights, 'ERW', 'ORD'))