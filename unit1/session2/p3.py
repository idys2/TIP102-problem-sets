'''
- input: sorted array of items
- output: same array without duplicates
- 
- iterate through list, if prev == current then remove prev
- 1. empty list -> empty list
'''

def remove_dupes(items):
    if len(items) == 0:
        return items
    
    index = 1
    while index < len(items):
        if items[index] == items[index-1]:
            items.pop(index)
        else:
            index += 1

    return len(items)

items = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
print(remove_dupes(items))

items = ["extract of malt", "haycorns", "honey", "thistle"]
print(remove_dupes(items))
