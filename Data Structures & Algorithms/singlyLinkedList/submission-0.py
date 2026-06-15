class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def get(self, i):

        curr = self.head
        idx = 0

        while curr:

            if idx == i:
                return curr.val

            curr = curr.next
            idx += 1

        return -1

    def insertHead(self, val):

        newNode = ListNode(val)

        newNode.next = self.head

        self.head = newNode

    def insertTail(self, val):

        newNode = ListNode(val)

        if self.head is None:
            self.head = newNode
            return

        curr = self.head

        while curr.next:
            curr = curr.next

        curr.next = newNode

    def remove(self, i):

        if self.head is None:
            return False

        if i == 0:
            self.head = self.head.next
            return True

        curr = self.head
        idx = 0

        while curr and idx < i - 1:
            curr = curr.next
            idx += 1

        if curr is None or curr.next is None:
            return False

        curr.next = curr.next.next

        return True

    def getValues(self):

        result = []

        curr = self.head

        while curr:
            result.append(curr.val)
            curr = curr.next

        return result
