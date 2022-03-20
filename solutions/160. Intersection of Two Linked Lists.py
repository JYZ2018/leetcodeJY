# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
​
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
       
        dummyA=headA
        dummyB=headB
        while dummyA is not dummyB:
            dummyA=dummyA.next if dummyA else headB
            dummyB=dummyB.next if dummyB else headA
        return dummyA
    
    
        
         #should check dummy not dummy.next
        # dummya=headA
        # dummyb=headB
        # while dummya is not dummyb:
        #     dummya=dummya.next if dummya.next else headB
        #     dummyb=dummyb.next if dummyb.next else headA
        # return dummya or 0
