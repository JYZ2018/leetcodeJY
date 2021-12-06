class Solution {
    public String longestPalindrome(String s) {
        //if (s.length()<=1) {return s;}
        int end=0; int start=0;
        for (int i=0; i<s.length();i++) {
            int n_1=palindrome(s,i,i); 
            int n_2=palindrome(s,i,i+1);
            int n_l=Math.max(n_1,n_2);
            if (n_l>end-start) {
                start=i-(n_l-1)/2;
                end=i+(n_l)/2;
                }
        }
        return s.substring(start,end+1);
    }
        
        public int palindrome(String s, int l, int r) {
            
            while (l>=0 && r<=s.length()-1 && s.charAt(l)==s.charAt(r)) {
                l=l-1;
                r=r+1;
            }
             
             return r-l-1; 
                   }
}
