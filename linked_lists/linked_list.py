class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

def print_ll(head):
    ptr = head
    while ptr is not None:
        print(ptr.value, end=", ")
        ptr = ptr.next

def create_linked_list():
    head = Node(-1)
    ptr = head

    while True:
        data = int(input())
        if data == -1:
            break
        new_node = Node(data)
        ptr.next = new_node
        ptr = ptr.next

    return head.next

def create_default_ll():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    return head

def count_nodes(head):
    ptr = head
    count = 0
    while ptr is not None:
        ptr = ptr.next
        count += 1

    return count

def find_index_of(head, k):
    ptr = head
    i = 0

    while ptr is not None:
        if ptr.value == k:
            return i
        i += 1
        ptr = ptr.next

def insert_at_front(head : Node, k : int) -> Node:
    new_node = Node(k)
    new_node.next = head
    return new_node

def insert_at_end(head, k):
    new_node = Node(k)
    if head is None:
        return new_node

    ptr = head
    while ptr.next is not None:
        ptr = ptr.next

    ptr.next = new_node

    return head

def insert_at_n(head, n, k):
    new_node = Node(k)
    if n == 1:
        new_node.next = head
        return new_node

    i = 1
    ptr = head

    while ptr.next is not None:
        if i >= n - 1:
            break
        i += 1
        ptr = ptr.next

    save = ptr.next
    ptr.next = new_node
    new_node.next = save

    return head

def delete_first(head):
    head = head.next
    return head

def delete_last(head):
    if head is None or head.next is None:
        return None
    ptr = head
    while ptr.next.next is not None:
        ptr = ptr.next

    ptr.next = None
    return head

head = create_default_ll()
print(count_nodes(head))
print_ll(head)
print()
print(find_index_of(head, 3))

head = insert_at_front(head, 100)
print_ll(head)

print()
head = insert_at_end(head, 100)
print_ll(head)

print()
head = insert_at_n(head, 2, 200)
head = insert_at_n(head, 4, 300)
head = insert_at_n(head, 9, 300)
print_ll(head)

print()
head = delete_first(head)
print_ll(head)

print()
head = delete_last(head)
print_ll(head)

