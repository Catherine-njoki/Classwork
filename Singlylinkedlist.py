
#from syntable import Class

class SinglyLinkedList:
     def __init__(self,value,nextnode=None):#creating attributes
         self.value = value
         self.nextnode = nextnode


     #instantiate the object
snode1 = SinglyLinkedList("1")
snode2 = SinglyLinkedList("2")
snode3 = SinglyLinkedList("3")
snode4 = SinglyLinkedList("4")

#use pointers to link them ,at the end it will be automtically pointed to None
snode1.nextnode=snode2 #this pointer is holding node2
snode2.nextnode=snode3
snode3.nextnode=snode4

currentNode = snode1
while True:
    print(currentNode.value,">>>",end=' ')

    if currentNode.nextnode is None:
        print("None")
        break

    currentNode = currentNode.nextnode #inreamenting
