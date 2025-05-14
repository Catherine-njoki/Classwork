class Node:
    def __init__(self, data):
        self.data = data
        #initialize the pointer
        self.next = None

#create another class
class LinkedList:
    def __init__(self):
        self.head = None

        #create a method
    def insertAtTheBeginning(self, new_data):
        #create a new attribute
        new_node = Node(new_data)
        new_node.next = self.head

        self.head = new_node

    def insertAtTheEnd(self, new_data):
        new_node = Node(new_data)
        if self.head is None: #checking if the head is empty
            self.head = new_node
            return

        last=self.head
        while last.next:
            last=last.next

        last.next=new_node

    #define another method
    def printlinkedlist(self):
        temp =self.head
        while temp:
            print(temp.data,end=' ')
            temp = temp.next
        print()

if __name__ == '__main__':
    llist = LinkedList()
    llist.insertAtTheBeginning("fox")
    llist.insertAtTheBeginning("brown")
    llist.insertAtTheBeginning("quick")
    llist.insertAtTheBeginning("The")
    llist.printlinkedlist()

    llist.insertAtTheEnd("jumped")
    llist.printlinkedlist()
