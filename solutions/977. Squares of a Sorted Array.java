class Solution {
    public int[] sortedSquares(int[] nums) {
        int[] result = new int[nums.length];
        
        int sep=-1;
        
        for (int i=0; i<nums.length; i++) {
            //System.out.println("nums[i] is: "+nums[i]);
            if (nums[i]>=0) {
                sep=i;
                break;
            }
        }
        
        //System.out.println("sep is: "+sep);
        
        if (sep==0) {
            for (int i=0; i<nums.length; i++) {
                result[i]=nums[i]*nums[i];
            }
            return result;
        }
        
       int m=0;
       if (sep==-1) {
            for (int i=nums.length-1; i>=0; i--) {
                result[m]=nums[i]*nums[i];
                m=m+1;
            }
            return result;
        }
        
        int l=sep-1;
        int r=sep;
        int k=0;
        while (l>=0  && r<nums.length) {
            if ((nums[l]*nums[l])<(nums[r]*nums[r])) {
                result[k]=nums[l]*nums[l];
                l=l-1;
            }
            else {
                result[k]=nums[r]*nums[r];
                r=r+1;
            }
            k=k+1;
            }
        if (l==-1) {
            for (int i=r; i<nums.length; i++) {
                result[k]=nums[i]*nums[i];
                k=k+1;
            }
        }
        
        if (r==nums.length) {
            for (int i=l; i>=0; i--) {
                result[k]=nums[i]*nums[i];
                k=k+1;
            }
        }
            
            
        return result;
        }
     
    }
​
