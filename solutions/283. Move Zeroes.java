class Solution {
    public void moveZeroes(int[] nums) {
        int j=0;
        if (nums.length>1) {
        for (int i=0; i<nums.length; i++) {
            if (nums[i]!=0) {
                nums[j]=nums[i];
                 j=j+1;   
            }
            //System.out.println("nums[0] is: "+ nums[0]+"nums[1] is: "+nums[1]);
        }
    for (int m=j; m<nums.length;m++){
        nums[m]=0;
    }
        }
    }
}
