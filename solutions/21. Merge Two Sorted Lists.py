# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # if list1.val<=list2.val:
        #     res=ListNode(list1.val,list2)
        #     list1=list1.next
        # else:
        #     res=ListNode(list2.val, list1)
        #     list2=list2.next
        # print(res)
        # while list1 and list2:
        #     if list1.val>=list2.val:
        '''
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next
        '''
            
        #  wrong, don;t know how to add element to the end of linked list 
        # should use dummy node
        
        # my original how to start the node, doesn't work
        if not list1:
            return list2
        if not list2:
            return list1
        
