class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse_list(head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    if head is None or head.next is None:
        return head

    curr = head
    prev = None
    next = None

    while curr != None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev

def print_ll(head):
    ptr = head
    while ptr is not None:
        print (ptr.value, end=", ")
        ptr = ptr.next

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

print()
print_ll(head)
print()
head = reverse_list(head)
print()
print_ll(head)
print()
