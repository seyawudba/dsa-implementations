class Node:
    def __init__(self,value):
        "Initializing a node class with a value and the next field set to none."
        self.value = value
        self.next = None
    
    def get_value(self):
        return self.value
    
    def set_value(self,new_value):
        self.value = new_value

    def __repr__(self):
        return f"{self.value}"
    

class LinkedList:
    node = Node(None)
    def __init__(self,head=None):
        """A linkedlist can be defined empty in the initial stage"""
        self.head = head