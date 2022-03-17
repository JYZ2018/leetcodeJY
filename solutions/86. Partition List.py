# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        res1=dummy1=ListNode(0)
        res2=dummy2=ListNode(0)
        while head:
            if head.val<x:
                #print(res1)
                res1.next=head
                res1=res1.next
            else:
                res2.next=head
                res2=res2.next
            head=head.next 
            # print(res1)
            #print(res2)
        res2.next=None
        #print(dummy1,dummy2)
        
        res1.next=dummy2.next
        
        return dummy1.next
    
            
            
            
                
        print(dummy1,dummy2)
        
        
        # don't know how to add [4,3] back to 2, how to single 2 out
        '''
        res1=res2=res3=dummy=ListNode(0)
        while head:
            #print("1 head is: ",head)
            if head.val<x:
                res1.next=head
                res1=res1.next
