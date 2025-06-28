class CircularListNode:
    def __init__(self,value):
        self.value = value
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
            if current_node.value == value:
                if current_node.next_node == current_node:
                    self.start_node = None
                else:
                    current_node.previous_node.next_node = current_node.next_node
                    current_node.next_node.previous_node = current_node.previous_node
                    if current_node == self.start_node:
                        self.start_node = current_node.next_node
                print(f"Removed: {value}")
                return
            current_node = current_node.next_node
            if current_node == self.start_node:
                print(f" Value {value} not found in the list.")
                break
    def show_list_forward(self):
            if self.start_node is None:
                print("The list is empty")
                return

            current_node = self.start_node
            value_list = []
            while True:
                value_list.append(
                    str(current_node.value))
                current_node = current_node.next_node
                if current_node == self.start_node:
                    break
            output_string="->".join(value_list)
            print(output_string)
    def show_list_backward(self):
            if self.start_node is None:
                print("The list is empty.")
                return
            last_node = self.start_node.previous_node
            current_node = last_node
            value_list = []
            while True:
                value_list.append(str(current_node.value))
                current_node = current_node.previous_node
                if current_node == last_node:
                    break

            output_string = "<-".join(value_list)
            print(output_string)
if __name__ == "__main__":
    my_circular_list = CircularDoublyLinkedList()
    my_circular_list.insert_at_end("Quick")
    my_circular_list.insert_at_end("Brown")
    my_circular_list.insert_at_end("Fox")

    print("\nList after inserting at the end:")
    my_circular_list.show_list_forward()
    my_circular_list.insert_at_beginning("The")
    print("\nList after inserting at the beginning:")
    my_circular_list.show_list_forward()

    print("\nList displayed backward:")
    my_circular_list.show_list_backward()

    my_circular_list.remove_by_value("Quick")
    print("\nList after removing Quick:")
    my_circular_list.show_list_forward()

    my_circular_list.remove_by_value("Quick") 
    my_circular_list.remove_by_value("Slow") 
    my_circular_list.remove_by_value("Brown")
    print("\nList after removing Brown:")
    my_circular_list.show_list_forward()

    
    my_circular_list.remove_by_value("The")
    my_circular_list.remove_by_value("Fox")
    print("\nList after removing all:")
    my_circular_list.show_list_forward()

    




    
       


















                    
     
                
















            
