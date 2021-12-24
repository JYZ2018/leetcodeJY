class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        //int index=n+m-1;
        
        while (n>0 && m>0) {
            if (nums1[m-1]>=nums2[n-1]) {
                nums1[n+m-1]=nums1[m-1];
                m=m-1;
            }
            else {
                nums1[n+m-1]=nums2[n-1];
                n=n-1;
            }
            //index=index-1;
        }
        
        while (n>=1) {
            nums1[n-1]=nums2[n-1];
            n=n-1;
        }
        
    }
}
