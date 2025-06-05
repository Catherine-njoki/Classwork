class CircularListNode:
    def __init__(self,value):
        self.value =value
        self.next_node = None
        self.previous_node = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.start_node = None
    def insert_at_end(self,value):
        new_node = CircularListNode(value)

        if self.start_node is None:
            new_node.next_node =new_node
            new_node.previous_node=new_node
            self.start_node = new_node

        else:
            last_node = self.start_node.previous_node
            last_node.next_node = new_node
            new_node.previous_node = last_node
            new_node.next_node = self.start_node
            self.start_node.previous_node = new_node

    def insert_at_beginning(self,value):
        self.insert_at_end(value)
        self.start_node = self.start_node.previous_node

    def remove_by_value(self,value):
        if self.start_node is None:
            print("The list is empty.Cannot remove any node")
            return

        current_node = self.start_node
        while True:
            if
