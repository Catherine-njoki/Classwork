from Singlylinkedlist2 import LinkedList


class CircularQueue:
    DEFAULT_CAPACITY = 10


    def __init__(self):
        self._data = [None] * CircularQueue.DEFAULT_CAPACITY #this method is a list
        self._size = 0
        self._front = 0

    # def __len__(self):
    #     return self._size
    # #this gives the size of the array

    def isEmpty(self):
        return self._size ==0

    def first(self):
        if self.isEmpty():
            return Empty("Queue is empty")#this line exits this method
        return self._data[self._front]#if the list is not empty
   # students =["Mary","John","Doe"]
    #students[0]#this one accesses Mary
    #create a dequeued element below
        dequeued_element = self._data[self._front]
        #lets do some garbage collection
        self._data[self._front] = None
        #decrease queue by one
        self._front -= 1




    def dequeue(self):#primary operation you can conduct on a queue
        if self.isEmpty():
            raise Empty("Queue is empty for dequeue operation")
        #raise and return have the same weight of function idk
        #lets conduct a dequeue operation
        front= (self._front + 1) % len(self._data)
        dequeued_element = self._data[front]
        self._data[self._front] = None
        self._size -=1
        return dequeued_element


    def enqueue(self, element):#primary operation you can conduct on a queue
        #before you enqueue check if the list is full by comparing the size of way the data was defined with the size
        if self._size ==len(self._data):
            self._resize(2* len (self._data))            #we are calling it
        tail = (self._front + self._size) % len(self._data)
        #gabage collection ,ensures there is no wasted memory
        self._data[tail] = element
        self._size = self._size + 1


    def resize(self, new_capacity):
        ...

class Empty(Exception):
    pass
if __name__ == '__main__':
    object_queue = CircularQueue()

    insert_elements=[11,22,33,44,55]

for element in insert_elements:
    object_queue.enqueue(element)
    print(f"Added element: {element}")
    #print(f"The new size of the queue:{len(object_queue)}")#every time I add an element it returns the size
    #print("\n Current Queue representation
    print(f"The front element of the queue:{object_queue._size}")