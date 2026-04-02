class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1) # Dummy Node
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1 # Index out of bounds

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next # Link new node to the current head's next (to account for the dummy) INSERT NODE AT HEAD
        self.head.next = new_node # Update head's next to point to the new node (to account for the dummy) 
        # FROM dummy_head -> 1 -> 2 -> 3 -> None (and wanting to add 0)
        # TO dummy_head -> 0 -> 1 -> 2 -> 3 -> None
        
        # If the list was empty (i.e., tail is the dummy node), update the tail
        if not new_node.next:
            self.tail = new_node
        # FROM dummy_head -> None
        # TO dummy_head -> 10 -> None        

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val) # Creating the New Node
        self.tail.next = new_node # Linking the New Node to the Current Tail
        self.tail = self.tail.next # Updating the Tail Pointer
        

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while i < index and curr: # the "and curr" is to ensure it is not out of bounds
            # Move curr to the node before target node
            i += 1
            curr = curr.next

        if curr and curr.next:
            if curr.next == self.tail:
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

        
