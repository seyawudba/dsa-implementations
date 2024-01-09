class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.queue = []

    def addnew(self,value):
        self.queue.append(value)
        if len(self.queue) == 1:
            self.first = self.last = value
        else:
            self.last = self.queue[-1]


    def removefrom(self):
        status = self.isempty()
        if status:
            return "The queue is empty"
        
        popped_value = self.queue.pop(0)
        
        if not status:
            self.first = self.queue[0]
        else:
            pass
        return popped_value
    
    def lengthof(self):
        if self.queue:
            return len(self.queue)
        return "Empty queue."
    
    def isempty(self):
        status = bool(self.queue)
        if status:
            return not status
        return status
    
    
    def __repr__(self):
        return f'{self.queue}'
