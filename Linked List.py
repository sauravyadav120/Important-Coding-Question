'''1 Write code for reversal of linked list'''
# Time Complexity : O(n)
# Space Complexity : O(1)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        print("NULL")
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)
llist.reverse()
print ("\nReversed linked list")
llist.printList()
'''2 - Print the Middle of a given linked list --> Time Complexity: O(n)'''
class Node:
    def __init__(self , data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None

    def push(self , new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data , end  = " ")
            temp = temp.next
        print('NULL')    

    def printmiddle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print('The middle element is', slow.data )

llist = Linkedlist()
llist.push(6)
llist.push(5)                                    
llist.push(4)                                    
llist.push(3)                                    
llist.push(2)                                    
llist.push(1)
llist.printlist()
llist.printmiddle() 

'''3 Detect loop in linked list --Floyd Cycle Detection Algorithm[2-pointer]'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
    def push(self , new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data , end = " ")
            temp = temp.next
        print("NULL")
            
    def detectLoop(self):
        slow = self.head
        fast = self.head
        while(slow and fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
llist = Linkedlist()
llist.push(20)
llist.push(17)
llist.push(15)
llist.push(10) 
llist.head.next.next.next.next = llist.head.next
print ("Loop Found:",llist.detectLoop())