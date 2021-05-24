class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

        #adds a node to the end of the list
        def push(<Node> node):
            temp = self.head
            while (temp):
                temp = temp.next
            temp.next = node
            self.length += 1
            #self.tail = node

        #removes the last node and returns the data
        def pop():
            temp = self.head
            while(temp):
                if temp.next == None:
                    result = temp.data
                    temp = None
                temp = temp.next
                self.length -= 1
            return result
            #result = self.tail.data
            #self.tail = None
        
        #adds a single node containing data to a chosen location
        #if the index is above the sixe of the list, do nothing
        def insert(uint index, node):
            if uint index > self.size:
                return
            #add at the back
            if uint index == self.size:
                push(node)
            #add at the front
            if uint index = 0:
                temp = self.head
                self.head.next = temp
                self.head = node

            #add in the middle   
            i = 0
            temp = self.head
            while (i < uint index):
                temp2 = temp.next
                i += 1
            node.next = temp2

        #remove a node at the index location in the list
        def remove(uint index):
            pass
        
        #returns a pointer to the node at the index location in the list
        #returns null if the node doesn't exist
        def elementAt(uint index):
            pass

        ##returns the length of the list
        def size():
            return self.size
        
        #returns a string representation of the linked list
        def printList():
            temp = self.head
            while (temp):
                print(temp.data)
                temp = temp.next

#reversing a Linked List
            
        
        
                      
            
            
            

        
            
    
