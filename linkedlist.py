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
    
    def add_new(self,value):
        new_node = Node(value)
        current = self.head
        prev = None
        if current:
            while current.next:
                prev = current
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def length_of(self):
        current = self.head
        if current:
            list_length = 1
            while current.next:
                list_length += 1
                prev = current
                current = current.next
            return list_length

    def index_of(self,value):
        current = self.head
        index = 0
        while current:
            if current.get_value == value:
                return index
            current = current.next
            index += 1
        return -1
    
    def insert_at(self,value,location):
        if location < 1 or location > self.length_of() + 1:
            raise ValueError("Invalid location")
        
        
        new_node = Node(value)
        current = self.head
        if location == 1:
            new_node.next = self.head
            self.head = new_node

        elif location == self.length_of() + 1:
            self.add_new(value)

        else:
            prev = None
            count = 1
            while count < location:
                prev = current
                current = current.next
                count += 1
            prev.next = new_node
            new_node.next = current
    
