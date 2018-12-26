from SLL import *

List = LinkedList()

##Inserting Operations##
List.push(5)    ##5->NULL
List.push(3)    ##3->5->NULL
List.push(10)   ##10->3->5->NULL
List.append(1)  ##10->3->5->1->NULL
List.append(4)  ##10->3->5->1->4->NULL
List.insertAfter(3,2)  ##10->3->2->5->1->4->NULL
List.insertAfter(15,10)
List.insertBefore(5,6)  ##10->3->2->6->5->1->4->NULL
List.insertBefore(12,13)

##Deleting Operations##
topElement = List.pop()   ##3->2->6->5->1->4->NULL
if(topElement==None):
    print("There is no item in the Linked List")
else:
    print("The top element in the Linked List is ", topElement)
#List.printList()
List.delValue(2)     ##3->6->5->1->4->NULL
#List.printList()
List.delValue(15)
List.delNode(1)      ##6->5->1->4->NULL
List.delNode(3)      ##6->5->4->NULL

##Printing the Linked List##
List.printList()

##Reverse the Linked List##
List.reverseList()    ##4->5->6->NULL
List.printList()
