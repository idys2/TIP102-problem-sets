'''
- input: string of C's and D's
- output: winning group

- two queues, one for C's and one for D's
- enqueue index of C/D into queue
'''
from collections import deque
def predictAdoption_victory(votes):
    cats = deque()
    dogs = deque()
    n = len(votes)

    # enqueue index of C/D into respective queue
    for i in range(n):
        if votes[i] == 'C':
            cats.append(i)
        else:
            dogs.append(i)

    # The front of each queue "fight", and the winner (lower index) "stays"
    # by being appended to the end
    winner_index = n
    while cats and dogs:
        if cats[0] < dogs[0]:
            cats.append(winner_index)
        else:
            dogs.append(winner_index)

        cats.popleft()
        dogs.popleft()
        winner_index += 1
    
    return "Cat Lovers" if cats else "Dog Lovers"

print(predictAdoption_victory("CD"))        # Cat Lovers
print(predictAdoption_victory("CDD"))       # Dog Lovers
print(predictAdoption_victory("CDDC"))      # Cat Lovers
print(predictAdoption_victory("CCDDC"))     # Cat Lovers
print(predictAdoption_victory("DDCCDC"))    # Dog Lovers 