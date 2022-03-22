# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
​
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # two pointer
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
        if not fast or not fast.next:
            return None
        #print(fast)
        slow=head
        while slow:
            
            if slow==fast:
                return slow
            slow=slow.next
            fast=fast.next
        
        # elegant hash map method
        # s=set()
        # while head:
        #     if head in s:
        #         return head
        #     s.add(head)
        #     head=head.next
        
        
        
        # use dictionary
        # d={}
