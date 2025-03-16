def find_missing_clues(clues, lower, upper):
    missing_clues = [] 

    if lower == upper:
        if len(clues) == 0:
            return [lower, upper]
        else:
            return missing_clues

    if len(clues) == 1 or upper < lower:
        return missing_clues

    if len(clues) == 0:
        return [lower, upper]

    for i in range(len(clues) - 1):
        if clues[i] + 1 != clues[i + 1]:
            missing_clues.append([clues[i] + 1, clues[i + 1] - 1])

    if clues[-1] + 1 != upper:
        missing_clues.append([clues[-1] + 1, upper])

    return missing_clues

clues = [0, 1, 3, 50, 75]
lower = 0
upper = 99
print(find_missing_clues(clues, lower, upper))

clues = [-1]
lower = -1
upper = -1
print(find_missing_clues(clues, lower, upper))
