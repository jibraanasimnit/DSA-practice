from more_itertools import tail
from revision import LinkedList

def nthToLast(inputLL, n):
    pointer1 = inputLL.head
    pointer2 = inputLL.head
    for i in range(n):
        if pointer2 is None:   
            return None
        else:
            pointer2 = pointer2.next  
    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1

customLL = LinkedList()
customLL.generate(10, 0 ,10)
print(customLL)
print(nthToLast(customLL, 10))