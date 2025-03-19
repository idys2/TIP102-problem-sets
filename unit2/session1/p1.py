'''
- library_catalog: room name -> num scrolls
- actual_distribution: room name -> num scrolls after rift
- 1. if either input is empty -> return {}
'''

def analyze_library(library_catalog, actual_distribution):
    result = {}

    if not library_catalog or not actual_distribution:
        return result

    for key in library_catalog.keys():
        if key in actual_distribution:
            result[key] = actual_distribution[key] - library_catalog[key]
        else:
            result[key] = -library_catalog[key]

    return result

library_catalog = {
    "Room A": 150,
    "Room B": 200,
    "Room C": 250,
    "Room D": 300
}

actual_distribution = {
    "Room A": 150,
    "Room B": 190,
    "Room C": 260,
    "Room D": 300
}

print(analyze_library(library_catalog, actual_distribution))