from stack import Stack


def reverse_string(stack , input_str):
    
    #loop through the string and push contents
    #char by char onto stack

    for i in range(len(input_str)):
        stack.push(input_str[i])
    
    rev_str = ""
    while not stack.is_empty():
        rev_str += stack.pop()
    
    return rev_str



input_str = "Hello"
s = Stack()
print(reverse_string(s , input_str))
