        if (res_1 !=null) {
            longL=l1;
            shortL=l2;
        }
        else {
            longL =l2;
            shortL=l1;
        }
        
        
        int under = 0;
        int over = 0;
        while (longL!=null ) {
            int shortVal;
            if (shortL ==null) shortVal=0;
            else shortVal=shortL.val;
            
            int sum = longL.val+shortVal+over;
            
            if (sum>=10) {
                under = sum % 10;
                over=sum/10;
            }
            else {
                under=sum;
                over=0;
            }
            //System.out.println(under +" "+over);
            
            longL.val = under;
            if (longL.next==null && over!=0) {
                longL.next = new ListNode(over);
                if (res_1!=null) return l1;
                else return l2;
                
            }
            longL=longL.next;
            if (shortL!=null) shortL=shortL.next;    
        }
        
        
    if (res_1!=null) return l1;
    else return l2;
        
    }
}
