class Stack:
    def __init__(self):
        self.top = None
        self.stack = []

    def push(self,value):
        self.stack.append(value)
        self.top = self.stack[-1]

    def peek(self):
        if not self.isempty:
            return self.top
        return "List is empty."
    
    def pop(self):
        if not self.isempty():
            popped_value = self.stack.pop()
            if not self.isempty():
                self.top = self.stack[-1]
            else:
                self.top = None
            return popped_value

        return "Stack contains no elements."
    
    def isempty(self):
        current = self.top
        if current:
            return not bool(self.stack)
        return bool(self.stack)
    
    