# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        ahead = behind = dummy

        # Move 'ahead' pointer n+1 steps ahead
        for _ in range(n + 1):
            ahead = ahead.next

        # Move both pointers until 'ahead' reaches the end
        while ahead:
            ahead = ahead.next
            behind = behind.next

        # Skip the n-th node from the end
        behind.next = behind.next.next

        # Return new head
        return dummy.next