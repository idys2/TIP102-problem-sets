'''
input: list
output: number of "layers" in a list
'''

def count_layers(sandwich):
    if len(sandwich) == 1:
        return 1
    else:
        return 1 + count_layers(sandwich[1])

sandwich1 = ["bread", ["lettuce", ["tomato", ["bread"]]]]
sandwich2 = ["bread", ["cheese", ["ham", ["mustard", ["bread"]]]]]

print(count_layers(sandwich1))
print(count_layers(sandwich2))