# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        curr1 = head;
        curr2 = head;
        #while (curr2 is not None and curr2.next!=None) {
        while curr2 is not None and curr2.next is not None:
            curr1=curr1.next;
            curr2=curr2.next.next;
        
        
        
        second = curr1.next;
        curr1.next=None;
      
        prev =None;
        curr3 = second;
        next_ = None;
        
        #while (curr3!=None) {
        while curr3 is not None:
            next_=curr3.next;
            curr3.next=prev;
            prev=curr3;
            curr3=next_;
        
        
        second = prev;
        next1=None;
        first =head;
        
        while (second is not  None) :
            next1 = second.next;
            second.next= first.next;
            first.next=second;
            second = next1; 
            first=first.next.next;
        
        
        return head;
        
