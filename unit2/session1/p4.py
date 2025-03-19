'''
inputs
- portals: number strings
- destination: number string

edge case: empty -> return 0

- generate all combinations of concatenated strings
- nested for loop
- note: (i,j) and (j,i) are different


'''
from collections import Counter
def num_of_time_portals(portals, destination):
    result = 0

    for i in range(len(portals)):
        for j in range(i+1, len(portals)):
            
            if portals[i] + portals[j] == destination:
                result += 1
            
            if portals[j] + portals[i] == destination:
                result += 1
    
    hm = Counter(portals)

    for key, value in hm.items():
        # iterate over keys list
        pass

    return result

portals0 = ["777", "777", "7"] # 4
destination0 = "7777"
portals1 = ["777", "7", "77", "77"]
destination1 = "7777"
portals2 = ["123", "4", "12", "34"]
destination2 = "1234"
portals3 = ["1", "1", "1"]
destination3 = "11"
print(num_of_time_portals(portals0, destination0)) # 4
print(num_of_time_portals(portals1, destination1))
print(num_of_time_portals(portals2, destination2))
print(num_of_time_portals(portals3, destination3))
