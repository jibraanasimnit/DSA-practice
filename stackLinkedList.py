class Node:
    def __init__(self):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        
class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()
    def isEmpty(self):
        if self.LinkedList.head == None:
            return "True"
        else:
            return "false"
    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node
        