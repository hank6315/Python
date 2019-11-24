from stack import Stack

'''
Input: "()"
Output: true

Input: "()[]{}"
Output: true

Input: "([)]"
Output: false

'''

def is_paren_balanced(paren_string):
    stack = ['S']
    m = {'}' : '{' , ')' : '(', ']' : '['}

    for char in paren_string:
        if char in m.keys():
            if stack.pop() != m[char]:
                return False
        else :
            stack.append(char)
            

    return len(stack) == 1


print(is_paren_balanced("()[]{}"))
print(is_paren_balanced("([)]"))