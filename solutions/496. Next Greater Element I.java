class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        int[] res = new int[nums1.length];
        Map<Integer,Integer> record = new HashMap<>();
        Stack<Integer> stack = new Stack<>();
        
        for (int num: nums2) {
            while (!stack.isEmpty() && num>stack.peek()) 
                record.put(stack.pop(),num);
            stack.push(num);
        }
        
        for (int i=0; i<nums1.length; i++) {
            res[i]=record.getOrDefault(nums1[i],-1);
        }
        
        return res;
    }
}
​
​
​
