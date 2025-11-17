# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        

        # 1) Find middle (slow/fast pointers)
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # After this loop: slow is at middle (end of first half)
        # Split second half from slow.next
        second = slow.next
        slow.next = None  # end first half

        # 2) Reverse second half
        prev = None
        curr = second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # prev now is head of reversed second half

        # 3) Merge first half and reversed second half
        first, second = head, prev
        while second:
            # store next pointers
            tmp1 = first.next
            tmp2 = second.next

            # weave
            first.next = second
            second.next = tmp1

            # move pointers
            first = tmp1
            second = tmp2
