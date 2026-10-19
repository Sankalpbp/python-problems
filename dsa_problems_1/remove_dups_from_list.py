# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def delete_duplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        ptr = head.next
        preptr = head

        while ptr is not None:
            if preptr.val == ptr.val:
                preptr.next = ptr.next
                ptr = ptr.next
            else:
                preptr = ptr
                ptr = ptr.next

        return head