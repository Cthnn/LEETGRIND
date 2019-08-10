class ListNode:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next


class LinkedList:
    def __init__(self, arr=None):
        self.head = None
        self.tail = None
        self.appendList(arr)

    def append(self, newNode):
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = self.tail.next

    def appendList(self, list):
        for num in list:
            self.append(ListNode(num))

    def printList(self):
        curr = self.head
        print('head', end='->')
        while curr:
            print(curr.val, end='->')
            curr = curr.next
        print('None')
