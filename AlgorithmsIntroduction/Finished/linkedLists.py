class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            
    def print(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
        print("None")
        
linkedList = LinkedList()
linkedList.insertAtBegin(2)
linkedList.insertAtBegin(10)
linkedList.insertAtBegin(5)
linkedList.print()