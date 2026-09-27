class LinkedList:
    class Node:
        def __init__(self, data, next):
            self.data = data
            self.next = next
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        i = 0
        curr = self.head
        while curr:
            if i is index:
                return curr.data
            curr = curr.next
            i += 1
        return -1
        
    def insertHead(self, val: int) -> None:
        # Check if there is a head node, list is empty, make head and tail newNode
        # Head exists, create new node, set next to head, set head to new node
        newNode = self.Node(val, None)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        

    def insertTail(self, val: int) -> None:
        newTail = self.Node(val, None)
        if self.tail is None:
            self.tail = newTail
            self.head = newTail
        else:
            self.tail.next = newTail
            self.tail = newTail
        

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        prev = None
       
        while curr:
            if i == index:
                if not prev:
                    # Remove head
                    self.head = curr.next
                    if not self.head:
                        self.tail = None
                else:
                    prev.next = curr.next
                    if curr == self.tail:
                        self.tail = prev
                return True
            prev = curr
            curr = curr.next
            i += 1
        return False
            

    def getValues(self) -> List[int]:
        arr = []
        curr = self.head
        while curr:
            arr.append(curr.data)
            curr = curr.next
        return arr
        
