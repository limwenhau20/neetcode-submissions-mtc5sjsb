class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1) #Dummy Node
        self.tail = self.head

    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1 #Index OOB

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next #assign the next first for new_node, before setting the new_node into head
        self.head.next = new_node
        if not new_node.next: #Edge Case 1: If List is Originally Empty
            self.tail = new_node


    def insertTail(self, val: int) -> None:
        # 2 cases 
        # Case 1: Tail is Empty; Case 2: Tail is not empty
        self.tail.next = ListNode(val) #assign the tail.next first, before setting the actual tail
        self.tail = self.tail.next


    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head # Cannot use head.next, because we need the Node before the one that's getting deleted (will incl Dummy)
        while i < index and curr:
            i += 1
            curr = curr.next
        
        if curr and curr.next:
            if curr.next == self.tail: # Edge Case 1: Delete the last Node
                self.tail = curr
            curr.next = curr.next.next
            return True
        
        return False


    def getValues(self) -> List[int]:
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
