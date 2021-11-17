class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result= new ArrayList<>();
        Arrays.sort(nums);
        for (int i=0;  i<nums.length; i++) {
           if ((i>0 && nums[i]!=nums[i-1])  || i==0) {
           int l=i+1;
           int r=nums.length-1;
           while (l<r) {
               //System.out.println("nums[i]+nums[1]+nums[r] is: "+(nums[i]+nums[l]+nums[r] ));
               //System.out.println("nums[i] is: "+nums[i]+" nums[l] is: "+nums[l]+" nums[r] is: "+nums[r] );
               if (nums[i]+nums[l]+nums[r]==0) {
                  // System.out.println("l is: "+l+" r is : "+r);
                   ArrayList<Integer> temp = new ArrayList<Integer>();
                   if ((nums[l]!=nums[l-1]) ||  l==i+1) {
                       //temp.add(nums[i]);
                       //temp.add(nums[l]);
                       //temp.add(nums[r]);
                       result.add(Arrays.asList(nums[i],nums[l],nums[r]));
                       //result.add(temp);
                       //System.out.println("result is: "+result);
                   }
                   l=l+1;
                   r=r-1;
                   //System.out.println("l is: "+l+" r is : "+r);
                 }
               else if (nums[i]+nums[l]+nums[r]<0) {
                   l=l+1;
               }
               else {r=r-1;}
          }  
           }
           
        }
        return result;
    }
}
