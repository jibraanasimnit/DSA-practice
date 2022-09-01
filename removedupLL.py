from linkedListQues import LinkedList

def removeDups(ll):
    if ll.head is None:
        return
    else:
        curNode = ll.head
        visited = set([curNode.value])
        while curNode.next:
            if curNode.next.value in visited:
                curNode.next = curNode.next.next
            else:
                visited.add(curNode.next.value)
                curNode = curNode.next
        return ll
    
    
def removeDups1(ll):
    if ll.head is None:
        return
    
    currentNode = ll.head
    while currentNode:
        runner = currentNode
        while runner.next:
            if runner.next.value == currentNode.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        currentNode = currentNode.next
    return ll.head

    
    
    
customLL = LinkedList()
customLL.generate(10, 0 ,8)
print(customLL)
removeDups1(customLL)
print(customLL)
                
        
    