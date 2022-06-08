class Solution {
    Set<Integer> res = new HashSet<>();
        
        public int getSum(int n) {
            String s = Integer.toString(n);
            int sum =0;
            for (char num: s.toCharArray()) {
                int temp=Character.getNumericValue(num);
                sum=sum+temp*temp;
            }
            return sum;
        }
    
        
    public boolean isHappy(int n) {
        if (getSum(n)==1) return true;
        if (res.contains(getSum(n))) return false;
        res.add(getSum(n));
        return isHappy(getSum(n));
            
            
    }
    
  
}
