class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
       
        Set<Integer> s1 = new HashSet<>();
        Set<Integer> s2 = new HashSet<>();
        for (Integer num:nums1) s1.add(num);
       
        for (Integer num: nums2)  {
            if (s1.contains(num)) {
                s2.add(num);
            }
        }
        
        
        int[] res = new int[s2.size()];
        int idx =0 ;
        for (int s: s2) {
            res[idx++]=s;
        }
        
        return res;
        
    }
}
