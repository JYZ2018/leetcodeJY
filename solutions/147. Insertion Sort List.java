/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode insertionSortList(ListNode head) {
        // recursion
        if (head==null || head.next==null) {
            return head;
        }
        
        head.next=insertionSortList(head.next);
        
        
        ListNode first = new ListNode(head.val);
//         ListNode temp0 =head;
//         while (temp0!=null) {
//             System.out.println("0 "+temp0.val);
//             temp0=temp0.next;
//         }
        
        
        ListNode curr =head;
        
        while (curr.next!=null && curr.next.val<=first.val) {
                 curr=curr.next;
            }
        
        ListNode next = curr.next;    
        curr.next=first;
        first.next = next;
        // ListNode temp =head;
        // while (temp!=null) {
        //     System.out.println(temp.val);
        //     temp=temp.next;
        // }
        //System.out.println();
        return head.next;
        
            
            
        
        
        
        
        
        
        
        
        
        
