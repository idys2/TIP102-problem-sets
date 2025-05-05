from collections import deque

def get_all_destinations(flights,start):
    queue = deque([start])
    visited = set()
    result = []

    while queue:
        airport = queue.popleft()
        if airport not in visited:
            visited.add(airport)
            result.append(airport)
        for destination in flights.get(airport, []):
            if destination not in visited:
                queue.append(destination)

    return result

flights = {
    "Tokyo": ["Sydney"],
    "Sydney": ["Tokyo", "Beijing"],
    "Beijing": ["Mexico City", "Helsinki"],
    "Helsinki": ["Cairo", "New York"],
    "Cairo": ["Helsinki", "Reykjavik"],
    "Reykjavik": ["Cairo", "New York"],
    "Mexico City": ["Sydney"]   
}

print(get_all_destinations(flights, "Beijing"))
print(get_all_destinations(flights, "Helsinki"))