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

    #to delete we will reassign the second node as the new end
    def deleteFromEnd(self):
        if self.head is None:
            return"list is empty"
        if self.head.next is None:
            self.head = None
            return

        #make a temporary variable
        temp=self.head
        while temp.next: #while arriving to the second last node
            temp=temp.next 

    def deleteFromBeginning(self):
        if self.head is None:
            return "list is empty"
        self.head=self.head.next #self.head will be 'The' the next pointer is holding quick, so the quick is set as the new head
        #this is possible because the pointer has data quick,when calling the head for the next node


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

    llist.deleteFromBeginning()
    llist.printlinkedlist()

    #llist.deleteFromEnd()
    #llist.printlinkedlist()

    llist.insertAtTheBeginning("A")
    llist.printlinkedlist()