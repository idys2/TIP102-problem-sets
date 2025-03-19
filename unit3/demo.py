'''
- input: string containing parenthesis
- output: true if all parentheses match, false o/w

edge cases
- empty string -> return false
- starts with ')' -> return false
'''

def p(s: str):
    if not s:
        return False
    
    stack = []

    for c in s:
        # normal case 1: got '('
        if c == '(':
            stack.append(c)

        else:
            # edge case: got ')' but stack is empty, so can't match this parenthesis
            if not stack:
                return False
            
            # normal case 2: got ')' and matching '(' in stack
            stack.pop()
            
    return True if not stack else False

print(p("()()()"))      # True
print(p(""))            # False
print(p(")()"))         # False
print(p("((())"))       # False
print(p("((())())"))    # True