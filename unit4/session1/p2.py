'''
input: brands
output: dict of counts of the materials found in each brand

- iterate over each list of materials in each brand
- create dictionary of counts

time: O(nm)
space: O(m)

alternate solution: combine all materials lists into one
- return Counter of that list
'''
from collections import Counter
def count_material_usage(brands):
    # alternate solution
    return dict(Counter([material for brand in brands for material in brand["materials"]]))

    # regular solution
    res = {}
    for brand in brands:
        for material in brand["materials"]:
            if material not in res.keys():
                res[material] = 1
            else:
                res[material] += 1
    
    return res

brands = [
    {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
    {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
    {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]}
]

brands_2 = [
    {"name": "NatureWear", "materials": ["hemp", "linen"]},
    {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
    {"name": "GreenFit", "materials": ["linen", "recycled wool"]}
]

brands_3 = [
    {"name": "OrganicThreads", "materials": ["organic cotton"]},
    {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
    {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]}
]

print(count_material_usage(brands))
print(count_material_usage(brands_2))
print(count_material_usage(brands_3))