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
        init_length = self.length_of
        if location < 1 or location > init_length + 1:
            raise ValueError("Invalid location")
        
        
        new_node = Node(value)
        current = self.head
        
        if location == 1:
            new_node.next = self.head
            self.head = new_node
            

        elif location == init_length + 1:
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

    def remove_at(self,location):
        count = 1
        if location < 1 or location > self.length_of():
            raise ValueError("The location specified does not exist")
        
        current = self.head
        
        if location == 1:
           self.head = current.next

        elif location == self.length_of():
            current = self.head
            prev = None
            while current.next:
                prev = current
                current = current.next
                count+=1
            
            "This line checks if we're really reached the last element"
            if count == self.length_of():
                prev.next = None

        else:
            prev = None
            current = self.head
            while count < location:
                prev = current
                current = current.next
            prev.next = current.next
    
    def to_array(self):
        count = 1
        prev = None
        to_array = []
        current = self.head
        while count < self.length_of()+1:
            prev = current
            current = current.next
            to_array.append(prev.get_value())
            count+=1
        return to_array
            




    
