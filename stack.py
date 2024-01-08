class Stack:
    def __init__(self):
        self.top = None
        self.stack = []
    def push(self,value):
        self.stack.append(value)
        self.top = self.stack[-1]
    
    