class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        # Edge case OOB Linked List
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.value
            i += 1
            curr = curr.next
        return -1
        

    def insertHead(self, val: int) -> None:
        # Edge case: Inserting into Empty List
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if new_node.next is None:
            self.tail = new_node


    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        self.tail.next = new_node
        self.tail = new_node


    def remove(self, index: int) -> bool:
        # Edge Case: We are deleting the last Node
        curr = self.head
        i = 0
        while curr and i < index:
            i += 1
            curr = curr.next

        if curr and curr.next:
            if self.tail == curr.next:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False
            




    def getValues(self) -> List[int]:
        output = []
        curr = self.head.next
        while curr:
            output.append(curr.value)
            curr = curr.next
        return output