#Linked List Insertion Method for a Printable Linked List


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    def appendLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index = index + 1
                nextNode = tempNode.next
                tempNode = newNode
                newNode.next = nextNode
                




linkedList = SLinkedList()
linkedList.appendLL(1,1)
linkedList.appendLL(2,1)
linkedList.appendLL(3,1)
linkedList.appendLL(4,1)
print([node.value for node in linkedList])


    



            
    