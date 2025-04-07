'''
input: string delimited with spaces
output: new string with orders reversed

q: input validation

iteratively:
- push each string onto stack
- pop from stack

recursively:
- recurse to the last word, then append each word back up
- base case: orders list size is 1: return the word
- recurive case: size > 1: return helper(orders_list[::-1])

helper(Bagel Sandwich Coffee)
helper(Bagel Sandwich)
helper(Bagel) -> Bagel

res = helper(Bagel Sandwich Coffee) + helper(Bagel Sandwich) + helper(Bagel)

res = Coffee + helper(Bagel Sandwich)
res = Coffee + Sandwich + helper(Bagel)
res = Coffee + Sandwich + Bagel
'''

def reverse_orders_helper(orders_list):
    if len(orders_list) > 0:
        return orders_list.pop() + " " + reverse_orders_helper(orders_list)
    return ""

def reverse_orders(orders):
    # O(n) space, can be optimized with find()
    orders_list = orders.split(" ") # O(n) time

    # O(n) recursive calls
    return reverse_orders_helper(orders_list) # build string here

print(reverse_orders(""))
print(reverse_orders("Bagel"))
print(reverse_orders("Bagel Sandwich Coffee"))