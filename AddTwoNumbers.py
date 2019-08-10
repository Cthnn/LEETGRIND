from LinkedList import *


def addTwoNumbers(l1, l2, c=0):
    val = l1.val + l2.val + c
    c = val // 10
    ret = ListNode(val % 10)

    if (l1.next != None or l2.next != None or c != 0):
        if l1.next == None:
            l1.next = ListNode(0)
        if l2.next == None:
            l2.next = ListNode(0)
        ret.next = addTwoNumbers(l1.next, l2.next, c)
    return ret


if __name__ == '__main__':
    l1 = LinkedList([1, 2, 3, 4, 5])
    l2 = LinkedList([4, 5, 6, 7, ])

    l1.printList()
    l2.printList()

    result = addTwoNumbers(l1.head, l2.head)
    curr = result
    while curr:
        print(curr.val)
        curr = curr.next
