def final_value_after_operations(operations):
    tigger = 1
    for i in range(len(operations)):
        if operations[i] == "bouncy" or operations[i] == "flouncy":
            tigger += 1
        elif operations[i] == "trouncy" or operations[i] == "pouncy":
            tigger -= 1
    return tigger

operations = ["trouncy", "flouncy", "flouncy"]
final_value_after_operations(operations)

operations = ["bouncy", "bouncy", "flouncy"]
final_value_after_operations(operations)
