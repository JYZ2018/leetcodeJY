class Solution {
    public int[] twoSum(int[] nums, int target) {
        //not necessary
        //int[] res = new int[2];
        Map<Integer,Integer> record = new HashMap<>();
        for (int i=0; i<nums.length; i++) {
            if (record.containsKey(target-nums[i])) {
                //res[0]=record.get(target-nums[i]);
                //res[1]=i;
                return new int[] {record.get(target-nums[i]),i};
            }
            
            record.put(nums[i],i);
        }
        return null;
    }
}
