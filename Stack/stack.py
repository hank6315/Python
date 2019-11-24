class Stack():
    def __init__(self):
        self.item = []

    def push(self , data):
        self.item.append(data)

    def pop(self):
        return self.item.pop()

    def get_stack(self):
        return self.item

    def is_empty(self):
        return self.item == []

    def peek(self):
        if not self.is_empty():
            return self.item[-1]

    

'''
s = Stack()

s.push(5)
s.push(4)
s.push(3)
s.push(2)

print(s.get_stack())

s.pop()

print(s.get_stack())

print(s.peek())
'''