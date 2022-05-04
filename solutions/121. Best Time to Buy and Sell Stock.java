class Solution {
    public int maxProfit(int[] prices) {
     //    int min=prices[0];
     //    int profit=0;
     //    for (int i:prices) {
     //        profit=Math.max(profit,(i-min));
     //        if (i<min) {min=i;}
     //    }
     // return profit;
    
     int min=prices[0];
     int profit=0;
     for (int i: prices) {
         profit=Math.max(profit,i-min);
         if (i<min) {
             min=i;
         }    
     }
    return profit;                      
    }
}
