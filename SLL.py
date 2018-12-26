
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head=None

##Pushing the data to the beginning of the Linked List##
    def push(self,data):
        newNode = Node(data)
        if(self.head==None):
            self.head = newNode
            #print("Pushed a node")
        else:
            newNode.next = self.head
            self.head = newNode

##Adding a new data to the end of the Linked List##
    def append(self,data):
        newNode = Node(data)
        curr = self.head
        while(curr.next!=None):
            curr = curr.next
        curr.next = newNode

##Insert the data after a given node##
    def insertAfter(self,key,data):
        #print(key,data)
        newNode = Node(data)
        curr = self.head
        while(curr!=None):
            if(curr.val==key):
         #       print(curr.val)
                newNode.next = curr.next
                curr.next = newNode
                break
            curr = curr.next
        if(curr==None):
            print("Node with the key %s is not found" % key)

##Insert the data before a given node##
    def insertBefore(self,key,data):
        newNode = Node(data)
        curr = self.head
        while(curr.next!=None and curr.next.val!=key):
            curr = curr.next
        if(curr.next==None and curr.val!=key):
            print("Node with the key %s is not found" % key)
        else:
            newNode.next = curr.next
            curr.next = newNode

##Delete the head node - Pop operation##
    def pop(self):
        curr = self.head
        if(curr==None):
            return None
        else:
            data = curr.val
            self.head = curr.next
            curr.next = None
            return data
                
##Delete a node with a given value##
    def delValue(self,key):
        if(self.head==None):
            print("Empty linked list")
            return
        curr = self.head
        while(curr.next!=None and curr.next.val!=key):
            curr = curr.next
        if(curr.next==None):
            print("Key %s not found in the Linked List" % key)
            return
        curr.next = curr.next.next

##Delete a node by its position##
    def delNode(self,pos):
        if(self.head==None):
            print("Empty Linked List")
            return
        if(pos==1):
            self.head = self.head.next
            return
        curPos = 1
        curr = self.head.next
        while(curr!=None):
            curPos+=1
            if(curPos==pos):
                prev.next = curr.next
                return
            else:
                prev = curr
                curr = curr.next
        if(curr==None):
            print("Position exceeds the total length of the Linked List")
            return

##Reverse the Linked List##
    def reverseList(self):
        if(self.head==None or self.head.next==None):
            print("Linked List is either empty or too few items to reverse")
            return
        curr = self.head
        prev = None
        while(curr.next!=None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        curr.next = prev
        self.head = curr
            
##Printing the contents of the Linked List##
    def printList(self):
        curr = self.head
        if(curr==None):
            print("Linked List is empty")
            return
        while(curr!=None):
            print(curr.val)
            curr = curr.next



