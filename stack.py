class Stack:
    def __init__(self):
        self.list = []
    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    
    
    def isEmpty(self):
        if self.list == []:
            return True  
        else:
            return False
    def push(self, value):
        self.list.append(value)
        return "the element has been successfully pushed"
    def pop(self):
        if self.isEmpty():
            return "no element to be popped"
        else:
            return self.list.pop()
    def peek(self):
        if self.isEmpty():
            return "nothing to peek"
        else:
            return self.list[len(self.list)-1]
    def delete(self):
        self.list = None
        
    
customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack.peek())


    
    
    