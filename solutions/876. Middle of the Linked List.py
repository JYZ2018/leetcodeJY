# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n=0
        dummy1,dummy2=head,head
        while dummy1:
            n+=1
            dummy1=dummy1.next
        mid=n//2
        for i in range(mid):
            dummy2=dummy2.next
        return dummy2
            
        
        
