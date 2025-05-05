'''
input: adjacency list
output: minimum number of edges to connect every node with each other

- similar to no. islands problem
- no. islands - 1
'''
from collections import deque

'''
returns minumum number of edges that need to be added such that there is a path
from each node to all other nodes
'''
def min_flights_to_expand(flights: dict):
    visited = set()
    queue = deque()
    num_edges = 0

    for node in flights:
        if node not in visited:
            queue.append(node)
            visited.add(node)

            while queue:
                current = queue.popleft()

                for neighbor in flights[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

            num_edges += 1

    return num_edges - 1  # Subtract 1 to get the number of edges needed


flights = {
    'JFK': ['LAX', 'SFO'],
    'LAX': ['JFK', 'SFO'],
    'SFO': ['JFK', 'LAX'],
    'ORD': ['ATL'],
    'ATL': ['ORD'],
    'MIA': ['ERW'],
    'ERW': ['MIA']
}

print(min_flights_to_expand(flights))