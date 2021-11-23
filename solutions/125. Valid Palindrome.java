class Solution {
    public boolean isPalindrome(String s) {
        int l=0;
        int r=s.length()-1;
        s=s.toLowerCase();
        while (l<r) { 
            
        while  ((s.charAt(l)<'0' || (s.charAt(l)>'9' && s.charAt(l)<'a')  || s.charAt(l)>'z')  && l<r) { l=l+1;}
        while  ((s.charAt(r)<'0' || (s.charAt(r)>'9' && s.charAt(r)<'a') || s.charAt(r)>'z') && l<r) { r=r-1;}
        if (s.charAt(l)!=s.charAt(r)) {return false;}
        else { l=l+1;
             r=r-1;}}
        return true;           
    }
}
