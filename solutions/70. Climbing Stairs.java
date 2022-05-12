class Solution {
    public int climbStairs(int n) {
       
        int way1=0;
        int way2=1;
        int ways=0;
        for (int i=1; i<=n;i++) {
            ways=way1+way2;
            way1=way2;
            way2=ways;
           
           //System.out.println(way1+" "+way2);
        }
        
      return ways;  
    }
}
