class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
        

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        curr = self.head.next
        while curr != self.tail and index > 0:
            curr = curr.next
            index -= 1
        if curr != self.tail and index == 0: ### Edge Case: Tail Dummy Node
            return curr.val
        else:
            return -1
        

    def addAtHead(self, val: int) -> None:
        # new_node = ListNode(val)
        # new_node.next = self.head.next
        # new_node.prev = self.head
        # self.head.next.prev = new_node
        # self.head.next = new_node

        new_node = ListNode(val)
        node_0 = self.head
        node_1 = self.head.next

        new_node.next = node_1
        new_node.prev = node_0
        node_1.prev = new_node
        node_0.next = new_node
        

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        node_tail = self.tail
        node_last = self.tail.prev

        new_node.next = node_tail
        new_node.prev = node_last
        node_tail.prev = new_node
        node_last.next = new_node


    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head.next

        while curr != self.tail and index > 0:
            curr = curr.next
            index -= 1
        
        if index == 0: 
            new_node = ListNode(val)
            node_0 = curr.prev
            node_1 = curr

            new_node.next = node_1
            new_node.prev = node_0
            node_1.prev = new_node
            node_0.next = new_node
            
        else:
            pass

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head.next

        while curr != self.tail and index > 0:
            curr = curr.next
            index -= 1
        
        if curr != self.tail and index == 0: 
            prev_node = curr.prev
            next_node = curr.next

            prev_node.next = next_node
            next_node.prev = prev_node
        else:
            pass


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)