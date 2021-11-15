class Solution {
    public int maxSubArray(int[] nums) {
        int sum_ = Integer.MIN_VALUE;
        int sum_max=Integer.MIN_VALUE;
        for (int i: nums) {
            if (sum_<0) {
                sum_=Math.max(sum_,i);
            }
            else {
                sum_=sum_+i;
            }
            sum_max=Math.max(sum_,sum_max);
        }
     return sum_max;   
    }
}
