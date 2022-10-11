from revision import LinkedList
def removeDups(inputLL):
    if inputLL.head is None:
        return
    else:
        currentNode = inputLL.head
        visited = set([currentNode.value])
        while currentNode.next:
            if currentNode.next.value in visited:
                currentNode.next = currentNode.next.next 
            else:
                visited.add(currentNode.next.value)
                currentNode = currentNode.next
        return inputLL


customLL = LinkedList()
customLL.generate(10, 0 ,99)
print(customLL)
removeDups(customLL)
print(customLL)



    
                
    
    