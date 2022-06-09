class Solution {
    public int lengthOfLongestSubstring(String s) {
        
        int left=0, right=0, res=0;
        
        Set<Character> count = new HashSet<>();
        
        
        while (right<s.length()) {
            char temp = s.charAt(right);
            if (!count.contains(temp))  count.add(temp);
            else {
                while (count.contains(temp)) {
                    count.remove(s.charAt(left));
                    left++;
                }  
            }
             count.add(temp);
             res= Math.max(res, right-left+1);
             right++;
            //System.out.println(left+" "+right+" "+res+" "+count+" ");
        }
        
        return res;
        
    }
}
