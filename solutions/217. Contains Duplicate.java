class Solution {
    public boolean containsDuplicate(int[] nums) {
        //Map<Integer, Integer> record = new HashMap<>();
        Set<Integer> record = new HashSet<>();
        for (int num: nums) {
            if (record.contains(num)) {
                return true;
            }
            record.add(num);
        }
        
         return false;   
        
    }
}
