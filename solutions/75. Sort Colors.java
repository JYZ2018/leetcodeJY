class Solution {
    public void sortColors(int[] nums) {
        int p0=0; int p1=0; int p2=nums.length-1;
        while (p1<=p2) {
            if (nums[p1]==0 ) {int temp_0=nums[p0];
                               nums[p0]=0;
                               nums[p1]=temp_0;
                               p0++;
                               p1++;}
            else if (nums[p1]==1) {p1++;}               
            else if (nums[p1]==2) {
                int temp=nums[p2];
                nums[p2]=2;
                nums[p1]=temp;
                p2--;
            }
            
        }
      
    }
}
