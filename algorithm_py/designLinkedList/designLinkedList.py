class ListNode:
    
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0

        while curr and i<index:
            curr = curr.next
            i+=1
        if curr and curr!=self.tail:
            return curr.val
        return -1       

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        new_node.prev = self.head
        self.head.next.prev = new_node
        self.head.next = new_node        

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.tail
        new_node.prev = self.tail.prev
        self.tail.prev.next = new_node
        self.tail.prev = new_node    
        

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head.next
        i=0
        while curr and i<index:
            curr = curr.next
            i+=1
        if curr:
            new_node = ListNode(val)
            new_node.next = curr
            new_node.prev = curr.prev
            curr.prev.next = new_node
            curr.prev = new_node
        
    def deleteAtIndex(self, index: int) -> None:
        curr = self.head.next
        i=0
        while curr and i<index:
            curr = curr.next
            i+=1
        if curr and curr != self.tail:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev