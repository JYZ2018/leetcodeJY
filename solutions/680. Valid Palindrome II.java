class Solution {
    public boolean validPalindrome(String s) {
       return isPalindrome(s,true);
    }
    
    public boolean isPalindrome(String s, boolean change) {
        int start=0;
        int end=s.length()-1;
        while (start<end) {
        if (s.charAt(start)==s.charAt(end)) {
            start=start+1;
            end=end-1;
            //System.out.println("11111111111111");
        }
        else if (change==true) {
            // System.out.println("22222222222"+" start is: "+start +" end is: "+end +"sunstring is:"+ s.substring(start,end));
            
            return (isPalindrome(s.substring(start,end),false) || isPalindrome(s.substring(start+1,end+1),false));
             
        }
        else {// System.out.println("3333333333333");
            return false; } }
       
    return true;}
}
